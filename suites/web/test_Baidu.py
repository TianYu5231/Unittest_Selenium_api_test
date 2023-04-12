# coding=utf-8
# @Author: yutian
# @Version: Python 3.7
# @File: test_Baidu.py
# @Date: 2023/4/12 17:11
# @SoftWare: PyCharm
import unittest

from config import commons
from test_cases.test_web.test_baidu_search import TestBaiduSearch

suite = unittest.TestSuite(unittest.TestLoader().loadTestsFromTestCase(TestBaiduSearch))
commons.get_html_report(suite, title='baidu_selenium')
