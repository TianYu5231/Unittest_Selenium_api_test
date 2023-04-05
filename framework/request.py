# coding=utf-8
# @Author: yutian
# @Version: Python 3.7
# @File: request.py
# @Date: 2023/4/5 09:48
# @SoftWare: PyCharm
import requests

from framework.logger import log


def request_get(url, params=None, **kwargs):
    """
    封装 get 请求
    :param url:
    :param params:
    :param kwargs:
    :return:
    """
    result = requests.get(url=url, params=params, **kwargs)
    log.info('GET 请求接口: {}'.format(result.url))
    log.info('返回结果: {}'.format(result.json()))
    return result


def request_post(url, data=None, json=None, **kwargs):
    """
    封装 post 请求
    :param url:
    :param data:
    :param json:
    :param kwargs:
    :return:
    """
    result = requests.post(url, data=data, json=json, **kwargs)
    log.info('POST 请求接口: {}'.format(result.url))
    log.info('返回结果: {}'.format(result.json()))
    return result


def request_put(url, data=None, **kwargs):
    """
    封装 put 请求
    :param url:
    :param data:
    :param kwargs:
    :return:
    """
    result = requests.post(url, data=data, **kwargs)
    log.info('PUT 请求接口: {}'.format(result.url))
    log.info('返回结果: {}'.format(result.json()))
    return result


def request_patch(url, data=None, **kwargs):
    """
    封装 patch 请求
    :param url:
    :param data:
    :param kwargs:
    :return:
    """
    result = requests.post(url, data=data, **kwargs)
    log.info('PATCH 请求接口: {}'.format(result.url))
    log.info('返回结果: {}'.format(result.json()))
    return result
