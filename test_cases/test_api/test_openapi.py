# coding=utf-8
# @Author: yutian
# @Version: Python 3.7
# @File: test_openapi.py
# @Date: 2023/4/5 09:18
# @SoftWare: PyCharm
import unittest

from interfaces.open_api import OpenApi
from framework.asserts import *


class TestOpenApi(unittest.TestCase):

    @unittest.skip
    def test_get_images_type(self):
        """
        校验type是否正确
        :return:
        """
        for i_type in ['animal', 'beauty', 'car', 'comic', 'food', 'game', 'movie', 'person', 'phone', 'scenery']:
            result = OpenApi().get_images(i_type)
            assert result.status_code == 200, log.error(f'{result.status_code} != 200')
            json_res = result.json()
            assert json_res['message'] == '成功!', log.error(f"{json_res['message']} != '成功!'")
            image_list = json_res['result']['list']
            for img in image_list:
                assert img['type'] == i_type, log.error(f"{img['type']} != {i_type}")

    def test_get_images_page(self):
        """
        校验page是否可小于0
        :return:
        """
        result = OpenApi().get_images(i_type='animal', page=-1, size=10)
        json_result = result.json()
        assert result.status_code == 200, log.error(f'{result.status_code} != 200')
        assert json_result['code'], log.error(f"{json_result['code']} != 400")
        assert json_result['message'] == 'page必须大于或等于0', log.error(f"{json_result['message']} != 'page必须大于或等于0'")

    @unittest.skip
    def test_get_images_size(self):
        """
        校验size是否可小于1，以及size返回数量
        :return:
        """
        result = OpenApi().get_images(i_type='animal', page=0, size=-1)
        json_result = result.json()
        assert result.status_code == 200, log.error(f'{result.status_code} != 200')
        assert json_result['code'] == 400, log.error(f"{json_result['code']} != 400")
        assert json_result['message'] == 'size必须大于或等于1', log.error(f"{json_result['message']} != 'size必须大于或等于1'")

        s_res = OpenApi().get_images(i_type='animal', page=0, size=20)
        j_result = s_res.json()
        assert result.status_code == 200, log.error(f'{result.status_code} != 200')
        assert len(j_result['result']['list']) == 20, log.error(f"{len(j_result['result']['list'])} != 200")

