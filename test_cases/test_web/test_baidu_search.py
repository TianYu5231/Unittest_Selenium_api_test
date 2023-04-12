# coding=utf-8
# @Author: yutian
# @Version: Python 3.7
# @File: test_baidu_search.py
# @Date: 2023/4/12 17:08
# @SoftWare: PyCharm
import unittest

from framework.asserts import assert_equal
from framework.logger import log
from pageobjects.baidu_page import BaiduPage


class TestBaiduSearch(unittest.TestCase):

    def setUp(self) -> None:
        self.baidu = BaiduPage()

    def tearDown(self) -> None:
        self.baidu.quit()

    def test_baidu_search(self):
        self.baidu.baidu_search()
        assert_equal(self.baidu.driver.title, 'python_百度搜索')
