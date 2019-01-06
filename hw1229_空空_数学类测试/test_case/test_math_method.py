from hw1229_空空_数学类测试.classfile.math_method import MathMethod
from hw1229_空空_数学类测试.test_case.do_excel import DoExcel
import HTMLTestRunnerNew
import unittest
from ddt import ddt, data


cases = DoExcel('测试数学类的数据.xlsx', 'data_add').read_data()


@ddt  # 装饰测试类
class TestMathMethod(unittest.TestCase):  # TestCase是unittest里专门写用例的地方
    """测试数学类的测试用例类"""
    def setUp(self):
        print('开始执行用例')

    # def tearDown(self):
    #     print('用例执行结束')

    # 测试加法
    @data(*cases)   # 有几条用例就执行几遍，*起到脱外套的作用,装饰测试方法
    def test_add(self, case):
        print(case)
        result = MathMethod(case.a, case.b).add()
        print(result)
        try:
            self.assertEqual(self, case.excepted, result)  # 判断期望值和实际值是否相等
            test_result = 'Pass'
        except Exception as e:
            test_result = 'Failed'
            print('测试失败，失败原因：{}'.format(e))
            raise e
        finally:
            print('a + b 的值 = {}'.format(result))
            DoExcel('测试数学类的数据.xlsx', 'data_add').write_data(row=case.id + 1, column= 6, value=result)
            DoExcel('测试数学类的数据.xlsx', 'data_add').write_data(row=case.id + 1, column=7, value=test_result)
        return result

    # 测试减法
    # def test_sub(self, a, b, excepted):
    #     result = MathMethod(a, b).sub()
    #     try:
    #         self.assertEqual(excepted, result)  # 判断期望值和实际值是否相等
    #         test_result = 'Pass'
    #     except Exception as e:
    #         test_result = 'Failed'
    #         print('测试失败，失败原因：{}'.format(e))
    #         raise e
    #     finally:
    #         print('a - b 的值 = {}'.format(result))
    #     return result


if __name__ == '__main__':
    TestMathMethod().test_add()
    # t = TestMathMethod()
    # t.test_add(a=0, b=0, excepted=0)
    # TestMathMethod().test_add(a=1, b=2, excepted=3)
    # TestMathMethod().test_add(0,0,0)
    # TestMathMethod().test_sub(a=0, b=0, excepted=0)
    # TestMathMethod.test_add(a=1, b=2, excepted=3)


