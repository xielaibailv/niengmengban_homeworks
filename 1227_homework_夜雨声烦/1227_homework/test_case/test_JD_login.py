#!usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2018/12/28 14:45
# @Author   : Yosef-夜雨声烦
# @Email    : wurz529@foxmail.com
# @File     : test_JD_login.py
# @Software : PyCharm Community Edition
import unittest
from common.jindong import Jindong

JD = Jindong("","","","")

class Test_JD_Login(unittest.TestCase):

    def setUp(self):
        print("********测试开始*********")

    def tearDown(self):
        print("********测试结束*********")

    def test_correct_login(self):
        res = JD.login("huahua","123456")
        try:
            self.assertTrue(res)
            print("登录成功！")
        except Exception as e:
            print("登录失败！")
            print("报错信息是{}".format(e))
            raise e


    def test_empty_login(self):
        res = JD.login(" ", " ")
        try:
            self.assertTrue(res)
            print("登录成功！")
        except Exception as e:
            print("登录失败！")
            print("报错信息是{}".format(e))
            raise e

    def test_wrong_login(self):
        res = JD.login("huahua", "1234")
        try:
            self.assertTrue(res)
            print("登录成功！")
        except Exception as e:
            print("登录失败！")
            print("报错信息是{}".format(e))
            raise e

if __name__ == '__main__':
    unittest.main()