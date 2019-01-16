from hw0104_空空_配置and日志.test_case.test_math_method import TestMathMethod  # 导入测试用例的模块，获取测试用例
import HTMLTestRunnerNew  # 导入HTML测试报告模块，生成HTML格式的测试报告
import unittest

# suite:集合套件,专门存储加载测试用例
suite = unittest.TestSuite()  # 创建一个对象
# 加载 loader
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(TestMathMethod))

report_path = '../test_result/test_report.html'
# 生成HTML格式的测试报告
with open(report_path, 'wb') as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file,
                                              verbosity=2,
                                              title='数学类的测试报告',
                                              description='第一次单元测试',
                                              tester='空空')
    runner.run(suite)  # 执行用例
