# coding=utf-8
# @Author: yutian
# @Version: Python 3.7
# @File: driver_check_tool.py
# @Date: 2023/3/31 10:38
# @SoftWare: PyCharm
import os.path
import re
import shutil
import time
import zipfile

import requests
from selenium import webdriver


def get_chrome_driver_list(current_chrome_version):
    """
    获取chrome driver 列表
    :return:
    """
    driver_res = requests.get('http://chromedriver.storage.googleapis.com/?delimiter=/&prefix=')
    common_version = '.'.join(current_chrome_version.split('.')[:3])
    pattern = re.compile(r'{}\.\d*'.format(common_version))
    driver_version_nums = re.findall(pattern, str(driver_res.content))
    print('可下载的driver 版本号：', driver_version_nums)
    return driver_version_nums


def unzip_file(src_file, dest_path):
    """
    解压zip文件
    :return:
    """
    if zipfile.is_zipfile(src_file):
        zipf = zipfile.ZipFile(src_file)
        try:
            zipf.extract(member='chromedriver', path=dest_path)
        except RuntimeError as e:
            print(e)
        finally:
            zipf.close()
    else:
        print('请检查zip文件是否正确!')


def copy_file(src_file, dest_path):
    """
    复制文件到指定文件夹
    :param src_file: 需要复制的文件
    :param dest_path: 目标文件路径
    :return:
    """
    if not os.path.isfile(src_file):
        print('{} 不存在'.format(src_file))
    else:
        fpath, fname = os.path.split(src_file)
        dest_driver_path = os.path.join(dest_path, fname)
        shutil.copyfile(src_file, dest_driver_path)
        print('copy {} -> {}'.format(src_file, dest_driver_path))


def check_chrome_driver_version():
    """
    检查当前 chrome driver 版本, 适用于mac
    :return:
    """
    chrome_driver_path = r'/usr/local/bin'
    download_path = r'/Users/yutian/Downloads'
    try:
        webdriver.Chrome()
        print('chrome driver 版本检查正常')
    except Exception as msg:
        res = re.search(r'Current browser version is (.*) with', str(msg))
        if res:
            current_chrome_version = res.group(1)
            print('当前浏览器版本号：', current_chrome_version)
            driver_version_nums = get_chrome_driver_list(current_chrome_version)
            driver_mac_zip_url = r'http://chromedriver.storage.googleapis.com/{}/chromedriver_mac64.zip'.format(
                driver_version_nums[-1])
            mac_zip_res = requests.get(driver_mac_zip_url)
            # download zipfile path
            download_zipfile_path = r'/Users/yutian/Downloads/chromedriver_{}.zip'.format(driver_version_nums[-1])
            with open(download_zipfile_path, 'wb') as dzo:
                dzo.write(mac_zip_res.content)
            time.sleep(3)
            # 解压zip文件
            unzip_file(download_zipfile_path, download_path)
            # 修改文件为unix
            os.system('chmod u+x {}/chromedriver'.format(download_path))
            if os.system('file {}/chromedriver'.format(download_path)) == 0:
                print('chromedriver 类型修改成功!')
                # 复制文件到 usr/local/bin
                copy_file(download_path + '/chromedriver', chrome_driver_path)

                print('chrome driver 版本更换成功！！！')
            else:
                print('chromedriver 类型修改失败，无法进行文件复制！')
        else:
            print('报错信息中未匹配到 浏览器版本！')


if __name__ == '__main__':
    check_chrome_driver_version()
