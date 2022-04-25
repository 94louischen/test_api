# -*- coding: utf-8 -*-
# @Time : 2021/9/13 10:45
# @Author : chenxuan

import jsonpath
from common import context
from tools.data_process import DataProcess
from data.extract_data import ExtractData


class Mixins:

    def send_request(self, interface_init: tuple, case: dict) -> object:
        """
        处理case数据，转换成可用数据发送请求
        :param interface_init:前置处理函数，返回cf, resp, mysql, log, mixins, yml等对象，以tuple类型返回
        :param case:数据库存储的用例数据，case对应一条记录，以字典格式返回
        :return: 返回请求响应对象
        """
        url = DataProcess.handle_path(case.get("url"))
        if case.get("data_type") == 'file':
            data, headers = DataProcess.handle_files(case.get("params"), case.get("headers"))
            header = DataProcess.handle_header(headers, url, data)
        else:
            data = DataProcess.handle_data(case.get("params"), url, case.get("title"))
            header = DataProcess.handle_header(case.get("headers"), url, data)
        # 发送请求
        response = interface_init[1].http_request(case.get("data_type"), case.get("method"), url, data, header)
        return response

    def extraction(self, interface_init: tuple, case: dict, response: object):
        """
        参数动态提取
        :param interface_init:conftest中前置函数方法
        :param case:单条用例数据
        :param response:接口响应对象
        :return:
        """
        global key
        extraction = DataProcess.handle_extra(case.get("extraction"))
        if extraction:  # 如果不需要参数提取，那么将不处理
            try:
                for key, value in extraction.items():
                    if key == 'building_ids':
                        setattr(ExtractData, key,
                                str(jsonpath.jsonpath(response, value)).replace('[', '').replace(']', '').replace('\'',
                                                                                                                  ''))
                    elif key in ['building_ids1', 'unit_ids', 'floor_ids', 'room_ids']:
                        setattr(ExtractData, key, jsonpath.jsonpath(response, value))
                    elif key == 'regionList':
                        setattr(ExtractData, key,
                                [{"regionId": i.pop("regionId"), "regionName": i.pop("regionName")} for i in
                                 jsonpath.jsonpath(response, value)])
                    elif key == 'scene':
                        setattr(ExtractData, key,
                                jsonpath.jsonpath(response, "$.result.appletsUrl")[0].split('=')[1])
                    elif key == 'houseIds':
                        setattr(ExtractData, key, jsonpath.jsonpath(response, value))
                    else:
                        setattr(ExtractData, key, jsonpath.jsonpath(response, value)[0])
                    interface_init[3].mylog.info("提取的参数值为{}:{}".format(key, getattr(ExtractData, key)))
            except Exception:
                interface_init[3].mylog.info(f"提取{key}参数失败")

    def response_assert(self, interface_init: tuple, case: dict, response: object):
        """
        遍历断言用例中所设置的预期值
        :param interface_init: conftest中前置函数方法
        :param case:
        :param response:
        :return:
        """
        global result, assert_key, resp_message
        expected = DataProcess.handle_expected(case.get("expected"))
        if expected:  # 如果没有预期断言值，那么将不做断言
            try:
                for assert_key in expected:
                    if assert_key == 'message':
                        resp_message = jsonpath.jsonpath(response, expected.get(assert_key)[1])[0]  # 实际接口响应message
                        interface_init[3].mylog.info(
                            f"{assert_key}断言的实际结果:{resp_message}，预期结果是:{expected.get(assert_key)[0]}")
                        assert expected.get(assert_key)[0] == resp_message
                    elif assert_key in ['result', 'result_items']:
                        assert jsonpath.jsonpath(response, expected.get(assert_key))[0]
                    elif assert_key == 'check_value':
                        for dict_key, value in expected.get('check_value').items():
                            interface_init[3].mylog.info(
                                f"{assert_key}断言的实际结果:{jsonpath.jsonpath(response, dict_key)[0]}，预期结果是:{value}")
                            assert jsonpath.jsonpath(response, dict_key)[0] == value
                    else:
                        interface_init[3].mysql.info("没有匹配到相应的断言key")
                result = "pass"
            except (AssertionError, TypeError):
                result = "fail"
                raise AssertionError(f'{assert_key}断言失败')
            finally:
                interface_init[2].update(interface_init[0].get_value('sql_data', 'update_case').
                                         format(resp_message, result, context.get_now_time(), case.get("id")))
                interface_init[3].mylog.info("当前执行的结果是:{}".format(result))
