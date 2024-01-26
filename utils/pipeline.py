#!/usr/bin/python
# -*- coding:utf-8 -*-


import pandas
from datetime import datetime


def save_into_csv(data_list):
    data_df = (pandas.DataFrame(data_list))
    file_name = './data/data_{}.csv'.format(datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))
    data_df.to_csv(file_name, index=False, header=['电影名', '人员信息', '电影信息', '得分', '评论数', '短评'], encoding='utf-8')
    print(str(datetime.now()) + ': ' + '数据成功保存至{}中。'.format(file_name))
