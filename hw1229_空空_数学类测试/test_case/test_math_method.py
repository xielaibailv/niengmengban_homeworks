from hw1229_空空_数学类测试.classfile.math_method import MathMethod
from hw1229_空空_数学类测试.test_case.do_excel import DoExcel
import unittest
from ddt import ddt, data

# 从两个sheet里读取值，分别传给下面的两个测试方法
add = DoExcel('测试数学类的数据.xlsx', 'data_add')
sub = DoExcel('测试数学类的数据.xlsx', 'data_sub')
add_cases = add.read_data()
sub_cases = sub.read_data()


@ddt  # 装饰测试类
class TestMathMethod(unittest.TestCase):  # TestCase是unittest里专门写用例的地方
    """测试数学类的测试用例类"""
    # def setUp(self):
        # 创建一个对象，将调用DoExcel类调用写在这里
        # 写在这里的话，每执行一次用例就要初始化一个对象，觉得不是很好，应该写在外面
        # self.add = DoExcel('测试数学类的数据.xlsx', 'data_add')
        # self.sub = DoExcel('测试数学类的数据.xlsx', 'data_sub')

    def tearDown(self):
        print('用例执行结束')

    # 测试加法
    @data(*add_cases)   # 有几条用例就执行几遍，*起到脱外套的作用,装饰测试方法
    def test_add(self, case):
        print('开始执行第{}条用例:{}'.format(case.id, case.title))
        result = MathMethod(case.a, case.b).add()
        try:
            self.assertEqual(case.expected, result)  # 判断期望值和实际值是否相等
            test_result = 'Pass'
        except Exception as e:
            test_result = 'Failed'
            print('测试失败，失败原因：{}'.format(e))
            raise e
        finally:
            print('a + b 的值 = {}'.format(result))
            add.write_data(row=case.id + 1, column= 6, value=result)
            add.write_data(row=case.id + 1, column=7, value=test_result)

    # 测试减法
    @data(*sub_cases)
    def test_sub(self, case):
        print('开始执行第{}条用例:{}'.format(case.id, case.title))
        result = MathMethod(case.a, case.b).sub()
        try:
            self.assertEqual(case.expected, result)  # 判断期望值和实际值是否相等
            test_result = 'Pass'
        except Exception as e:
            test_result = 'Failed'
            print('测试失败，失败原因：{}'.format(e))
            raise e
        finally:
            print('a - b 的值 = {}'.format(result))
            sub.write_data(row=case.id + 1, column= 6, value=result)
            sub.write_data(row=case.id + 1, column=7, value=test_result)


if __name__ == '__main__':
    unittest.main()


