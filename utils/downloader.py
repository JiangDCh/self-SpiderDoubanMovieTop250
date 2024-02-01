#!/usr/bin/python
# -*- coding:utf-8 -*-


import random
from datetime import datetime

import requests
import urllib.request
import urllib.error


# supper: None
# TODO: 用于下载网页的HTML文件
class Downloader(object):

    # input: String
    # output: None
    # TODO: 定义初始化类的方法，在初始化方法中设置好headers
    def __init__(self, filename='Default.log'):
        self.headers = [
            {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                           'Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'},
            {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                           'Chrome/100.0.4896.127 Safari/537.36'},
        ]

    # input: String
    # output: String
    # TODO: 通过requests获取网页的HTML
    def get_html_by_requests(self, url, timeout=5):
        try:
            response = requests.get(url, headers=random.choice(self.headers), timeout=timeout)
            response.raise_for_status()
            response.encoding = response.apparent_encoding
            print(str(datetime.now()) + ': ' + '目标网页{}获取成功。'.format(url))
            return response.text
        except requests.exceptions.MissingSchema as e:
            print(str(datetime.now()) + ': ' + '{}被触发，请求中缺少请求协议，请检查URL的请求协议。'.format(e))
        except requests.exceptions.ConnectionError as e:
            print(str(datetime.now()) + ': ' + '{}被触发，存在网络连接错误，请检查本地的网络连接情况。'.format(e))
        except requests.exceptions.Timeout as e:
            print(str(datetime.now()) + ': ' + '{}被触发，网络连接超时，请检查本地的网络连接质量。'.format(e))
        except requests.exceptions.HTTPError as e:
            print(str(datetime.now()) + ': ' + '{}被触发，目标网页{}的返回状态异常，状态码为{}。'.format(e, url, e.response.status_code))
        except requests.exceptions.RequestException as e:
            print(str(datetime.now()) + ': ' + '{}被触发，出现意料之外的访问异常，请检查。'.format(e))

    # input: String
    # output: String
    # TODO: 通过urllib获取网页的HTML
    def get_html_by_urllib(self, url, timeout=5):
        try:
            request = urllib.request.Request(url, headers=random.choice(self.headers))
            response = urllib.request.urlopen(request, timeout=timeout)
            print(str(datetime.now()) + ': ' + '目标网页{}获取成功。'.format(url))
            return response.read().decode('utf-8')
        except ValueError:
            print(str(datetime.now()) + ': ' + '{}被触发，请求中缺少请求协议，请检查URL的请求协议。'.format(ValueError))
        except urllib.error.HTTPError as e:
            print(str(datetime.now()) + ': ' + '{}被触发，{}，状态码为{}，请检查网页状态。'.format(e, e.code, e.reason))
        except urllib.error.URLError as e:
            print(str(datetime.now()) + ': ' + '{}被触发，{}，请检查连接情况。'.format(e, e.reason))
