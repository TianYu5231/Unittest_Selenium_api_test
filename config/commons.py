# coding=utf-8
# @Author: yutian
# @Version: Python 3.7
# @File: commons.py
# @Date: 2023/4/4 16:32
# @SoftWare: PyCharm
import os.path
import time

from config.HTMLTestRunner import HTMLTestRunner
from framework.logger import Logger

logger = Logger('common').get_log()
current_path = os.path.dirname(os.getcwd())


class Common(object):

    def get_html_report(self, suit, title):
        """
        生成html报告
        :param suit: 测试用例套
        :param title:  报告title
        :return:
        """
        r_path = os.path.join(current_path, 'reports')
        r_file = os.path.join(r_path, '{}.html'.format(time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime())))
        with open(r_file, 'wb+', encoding='utf-8') as f:
            runner = HTMLTestRunner(stream=f, title=title)
            runner.run(suit)
        logger.info(f'生成测试报告：{os.path.split(r_file)[-1]}')
