from common import constant
from common.ExcelTools import DoExcel
from common.SqlTools import DoMysql
from common.ConfTools import DoConf


class ImportData:

    def __init__(self, sheet_name):
        self.excel = DoExcel(constant.excel_import_dir, sheet_name)
        self.cnf = DoConf(constant.globe_conf_dir)
        self.db = DoMysql()

    def data_import(self):
        """
        导入excel数据
        :return:
        """
        cases = self.excel.read_excel()
        datas = [tuple(case.__dict__.values()) for case in cases]
        """
        上面一行的解释
        lsit1 = []
        for case in cases
            dict1 = case.__dict__   # __dict__ 获取对象的所有属性和方法，并以字典的格式返回
            values = tuple(dict1.values())   # dict1.values() 获取字典的所有值
            list1.append(values） # 返回的结果[(),(),()]
        """
        sql = self.cnf.get_value("sql_data", "import_sql")
        self.db.insert_all(sql, datas)
        print("导入成功")


if __name__ == '__main__':
    import_data = ImportData("infra-marketing")
    result = import_data.data_import()
