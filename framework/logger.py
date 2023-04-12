# coding=utf-8
# @Author: yutian
# @Version: Python 3.7
# @File: logger.py
# @Date: 2023/3/31 15:54
# @SoftWare: PyCharm
import logging

import os.path
import time

import colorlog

# console 日志颜色
console_log_color = {
    'DEBUG': 'white',
    'INFO': 'green',
    'WARNING': 'yellow',
    'ERROR': 'red',
    'CRITICAL': 'bold_red',
}

cur_path = os.path.dirname(os.path.abspath(__file__))
base_dir = cur_path[:cur_path.find('Unittest_Selenium_api_test') + len('Unittest_Selenium_api_test')]


class Logger(object):
    def __init__(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)

        log_time = time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime())
        log_path = os.path.join(base_dir, 'logs')
        log_name = os.path.join(log_path, '{}.log'.format(log_time))
        # 输出到日志文件
        file_handler = logging.FileHandler(log_name)
        file_handler.setLevel(logging.INFO)
        file_formatter = logging.Formatter(self.file_fmt)
        file_handler.setFormatter(file_formatter)

        # 输出到控制台
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_formatter = colorlog.ColoredFormatter(self.console_fmt, log_colors=console_log_color)
        console_handler.setFormatter(console_formatter)

        if not self.logger.handlers:
            self.logger.addHandler(file_handler)
            self.logger.addHandler(console_handler)

        file_handler.close()
        console_handler.close()

    @property
    def file_fmt(self):
        return '[%(asctime)s] %(filename)s(%(funcName)s) -> line:%(lineno)d [%(levelname)s]: %(message)s'

    @property
    def console_fmt(self):
        return '%(log_color)s[%(asctime)s] %(filename)s(%(funcName)s) -> line:%(lineno)d [%(levelname)s]: %(message)s'

    def get_log(self):
        return self.logger


log = Logger().get_log()
