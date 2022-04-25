# -*- coding:utf-8 -*-
import allure
import pytest
from common import constant
from common.ConfTools import DoConf
from common.SqlTools import DoMysql

pytestmark = pytest.mark.slow


@pytest.mark.test
@pytest.mark.usefixtures("interface_init")
class TestAuthorization:
    cases = DoMysql().read_fetchall(DoConf(constant.globe_conf_dir).get_value("sql_data", "login_data"))

    @pytest.mark.parametrize("case", cases)
    def test_get_token(self, interface_init, case):
        allure.dynamic.title(case["title"])  # 动态获取用例标题
        interface_init[3].mylog.info("当前执行的用例是:{}".format(case["title"]))
        response = interface_init[4].send_request(interface_init, case)
        interface_init[4].response_assert(interface_init, case, response)
        interface_init[4].extraction(interface_init, case, response)
