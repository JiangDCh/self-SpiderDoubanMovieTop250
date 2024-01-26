#!/usr/bin/python
# -*- coding:utf-8 -*-


import re
import sys
import time
import random
from tqdm import tqdm
from datetime import datetime


from utils.logger import Logger
from utils.downloader import Downloader
from utils.spider import spider_by_lxml, spider_by_beautifulsoup_find, spider_by_beautifulsoup_select
from utils.pipeline import save_into_csv


sys.stdout = Logger(r'./logs/douban_log_{}.txt'.format(datetime.now().strftime('%Y-%m-%d_%H-%M-%S')))

# TODO: 程序入口主方法
if __name__ == '__main__':
    original_url = r'https://movie.douban.com/top250?start={}&filter='
    downloader = Downloader()

    data_list = []
    for i in tqdm(range(10), desc="Processing"):
        original_html = downloader.get_html_by_requests(original_url.format(i * 25))
        # original_html = downloader.get_html_by_urllib(original_url.format(i * 25))

        cleaned_html = re.sub(r'&nbsp;', ' ', original_html)
        cleaned_html = re.sub(r'\n', '', cleaned_html)
        cleaned_html = re.sub(r'\r', '', cleaned_html)

        data_list += spider_by_lxml(cleaned_html)
        # data_list += spider_by_beautifulsoup_find(cleaned_html)
        # data_list += spider_by_beautifulsoup_select(cleaned_html)

        time.sleep(random.uniform(1, 2))

    save_into_csv(data_list)

    # pipreqs . --force --encoding=utf-8
