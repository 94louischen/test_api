# -*- coding: utf-8 -*-
import os
import pytest
import shutil

from common.constant import report_dir

# 此命令在windows10上使用，以下两行是强制清空目录然后在新建
shutil.rmtree(report_dir)
os.mkdir(report_dir)
pytest.main(["-m", "test", "--alluredir=output/report"])
# 此命令在windows10上使用，以下是调用cmd并生成allure报告
os.system("allure serve output/report")
