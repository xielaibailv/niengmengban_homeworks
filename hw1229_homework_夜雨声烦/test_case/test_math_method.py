#！/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     :2018/12/29 21:43
# @Author   :Yosef
# E-mail    :wurz529@foxmail.com
# File      :test_math_method.py
# Software  :PyCharm Community Edition
import unittest
import openpyxl
from hw1229_homework_夜雨声烦.common.math_method import MathMethod

class TestMathMethod(unittest.TestCase):
    def __init__(self,a,b,expected,MethodName):
        super(TestMathMethod, self).__init__(MethodName)
        self.a = a
        self.b = b
        self.expected = expected


    def setUp(self):
        print("********测试开始*********")

    def tearDown(self):
        print("********测试结束*********")

    def test_add(self):
        act = MathMethod(self.a,self.b).add()
        expected = self.expected
        try:
            self.assertEqual(act,expected)
            print("{}+{} Test pass!!".format(self.a, self.b))
        except Exception as e:
            print("Sorry, test failed!!异常信息是{}".format(e))
            raise e

    def test_sub(self):
        res = MathMethod(self.a, self.b).sub()
        expected = self.expected
        try:
            self.assertEqual(res, expected)
            print("{}-{} Test pass!!".format(self.a,self.b))
        except Exception as e:
            print("Sorry, test failed!!异常信息是{}".format(e))
            raise e


