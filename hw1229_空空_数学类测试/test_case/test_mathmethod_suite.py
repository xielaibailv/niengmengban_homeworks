from hw1229_空空_数学类测试.test_case.do_excel import DoExcel    # 导入doexcel模块，获取测试数据
from hw1229_空空_数学类测试.test_case.do_excel import Cases
from hw1229_空空_数学类测试.test_case.test_math_method import TestMathMethod   # 导入测试用例的模块，获取测试用例
import HTMLTestRunnerNew   # 导入HTML测试报告模块，生成HTML格式的测试报告
import unittest


suite = unittest.TestSuite()
# 测试加法
# 利用字典用例，获取测试数据
# test_data = DoExcel('测试数学类的数据.xlsx', 'data_add').read_data()  # 获取到的是列表嵌套的字典
# for item in test_data:
#     suite.addTest(TestMathMethod.test_add(item['a'], item['b'], item['excepted'], 'test_add'))

# 利用类与对象，获取测试数据
cases = DoExcel('测试数学类的数据.xlsx', 'data_add').read_data()  # 获取到的是列表嵌套的字典
for case in cases:
    suite.addTest(TestMathMethod.test_add(case.a, case.b, case.excepted, 'test_add'))








# 生成HTML格式的测试报告
with open('test_report.html', 'wb') as file :
    runner = HTMLTestRunnerNew.HTMLTestRunner(file, 2, title='数学类的测试报告', description='第一次单元测试', tester='空空')
    runner.run(suite)
