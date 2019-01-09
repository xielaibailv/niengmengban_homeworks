import HTMLTestRunnerNew   # 导入HTML测试报告模块，生成HTML格式的测试报告
import unittest
from hw1227_空空_京东类测试.test_jd.test_jd import TestMethod


# suite:集合套件,专门存储加载测试用例
suite = unittest.TestSuite()   # 创建一个对象
# 获取测试数据
loader = unittest.TestLoader()
# 从测试模块里加载测试用例
suite.addTest(loader.loadTestsFromTestCase(TestMethod))
# 生成HTML格式的测试报告
with open('../test_report/test_report.html', 'wb') as file :
    runner = HTMLTestRunnerNew.HTMLTestRunner(file, 2, title='京东电商的测试报告', description='第一次单元测试', tester='空空')
    runner.run(suite)
