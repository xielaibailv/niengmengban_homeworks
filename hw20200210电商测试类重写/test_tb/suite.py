import HTMLTestRunnerNew
import unittest
from hw20200210电商测试类重写.test_tb.test_tb import TestMethod

suite = unittest.TestSuite()
loader = unittest.TestLoader()

suite.addTest(loader.loadTestsFromTestCase(TestMethod))

with open('../test_report/TestReport.html','wb') as f:
    runner = HTMLTestRunnerNew.HTMLTestRunner(f,2,title='电商测试报告',description='20200225',tester='yoyo')
    runner.run(suite)

