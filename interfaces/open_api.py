# coding=utf-8
# @Author: yutian
# @Version: Python 3.7
# @File: open_api.py
# @Date: 2023/4/4 16:52
# @SoftWare: PyCharm
from framework.request import request_get, request_post


class OpenApi(object):

    def __init__(self):
        self.do_main = 'https://api.apiopen.top/api'

    def get_images(self, i_type, page=0, size=10):
        """
        获取图片
        :param i_type: 图片类型：animal, beauty, car, comic, food, game, movie, person, phone, scenery
        :param page: 默认0
        :param size: 默认10
        :return:
        """
        url = self.do_main + '/getImages'
        result = request_get(url=url, params={'type': i_type, 'page': page, 'size': size})
        return result

    def get_video(self, page=0, size=10):
        """
        获取短视频
        :param page: 默认0
        :param size: 默认10
        :return:
        """
        url = self.do_main + '/getHaoKanVideo'
        result = request_get(url=url, params={'page': page, 'size': size})
        return result

    def get_sentences(self):
        """
        获取一言名句
        :return:
        """
        url = self.do_main + '/sentences'
        result = request_get(url=url)
        return result

    def login(self, account, password):
        """
        登录接口
        :param account: 账户名
        :param password: 密码
        :return:
        """
        url = self.do_main + '/login'
        result = request_get(url=url, json={'account': account, 'password': password})
        return result

    def register(self, account, password, code):
        """
        注册账号
        :param account: 账号
        :param password: 密码
        :param code: 邮箱验证码
        :return:
        """
        url = self.do_main + '/register'
        result = request_post(url=url, json={'account': account, 'code': code, 'password': password})
        return result


if __name__ == '__main__':
    oa = OpenApi()
    print(oa.get_images('movie').json())
