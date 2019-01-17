from hw0104_空空_配置and日志.classfile.math_method import MathMethod
from hw0104_空空_配置and日志.test_case.do_excel import DoExcel
from hw0104_空空_配置and日志.config_file.read_case import ReadCase
from hw0104_空空_配置and日志.test_case.log import MyLog
import unittest
from ddt import ddt, data

# 获取配置文件里的执行用例数量
file = '../config_file/case.ini'
button =(ReadCase(file).get_value('CASE','button'))

# 从两个sheet里读取值，分别传给下面的两个测试方法
add = DoExcel('测试数学类的数据.xlsx', 'data_add',button)
sub = DoExcel('测试数学类的数据.xlsx', 'data_sub',button)
add_cases = add.read_data()
sub_cases = sub.read_data()

# 创建日志
my_logger = MyLog()


@ddt  # 装饰测试类
class TestMathMethod(unittest.TestCase):  # TestCase是unittest里专门写用例的地方
    """测试数学类的测试用例类"""
    def setUp(self):
        my_logger.info('-------开始执行用例-------')

    def tearDown(self):
        my_logger.info('-------用例执行结束-------')

    # 测试加法
    @data(*add_cases)   # 有几条用例就执行几遍，*起到脱外套的作用,装饰测试方法
    def test_add(self, case):
        my_logger.info('开始执行第{}条用例:{}'.format(case.id, case.title))
        result = MathMethod(case.a, case.b).add()
        my_logger.info('{} + {} = {}' .format(case.a, case.b, result))
        try:
            self.assertEqual(case.expected, result)  # 判断期望值和实际值是否相等
            test_result = 'Pass'
        except AssertionError as e:
            test_result = 'Failed'
            msg = '测试失败，失败原因：{}'.format(e)
            my_logger.error(msg)
            print(msg)
            raise e
        finally:
            add.write_data(row=case.id + 1, column= 6, value=result)
            add.write_data(row=case.id + 1, column=7, value=test_result)

    # 测试减法
    @data(*sub_cases)
    def test_sub(self, case):
        my_logger.info('开始执行第{}条用例:{}'.format(case.id, case.title))
        result = MathMethod(case.a, case.b).sub()
        my_logger.info('{} - {} = {}'.format(case.a, case.b, result))
        try:
            self.assertEqual(case.expected, result)  # 判断期望值和实际值是否相等
            test_result = 'Pass'
        except AssertionError as e:
            test_result = 'Failed'
            msg = '测试失败，失败原因：{}'.format(e)
            my_logger.error(msg)
            print(msg)
            raise e
        finally:
            sub.write_data(row=case.id + 1, column= 6, value=result)
            sub.write_data(row=case.id + 1, column=7, value=test_result)


if __name__ == '__main__':
    unittest.main()


