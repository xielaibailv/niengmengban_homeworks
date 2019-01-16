from hw0102_空空_ddt和配置.test_ddt import TestMethod
import unittest
import HTMLTestRunnerNew


# suite
suite = unittest.TestSuite()
# 加载 loader
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(TestMethod))
#
# with open('test_result.txt','w') as f :
#     runner = unittest.TextTestRunner(stream = f, descriptions = True, verbosity = 2)
#     runner.run(suite)

runner = unittest.TextTestRunner(descriptions = True, verbosity = 2)
runner.run(suite)