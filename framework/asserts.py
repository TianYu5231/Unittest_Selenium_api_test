# coding=utf-8
# @Author: yutian
# @Version: Python 3.7
# @File: asserts.py
# @Date: 2023/4/5 11:17
# @SoftWare: PyCharm


from framework.logger import log


def assert_equal(arg1, arg2, msg=None):
    """
    断言 arg1，arg2 是否相等
    :param arg1: 参数1
    :param arg2: 参数2
    :param msg: 错误提示
    :return:
    """
    if arg1 == arg2:
        return True
    else:
        if msg:
            log.error('{} != {}, msg={}'.format(arg1, arg2, msg))
        else:
            log.error('{} != {}'.format(arg1, arg2))
        return False


def assert_in(arg1, arg2, msg=None):
    """
    断言arg2 是否包含 arg1
    :param arg1: 参数1
    :param arg2: 参数2
    :param msg: 错误提示
    :return:
    """
    if arg1 in arg2:
        return True
    else:
        if msg:
            log.error('{} not in {}, msg={}'.format(arg1, arg2, msg))
        else:
            log.error('{} not in {}'.format(arg1, arg2))


def assert_True(arg1, msg=None):
    """
    断言是否为True
    :param arg1:
    :param msg:
    :return:
    """
    if arg1 is True:
        return True
    else:
        if msg:
            log.error('{} is not True, msg={}'.format(arg1, msg))
        else:
            log.error('{} is not True'.format(arg1))


def assert_False(arg1, msg=None):
    """
    断言是否为False
    :param arg1: 参数1
    :param msg: 错误提示
    :return:
    """
    if arg1 is False:
        return True
    else:
        if msg:
            log.error('{} is not False, msg={}'.format(arg1, msg))
        else:
            log.error('{} is not False'.format(arg1))

