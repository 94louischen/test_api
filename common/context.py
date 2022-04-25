import json
import string

from faker import Faker
import re
import time
import hashlib
import random
import datetime
import configparser
from common.ConfTools import DoConf
from common import constant
from data.extract_data import ExtractData


def param_replace(data: str) -> str:
    """
    替换data中带##的字段
    :param data:
    :return:
    """
    if data:
        data = str(data)
        p = "#(.*?)#"
        while re.search(p, data):
            params = re.search(p, data)
            params1 = params.group(1)
            try:
                params2 = DoConf(constant.globe_conf_dir).get_value('data', params1)
                if type(params2) != str:
                    params2 = str(params2)
            except configparser.NoOptionError as e:
                if hasattr(ExtractData, params1):
                    params2 = getattr(ExtractData, params1)
                    if type(params2) != str:
                        params2 = str(params2)
                elif params1 == 'get_now_time(1)':
                    exec(params1)  # exec可以执行python代码
                    params2 = getattr(ExtractData, 'date')
                elif params1 == 'generate_name()':
                    exec(params1)
                    params2 = getattr(ExtractData, 'real_name')
                elif params1 == 'generate_id_card()':
                    exec(params1)
                    params2 = getattr(ExtractData, 'id_number')
                elif params1 == 'generate_phone()':
                    exec(params1)
                    params2 = getattr(ExtractData, 'mobile_number')
                elif params1 == 'generate_title()':
                    exec(params1)
                    params2 = getattr(ExtractData, 'title')
                else:
                    print("找不到相关值")
                    params2 = 'None'
                    # raise e
            data = re.sub(p, params2, data, count=1)
    return data


def get_random_number(data=None):
    """
    生成一个当前日期和随机数的组合
    :param data:
    :return:
    """
    if data:
        today = datetime.datetime.now().strftime('%m%d')
        num = random.randint(1, 100)
        data = data + "_" + today + str(num)
        return data


def get_now_time(istime: int = 0):
    """
     获取当前时间
    :param istime: 标记是否返回详细时间
    :return: 返回当前时间
    """
    if istime:
        date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    else:
        date = datetime.datetime.now().strftime('%Y-%m-%d')
    setattr(ExtractData, 'date', date)
    return date


def modify_date(data):
    if data:
        # 匹配2020-07-06T19:00:00这样的日期，然后取T后面的值
        p = "A\\d{4}-\\d{2}-\\d{2}(T\\d{2}:\\d{2}:\\d{2})A"
        p1 = "B(\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2})B"
        while re.search(p, data):
            params1 = re.search(p, data).group(1)
            today = datetime.datetime.now().strftime('%Y-%m-%d')
            update_time = today + params1
            # 替换所传参数中的日期
            data = re.sub(p, update_time, data, count=1)
        # 匹配以"B()B"包裹的日期字段，并替换为当前日期
        if re.search(p1, data):
            today = (datetime.datetime.now() + datetime.timedelta(minutes=1)).strftime('%Y-%m-%dT%H:%M:%S')
            data = re.sub(p1, today, data, count=1)
    return data


def get_sign(version='xxx', randomMap='xxx', Prefix='xxx', suffix='xxx', token=None):
    """
    运营后台生成签名
    :param version: pc版本
    :param randomMap: 加密串允许字符
    :param Prefix: 签名前缀
    :param suffix: 签名后缀
    :param token: 登录接口返回的token
    :return: 签名相关的请求头
    """
    pass


def data_format(data=None):
    """
    python不支持相关java的数据类型，所以调整一下
    :param data:
    :return:
    """
    if not isinstance(data, str):
        data = str(data).replace('null', 'None').replace('true', 'True').replace('false', 'False')
    return data


def generate_id_card():
    """
    :return:返回身份证
    """
    fake = Faker("zh_CN")
    id_number = fake.ssn()
    setattr(ExtractData, 'id_number', id_number)
    return id_number


def generate_phone():
    """
    :return: 返回电话号码
    """
    fake = Faker("zh_CN")
    mobile_number = fake.phone_number()
    setattr(ExtractData, 'mobile_number', mobile_number)
    return mobile_number


def generate_name():
    """
    :return: 返回姓名
    """
    fake = Faker("zh_CN")
    real_name = fake.name()
    setattr(ExtractData, 'real_name', real_name)
    return real_name


def get_online_sign(url: str, data, platform='xxx'):
    """
    外网项目get接口签名
    :param url:请求url
    :param data:请求体参数
    :param platform:加密码
    :return:返回请求头
    """
    pass


def get_im_sign(body):
    """
    IM即时通讯接口请求签名
    :param body: 请求body
    :return: 返回指定格式的请求体
    """
    pass


def get_timestamp():
    """
    :return: 返回当前10位时间戳
    """
    timestamp = int(time.time())
    return timestamp


def get_sms_code(sql: str = None):
    """
    提取验证码
    :param sql: 需要执行的sql
    :return: 短信验证码
    """
    time.sleep(1)  # 默认等1秒
    global sms_code
    from common.SqlTools import DoMysql
    import re
    mysql_obj = DoMysql()
    try:
        sms_text = mysql_obj.read_fetchone(sql)
        sms_code = re.findall('您的验证码：(.+?)，该验证码5分钟内有效，限本次使用，请勿泄露验证码。', sms_text.get('FCONTENT'))[0]
    except Exception:
        sms_code = 123456
    finally:
        return sms_code


def generate_title():
    """
    随机生成title
    """
    title = get_random_number("测试数据")
    setattr(ExtractData, 'title', title)


if __name__ == '__main__':
    print(generate_name())
    print(generate_id_card())
    print(generate_phone())