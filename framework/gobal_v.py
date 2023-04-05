# coding=utf-8
# @Author: yutian
# @Version: Python 3.7
# @File: gobal_v.py
# @Date: 2023/4/5 16:15
# @SoftWare: PyCharm

# 暂时不使用该模块

def _init():
    global _global_test
    _global_test = {'pass_tag': True}


def set_test_result(key, value):
    _global_test[key] = value


def get_test_result(key):
    return _global_test.get(key)


_init()
