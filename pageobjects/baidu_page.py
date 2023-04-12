# coding=utf-8
# @Author: yutian
# @Version: Python 3.7
# @File: baidu_page.py
# @Date: 2023/4/12 16:19
# @SoftWare: PyCharm
from selenium import webdriver

from config.driver_check_tool import check_chrome_driver_version
from framework.basepage import BasePage


class BaiduPage(BasePage):

    def __init__(self):
        check_chrome_driver_version()
        super(BaiduPage, self).__init__(webdriver.Chrome())

    def baidu_search(self):
        self.implicitly_wait(5)
        self.open('https://www.baidu.com')
        self.send_keys(self.get_element('id', value='kw'), 'python')
        self.click_element(self.get_element('id', value='su'))
