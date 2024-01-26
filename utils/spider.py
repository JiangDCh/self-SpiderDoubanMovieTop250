#!/usr/bin/python
# -*- coding:utf-8 -*-


import re
from lxml import etree
from bs4 import BeautifulSoup
from datetime import datetime


def spider_by_lxml(html):
    tree = etree.HTML(html)
    return_list = []

    for movie_div in tree.xpath('//div[@id="content"]//div[@class="info"]'):
        title = movie_div.xpath('div[@class="hd"]/a/span/text()')
        print(str(datetime.now()) + ': ' + str(title))
        title = ''.join(title)
        print(str(datetime.now()) + ': ' + title)

        info = movie_div.xpath('div[@class="bd"]/p/text()')
        print(str(datetime.now()) + ': ' + str(info))
        info_1 = re.sub(r'\s{2,}', ' ', info[0])
        info_1 = re.sub(r'^\s+', '', info_1)
        info_2 = re.sub(r'\s{2,}', ' ', info[1])
        info_2 = re.sub(r'^\s+', '', info_2)
        print(str(datetime.now()) + ': ' + info_1, info_2)

        point = movie_div.xpath('div[@class="bd"]/div/span[@class="rating_num"]/text()')[0]
        print(str(datetime.now()) + ': ' + point)

        num_of_comment = movie_div.xpath('div[@class="bd"]/div/span[not(@*)]/text()')[0]
        print(str(datetime.now()) + ': ' + num_of_comment)
        num_of_comment = re.compile(r'^\d+').match(num_of_comment).group()
        print(str(datetime.now()) + ': ' + num_of_comment)

        short_comment = movie_div.xpath('div[@class="bd"]/p[@class="quote"]/span/text()')
        print(str(datetime.now()) + ': ' + str(short_comment))
        short_comment = ''.join(short_comment)
        print(str(datetime.now()) + ': ' + short_comment)

        return_list.append([title, info_1, info_2, point, num_of_comment, short_comment])

    print(str(datetime.now()) + ': ' + '使用lxml解析成功。')
    return return_list


def spider_by_beautifulsoup_select(html):
    soup = BeautifulSoup(html, 'html.parser')
    return_list = []

    for movie_div in soup.select('#content .info'):
        title = movie_div.select_one('.hd a span').get_text(strip=True)
        print(str(datetime.now()) + ': ' + title)

        info = movie_div.select_one('.bd p').get_text(strip=True, separator='\n')
        print(str(datetime.now()) + ': ' + info)
        info_1, info_2 = re.sub(r'^\s+|\s{2,}', ' ', info).split('\n', 1)
        print(str(datetime.now()) + ': ' + info_1, info_2)

        point = movie_div.select_one('.bd .rating_num').get_text(strip=True)
        print(str(datetime.now()) + ': ' + point)

        num_of_comment = movie_div.select_one('.bd .star span:last-child').get_text(strip=True)
        print(str(datetime.now()) + ': ' + num_of_comment)
        num_of_comment = re.match(r'\d+', num_of_comment).group()
        print(str(datetime.now()) + ': ' + num_of_comment)

        short_comment = ''
        try:
            short_comment = movie_div.select_one('.bd .quote span').get_text(strip=True)
        except AttributeError:
            pass
        finally:
            print(str(datetime.now()) + ': ' + short_comment)

        return_list.append([title, info_1, info_2, point, num_of_comment, short_comment])

    print(str(datetime.now()) + ': ' + '使用BeautifulSoup解析成功。')
    return return_list


def spider_by_beautifulsoup_find(html):
    pass
