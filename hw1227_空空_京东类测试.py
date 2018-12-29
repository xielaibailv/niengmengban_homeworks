import unittest
from hw1224_空空_类的继承淘宝京东  import JingDong
import HTMLTestRunnerNew

class TestMethod(unittest.TestCase):
    def setUp(self):
        j = JingDong('京东', '自营', '刘强东')

    #登录失败
    def test_login_faild(self,j):
        login_result = j.login('HUAHUA', '123456')
        try:
            self.assertFalse(login_result)
        except Exception as e:
            print('断言失败，原因：%s' %e)
            raise e

    #使用支付宝进行支付，结果失败
    def test_payment_zhifubao(self,j):
        # login_result = j.login('huahua', '123456')
        # payment = j.mode_payment('2')
        j.count(1000,'2')


