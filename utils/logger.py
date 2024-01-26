#!/usr/bin/python
# -*- coding:utf-8 -*-


import sys


# supper: None
# TODO: 创建用于存储日志的类，便于将输出重定向到日志文件方便查询
class Logger(object):

    # input: String
    # output: None
    # TODO: 定义初始化类的方法
    def __init__(self, filename='Default.log'):
        self.terminal = sys.stdout
        self.log = open(filename, mode='a', encoding='utf-8')

    # input: String
    # output: None
    # TODO: 定义同时输出在控制台和文件的方法
    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    # input: None
    # output: None
    # TODO: Logger关闭时自动调用，关闭文件流
    def flush(self):
        # self.log.close()
        pass

# sys.stdout = Logger('douban_log.txt')
