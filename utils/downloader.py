#!/usr/bin/python
# -*- coding:utf-8 -*-


import time
import random
import requests
from requests.exceptions import MissingSchema, RequestException, HTTPError, ConnectionError, Timeout


# supper: None
# TODO: 用于下载网页的HTML文件
class Downloader(object):

    # input: String
    # output: None
    # TODO: 定义初始化类的方法
    def __init__(self, filename='Default.log'):
        self.headers = [
            {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                           'Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'},
            {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                           'Chrome/100.0.4896.127 Safari/537.36'},
        ]

    # input: String
    # output: String
    # TODO: 获取网页的HTML
    def get_html(self, url):
        response = None
        try:
            response = requests.get(url, headers=random.choice(self.headers), timeout=5)
            response.raise_for_status()
            response.encoding = response.apparent_encoding
            return response.text
        except MissingSchema:
            print('{}被触发，请求中缺少请求协议，请检查URL的请求协议。'.format(MissingSchema))
        except ConnectionError:
            print('{}被触发，存在网络连接错误，请检查本地的网络连接情况。'.format(ConnectionError))
        except Timeout:
            print('{}被触发，网络连接超时，请检查本地的网络连接质量。'.format(Timeout))
        except HTTPError:
            print('{}被触发，目标网页{}的返回状态异常，状态码为{}。'.format(Timeout, url, response.status_code))
        except RequestException:
            print('{}被触发，出现意料之外的访问异常，请检查。。'.format(RequestException))
        finally:
            time.sleep(random.uniform(1, 2))
            print('目标网页{}获取成功!'.format(url))
