import pymysql
from common.ConfTools import DoConf
from common import constant
from common.LogTools import DoLogs

log = DoLogs(__name__)


class DoMysql:

    def __init__(self):
        conf = DoConf(constant.globe_conf_dir)
        # 打开数据库连接
        self.db = pymysql.Connection(host=conf.get_value('db', 'host'),
                                     user=conf.get_value('db', 'username'),
                                     password=conf.get_value('db', 'pwd'),
                                     cursorclass=pymysql.cursors.DictCursor)  # 将游标执行的结果以字典返回
        # 使用 cursor() 方法创建一个游标对象 cursor
        self.cursor = self.db.cursor()

    # 把结果集的第一行以字典的形式返回
    def read_fetchone(self, sql):
        self.cursor.execute(sql)
        datas = self.cursor.fetchone()
        self.db.commit()
        return datas

    # 把多行结果以字典的形式返回一个大列表
    def read_fetchall(self, sql):
        self.cursor.execute(sql)
        datas = self.cursor.fetchall()
        self.db.commit()
        return datas

    def insert_one(self, sql):
        """
        单条执行插入
        :param sql:
        :return:
        """
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except:
            # 发生错误时回滚
            self.db.rollback()

    def insert_all(self, sql, values):
        """
        批量执行插入
        :param sql:
        :param values:
        :return:
        """
        try:
            self.cursor.executemany(sql, values)
            self.db.commit()
            log.mylog.info("批量添加成功")
        except Exception as e:
            self.db.rollback()
            log.mylog.info("添加失败,错误原因{}".format(e))
            raise e

    def update(self, sql):
        """
        更新数据
        :param sql:
        :return:
        """
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            log.mylog.info("更新失败,错误原因{}".format(e))
            raise e

    def delete(self, sql):
        """
        执行删除操作
        :param sql:
        :return:
        """
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except:
            # 发生错误时回滚
            self.db.rollback()

    def close(self):
        self.cursor.close()
        self.db.close()


if __name__ == '__main__':
    cases = DoMysql().read_fetchall('')
    print(cases)
