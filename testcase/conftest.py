import pytest
from common import constant, context
from common.HttpRequest import Request
from common.ConfTools import DoConf
from common.LogTools import DoLogs
from common.SqlTools import DoMysql
from common.yaml_tools import YamlTools
from tools.mixins import Mixins
from data.extract_data import ExtractData


@pytest.fixture(scope="class")
def interface_init():
    cf = DoConf(constant.globe_conf_dir)
    resp = Request()
    mysql = DoMysql()
    log = DoLogs(__name__)
    mixins = Mixins()
    yml = YamlTools()
    # 前置生成身份证和手机号
    setattr(ExtractData, 'id_card', context.generate_id_card())
    setattr(ExtractData, 'phone', context.generate_phone())
    setattr(ExtractData, 'userName', context.generate_name())
    setattr(ExtractData, 'timeStamp', context.get_timestamp())
    yield cf, resp, mysql, log, mixins, yml
    # 生成器后置处理逻辑
    resp.close()
    mysql.close()


@pytest.fixture(scope="class")
def teardown_class(interface_init):
    """
    删除用户数据和组织数据
    :param interface_init:
    :return:
    """
    yield
    if interface_init[0].get_value('data', 'host') not in ['https://www.xxxx.com']:
        try:
            sql_list = interface_init[5].read_yaml_all(constant.database_dir)
            sql_list = eval(context.param_replace(str(sql_list)))
            for sql_obj in sql_list:
                for key, value in sql_obj.items():
                    for sql in value:
                        interface_init[2].delete(sql)
                        interface_init[3].mylog.info("执行的sql为{}".format(sql))
        except Exception as e:
            interface_init[3].mylog.error(e)
            raise e
