#!/usr/bin/python
# -*- coding:utf-8 -*-


import re
import sys
from datetime import datetime
from utils.logger import Logger
from utils.downloader import Downloader
from utils.spider import spider_by_lxml, spider_by_beautifulsoup_find, spider_by_beautifulsoup_select
from utils.pipeline import save_into_csv


sys.stdout = Logger(r'./logs/douban_log_{}.txt'.format(datetime.now().strftime('%Y-%m-%d_%H-%M-%S')))


if __name__ == '__main__':

    original_url = r'https://movie.douban.com/top250?start={}&filter='

    downloader = Downloader()

    data_list = []

    for i in range(10):
        original_html = downloader.get_html(original_url.format(i * 25))
        cleaned_html = re.sub(r'&nbsp;', ' ', original_html)
        cleaned_html = re.sub(r'\n', '', cleaned_html)
        cleaned_html = re.sub(r'\r', '', cleaned_html)
        # cleaned_html = re.sub(r'<br\s*/*>', '', cleaned_html)
        data_list += spider_by_lxml(cleaned_html)
        # data_list += spider_by_beautifulsoup_find(cleaned_html)
        # data_list += spider_by_beautifulsoup_select(cleaned_html)

    save_into_csv(data_list)
    # pipreqs . --force --encoding=utf-8
