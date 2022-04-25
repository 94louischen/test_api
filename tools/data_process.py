# -*- coding: utf-8 -*-
# @Time : 2021/9/9 16:55
# @Author : chenxuan


from tools.__init__ import *


class DataProcess:

    @classmethod
    def handle_path(cls, url: str) -> str:
        """
        路径参数处理
        :param path_str: 带提取表达式的字符串 #host#/security/city/businessArea/updateById/#id#
        return  https://test-xxxxx.com/security/city/businessArea/updateById/1
        """
        url = param_replace(url)
        # DoLogs(__name__).mylog.info(f'请求地址: {url}')
        return url

    @classmethod
    def handle_header(cls, header_str: str, url: str, data: dict) -> dict:
        """
        处理header，将相关签名的信息加入到请求头
        :param header_str: 用例栏中的header
        :param url: url
        :param data: 请求体
        :return: 返回完整的请求头
        """
        if header_str:
            header_str = param_replace(header_str)
            header = eval(header_str)
            if url.find(DoConf(constant.globe_conf_dir).get_value("data", "online_host")) != -1:
                headers = dict(header, **get_online_sign(url, data))
            elif url.find('web-im-communication') != -1:  # IM接口的请求头不参与签名
                headers = header
            elif url.find(DoConf(constant.globe_conf_dir).get_value("data", "host")) != -1:
                headers = dict(header, **get_sign(token=getattr(ExtractData, "token")))
            elif url.find(DoConf(constant.globe_conf_dir).get_value("data", "host_coop")) != -1:
                headers = dict(header, **get_sign(token=getattr(ExtractData, "token")))
            elif url.find(DoConf(constant.globe_conf_dir).get_value("data", "agent_host")) != -1:
                headers = dict(header, **get_sign(token=getattr(ExtractData, "token")))
            else:  # openApi接口不参与签名
                headers = header
            # DoLogs(__name__).mylog.info(f'请求头: {headers}')
            return headers

    @classmethod
    def handle_data(cls, variable: str, url: str, title: str) -> dict:
        """
        请求体数据处理
        :param variable: 请求体中包含需求替换的变量如：#id#
        :return: 返回python的对象
        """
        if variable:
            data = param_replace(variable)
            if url.find('web-im-communication') != -1 and title.find('腾讯回调函数') == -1:
                variable = get_im_sign(data)
            else:
                variable = convert_json(data)
            return variable

    @classmethod
    def handle_files(cls, variable: str, headers: str) -> tuple:
        """
        文件上传的请求体参数处理
        :param variable: 请求体参数
        :param headers: 请求头
        :return:返回处理后的请求体和请求头元组
        """
        variable = eval(param_replace(variable))
        headers = eval(param_replace(headers))
        key = list(variable)[0]
        file_obj = MultipartEncoder(fields=dict(variable, **{
            key: (variable[key], open(os.path.join(constant.data_dir, variable[key]), 'rb'),
                  'text/plain')}),
                                    boundary=uuid4().hex)
        headers["Content-Type"] = file_obj.content_type
        return file_obj, headers

    @classmethod
    def handle_expected(cls, expected: str) -> dict:
        """
        处理接口断言的预期值
        :param expected:
        :return:
        """
        try:
            expected = eval(param_replace(expected))
        except Exception:
            DoLogs(__name__).mylog.info('空参数无法执行eval()')
        return expected

    @classmethod
    def handle_extra(cls, extraction: str) -> dict:
        """
        处理需要进行接口传递的数据
        :param extraction:
        :return:
        """
        try:
            extraction = eval(param_replace(extraction))
        except Exception:
            DoLogs(__name__).mylog.info('空参数无法执行eval()')
        return extraction

    @classmethod
    def handle_sql(cls, sql: str) -> str:
        """
        处理sql数据
        :param sql:
        :return:
        """
        try:
            sql = param_replace(sql)
        except Exception:
            DoLogs(__name__).mylog.info('参数替换失败')
        return sql
