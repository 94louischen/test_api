import json

import yaml
from common import constant


class YamlTools:

    def __init__(self):
        pass

    def write_yaml(self, *args):
        """
        把自定义的类型数据写入yaml文件
        :param args:
        :param kwargs:
        :return:
        """
        with open(args[0], "a+", encoding="utf-8") as file:
            yaml.dump(args[1], stream=file, allow_unicode=True)

    def write_yaml_all(self, *args):
        with open(args[0], "a+", encoding="utf-8") as file:
            yaml.dump_all([args[1], args[2], args[3]], stream=file, allow_unicode=True)

    def read_yaml(self, file):
        """
        读取yaml的内容
        :param args:
        :return:
        """
        with open(file, "r", encoding="utf-8") as file:
            data = yaml.load(file, Loader=yaml.FullLoader)
            return data

    def read_yaml_all(self, file):
        """
        读取yaml中的多条数据，并返回一个列表
        :param file: yaml文件
        :return:list
        """
        with open(file, "r", encoding="utf-8") as file:
            datas = yaml.load_all(file, Loader=yaml.FullLoader)
            return [data for data in datas]


if __name__ == '__main__':
    yml = YamlTools()
    test_data = yml.read_yaml_all("")
    print(test_data)
