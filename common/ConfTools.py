# -*- coding:utf-8 -*-
from configparser import ConfigParser
from common import constant


class DoConf:

    def __init__(self, files):
        self.cf = ConfigParser()
        self.cf.read(files, encoding='utf-8')
        switch = self.cf.get('switch', 'on')
        if switch == "dev":
            self.cf.read(constant.conf_test_dir, encoding='utf-8')
        elif switch == "uat":
            self.cf.read(constant.conf_uat_dir, encoding='utf-8')
        elif switch == "prod":
            self.cf.read(constant.conf_prod_dir, encoding='utf-8')
        else:
            print("没有匹配到对应的文件")

    def get_value(self, sections, options):
        value = self.cf.get(sections, options)
        return value


if __name__ == '__main__':
    dc = DoConf(constant.globe_conf_dir)
    print(dc.get_value('dev_db', 'host'))
