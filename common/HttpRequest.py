import requests

from json import JSONDecodeError
from common.LogTools import DoLogs


class Request:
    log = DoLogs(__name__).mylog

    def __init__(self):
        self.session = requests.sessions.session()

    def http_request(self, parametric_key: str, method: str, url: str, data: dict, headers=None, cookies=None):
        """
        使用request库根据不同的请求方式进行http请求
        :param parametric_key:入参关键字， params(一般在url?参数名=参数值), data(一般用于form表单类型参数)， json(一般用于json类型请求参数)
        :param method:请求方法
        :param url:请求url
        :param data:请求参数
        :param headers:请求头
        :param cookies: 请求cookies
        :return: 返回请求响应对象
        """
        if parametric_key == 'params':
            resp = self.session.request(method, url, params=data, headers=headers, cookies=cookies)
        elif parametric_key == 'data' or parametric_key == 'file':
            resp = self.session.request(method, url, data=data, headers=headers, cookies=cookies)
        elif parametric_key == 'json':
            resp = self.session.request(method, url, json=data, headers=headers, cookies=cookies)
        else:
            raise ValueError(
                '可选关键字为params, json, data, file')
        try:
            response = resp.json()
        except JSONDecodeError:
            self.log.info(resp)  # 调试
            self.log.info('转字典格式报错')
            response = None
        self.log.info(
            f'\n最终请求地址:{url}\n请求方法:{method}\n请求头:{headers}\n请求参数:{data}\n响应数据:{response}')
        self.log.info(f'响应耗时(s): {resp.elapsed.total_seconds()}')
        return response

    def close(self):
        self.session.close()


if __name__ == '__main__':
    pass

