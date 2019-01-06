#！/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     :2018/12/29 21:34
# @Author   :Yosef
# E-mail    :wurz529@foxmail.com
# File      :run.py
# Software  :PyCharm Community Edition
import unittest
import HTMLTestRunnerNew
from test_case.test_math_method import TestMathMethod
from common.do_excel import DoExcel

testdata = DoExcel("conf/test_data.xlsx","add_test_data").read_data() # 取出来的是字典
total_row = len(testdata)
print(total_row)
suite = unittest.TestSuite()
for i in range(0,total_row):
    a = testdata[i]["a"]
    b = testdata[i]["b"]
    expected = testdata[i]["expected result"]

    actual = a + b
    if i == 0:
        DoExcel("conf/test_data.xlsx", "add_test_data").write_data(1 , 4, "actual result")
    else:
        DoExcel("conf/test_data.xlsx", "add_test_data").write_data(i+2 , 4, actual)

    suite.addTest(TestMathMethod(a,b,expected,"test_add"))

report_path = "test_report/元旦作业.html"

with open(report_path,"wb+") as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file, verbosity=2,title="测试报告",description="这是描述细节",
                                              tester="夜雨声烦")
    runner.run(suite)

