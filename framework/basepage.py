# coding=utf-8
# @Author: yutian
# @Version: Python 3.7
# @File: basepage.py
# @Date: 2023/3/31 17:00
# @SoftWare: PyCharm
import os.path

from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from config import commons
from framework.logger import log

base_dir = commons.get_base_dir()


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        """
        访问url
        :param url:
        :return:
        """
        log.info('访问 url: {}'.format(url))
        self.driver.get(url)

    def close(self):
        """
        关闭页面
        :return:
        """
        log.info('关闭页面')
        self.driver.close()

    def quit(self):
        """
        退出浏览器
        :return:
        """
        log.info('退出浏览器')
        self.driver.quit()

    def forward(self):
        """
        浏览器前进操作
        :return:
        """
        self.driver.forward()
        log.info('浏览器前进操作')

    def back(self):
        """
        浏览器后退操作
        :return:
        """
        log.info('浏览器后退操作')
        self.driver.back()

    def implicitly_wait(self, seconds):
        """
        隐形等待
        :param seconds: 秒
        :return:
        """
        log.info('隐形等待 {} 秒'.format(seconds))
        self.driver.implicitly_wait(seconds)

    def web_driver_wait(self, ele, seconds):
        """
        显性等待元素是否可见
        :param ele: 元素
        :param seconds: 秒
        :return:
        """
        log.info('等待元素{}可见'.format(ele))
        try:
            WebDriverWait(self.driver, seconds).until(EC.visibility_of_element_located(ele))
            log.info('wait for {} seconds'.format(seconds))
        except NameError as e:
            log.error('Failed to load the element with {}'.format(e))

    def get_element(self, local_method='', value=''):
        """
        查找元素
        :param local_method: 定位类型
        :param value: 定位类型值
        :return:
        """
        log.info('查找元素: {}'.format(value))
        try:
            by = self.check_local_method(local_method)
            return self.driver.find_element(by=by, value=value)
        except Exception as e:
            log.error('查找元素{}失败: {}'.format(value, e))
            self.save_screentshot()

    def get_elements(self, local_method='', value=''):
        """
        查找多个元素
        :param local_method: 定位类型
        :param value: 定位类型值
        :return: list
        """
        log.info('查找元素: {}'.format(value))
        try:
            by = self.check_local_method(local_method)
            return self.driver.find_elements(by=by, value=value)
        except Exception as e:
            log.error('查找元素{}失败: {}'.format(value, e))
            self.save_screentshot()

    def click_element(self, ele):
        """
        点击元素
        :param ele: 被点击的元素
        :return:
        """
        log.info('点击元素: {}'.format(ele))
        try:
            ele.click()
        except Exception as e:
            log.error('元素{}点击失败: {}'.format(ele, e))
            self.save_screentshot()

    def switch_window(self, handle):
        """
        切换到指定窗口
        :param handle: 指定窗口句柄
        :return:
        """
        log.info('切换窗口')
        try:
            self.driver.switch_to.window(handle)
        except Exception as e:
            log.error('窗口切换失败: {}'.format(e))

    def switch_current_window(self):
        """
        切换到当前窗口
        :return:
        """
        log.info('切换到当前窗口')
        current_handle = self.driver.current_window_handle
        self.switch_window(current_handle)

    def send_keys(self, ele, data):
        """
        输入文本
        :param ele: 元素
        :param data: 文本内容
        :return:
        """
        log.info('输入文本')
        ele.send_keys(data)

    def clear_input_text(self, ele):
        """
        清空文本
        :param ele: 元素
        :return:
        """
        log.info('清空文本')
        ele.send_keys(Keys.CANCEL + 'a')
        ele.send_keys(Keys.DELETE)

    def switch_frame(self, data):
        """
        切换frame
        :param data:
        :return:
        """
        log.info('切换frame')
        self.driver.switch_to.frame(data)

    def move_to_element(self, ele):
        """
        鼠标悬浮
        :param ele:
        :return:
        """
        log.info('鼠标悬浮')
        action = ActionChains(self.driver)
        action.move_to_element(ele).perform()

    def save_screentshot(self):
        """
        保存页面截图
        :return:
        """
        log.info('保存截图')
        screen_path = os.path.join(base_dir, 'screenshots')
        screen_file = screen_path + self.driver.title + '.png'
        try:
            self.driver.save_screentshot(screen_file)
        except Exception as e:
            log.error('截图保存失败: {}'.format(e))

    def check_local_method(self, method):
        """
        判断定位方法
        :param method:
        :return:
        """
        if method == 'id':
            return By.ID
        elif method == 'name':
            return By.NAME
        elif method == 'class_name':
            return By.CLASS_NAME
        elif method == 'link_text':
            return By.LINK_TEXT
        elif method == 'partial_link_text':
            return By.PARTIAL_LINK_TEXT
        elif method == 'xpath':
            return By.XPATH
        elif method == 'css_selector':
            return By.CSS_SELECTOR
        else:
            log.error('定位方法不存在.')
            return False

