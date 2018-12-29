#！/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     :2018/12/27 21:59
# @Author   :Yosef
# E-mail    :wurz529@foxmail.com
# File      :run.py
# Software  :PyCharm Community Edition
import unittest
import HTMLTestRunnerNew
from test_case.test_JD import Test_JD_Pay
from test_case.test_JD_login import Test_JD_Login

suite = unittest.TestSuite()
loader = unittest.TestLoader()

suite.addTest(loader.loadTestsFromTestCase(Test_JD_Pay))
suite.addTest(loader.loadTestsFromTestCase(Test_JD_Login))

report_path = "test_report/京东测试报告.html"

with open(report_path,"wb+") as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file, verbosity=2, title="京东支付测试报告", description="这是描述细节", tester="夜雨声烦")
    runner.run(suite)