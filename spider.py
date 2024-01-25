#!/usr/bin/python
# -*- coding:utf-8 -*-


import re
import sys
from lxml import etree
from datetime import datetime
from utils.logger import Logger
from utils.downloader import Downloader


sys.stdout = Logger(r'./logs/douban_log_{}.txt'.format(datetime.now().strftime('%Y-%m-%d_%H-%M-%S')))

original_url = r'https://movie.douban.com/top250?start={}&filter='

downloader = Downloader()

for i in range(10):
    original_html = downloader.get_html(original_url.format(i * 25))
    cleaned_html = re.sub(r'&nbsp;', ' ', original_html)
    cleaned_html = re.sub(r'\n', '', cleaned_html)
    cleaned_html = re.sub(r'\r', '', cleaned_html)
    # cleaned_html = re.sub(r'<br\s*/*>', '', cleaned_html)
    tree = etree.HTML(cleaned_html)
    for movie_div in tree.xpath('//div[@id="content"]//div[@class="info"]'):
        title = movie_div.xpath('div[@class="hd"]/a/span/text()')
        print(title)
        title = ' '.join(title)
        print(title)
        print(movie_div.xpath('div[@class="bd"]/p/text()'))
        print(''.join(movie_div.xpath('div[@class="bd"]/p/text()')))
        break

    break
# pipreqs . --force --encoding=utf-8
