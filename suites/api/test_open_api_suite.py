# coding=utf-8
# @Author: yutian
# @Version: Python 3.7
# @File: test_open_api_suite.py
# @Date: 2023/4/5 10:25
# @SoftWare: PyCharm
import sys
sys.path.append('../..')
import unittest

from config import commons
from test_cases.test_api.test_openapi import TestOpenApi


suite = unittest.TestSuite(unittest.TestLoader().loadTestsFromTestCase(TestOpenApi))
commons.get_html_report(suite, title='OpenApi 测试报告')
