#!/usr/bin/python
# -*- coding:utf-8 -*-


import re
from lxml import etree
from bs4 import BeautifulSoup
from datetime import datetime


# input: String
# output: List
# TODO: 用lxml中etree的xpath解析并获取HTML中的数据
def spider_by_lxml(html):
    tree = etree.HTML(html)
    return_list = []

    for movie_div in tree.xpath('//div[@id="content"]//div[@class="info"]'):
        title = movie_div.xpath('div[@class="hd"]/a/span/text()')
        print(str(datetime.now()) + ': ' + str(title))
        title = re.sub(r'\s{2,}', ' ', ''.join(title))
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


# input: String
# output: List
# TODO: 用BeautifulSoup中的find系列解析并获取HTML中的数据
def spider_by_beautifulsoup_find(html):
    html = re.sub(r'<br\s*/*>', '', html)
    soup = BeautifulSoup(html, 'html.parser')
    return_list = []

    for movie_div in soup.find_all('div', class_='info'):
        title = movie_div.find('div', class_='hd').a.find_all('span')
        title = ''.join([x.get_text() for x in title])
        title = re.sub(r'\s{2,}', ' ', title)
        # title = [re.sub(r'^\s+', '', x) for x in title]
        print(str(datetime.now()) + ': ' + title)

        info = movie_div.find('div', class_='bd').p.get_text(strip=True)
        info_1, info_2 = re.split(r'\s{8,}', info, 1)
        info_1 = re.sub(r'\s{2,}', ' ', info_1)
        info_1 = re.sub(r'^\s+', '', info_1)
        info_2 = re.sub(r'\s{2,}', ' ', info_2)
        info_2 = re.sub(r'^\s+', '', info_2)
        print(str(datetime.now()) + ': ' + info_1, info_2)

        point = movie_div.find('div', class_='bd').find('div', class_='star')
        point = point.find('span', class_='rating_num').get_text(strip=True)
        print(str(datetime.now()) + ': ' + point)

        num_of_comment = movie_div.find('div', class_='bd').find('div', class_='star')
        num_of_comment = num_of_comment.find('span', class_=False, string=re.compile(r'^\d.*?')).get_text(strip=True)
        print(str(datetime.now()) + ': ' + str(num_of_comment))
        num_of_comment = re.match(r'\d+', num_of_comment).group()
        print(str(datetime.now()) + ': ' + num_of_comment)

        short_comment = ''
        try:
            short_comment = movie_div.find('div', class_='bd').find('p', class_='quote').get_text(strip=True)
        except AttributeError:
            pass
        finally:
            print(str(datetime.now()) + ': ' + short_comment)

        return_list.append([title, info_1, info_2, point, num_of_comment, short_comment])

    print(str(datetime.now()) + ': ' + '使用BeautifulSoup的find系列方法解析成功。')
    return return_list


# input: String
# output: List
# TODO: 用BeautifulSoup中的select系列解析并获取HTML中的数据
def spider_by_beautifulsoup_select(html):
    soup = BeautifulSoup(html, 'html.parser')
    return_list = []

    for movie_div in soup.select('#content .info'):
        title = ''.join([x.get_text() for x in movie_div.select('.hd a span')])
        title = re.sub(r'\s{2,}', ' ', title)
        print(str(datetime.now()) + ': ' + title)

        info = movie_div.select_one('.bd p').get_text(strip=True, separator='\n')
        print(str(datetime.now()) + ': ' + info)
        info = re.sub(r'\s{2,}', ' ', info)
        info_1, info_2 = re.sub(r'^\s+', '', info).split('\n', 1)
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

    print(str(datetime.now()) + ': ' + '使用BeautifulSoup的select系列方法解析成功。')
    return return_list
