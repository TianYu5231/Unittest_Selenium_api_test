# coding=utf-8
# @Author: yutian
# @Version: Python 3.7
# @File: basepage.py
# @Date: 2023/3/31 17:00
# @SoftWare: PyCharm
from selenium.webdriver.support.wait import WebDriverWait

from framework.logger import Logger

logger = Logger(logger='BasePage').get_log()

class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def quit(self):
        self.driver.quit()

    def forward(self):
        """
        浏览器前进操作
        :return:
        """
        self.driver.forward()
        logger.info('浏览器前进操作')

    def back(self):
        """
        浏览器后退操作
        :return:
        """
        self.driver.back()
        logger.info('浏览器后退操作')

    def wait(self, loc, seconds):
        try:
            WebDriverWait(self.driver, seconds).until(lambda driver:driver.find_element(*loc))
            logger.info('wait for {} seconds'.format(seconds))
        except NameError as e:
            logger.error('Failed to load the element with {}'.format(e))
