import unittest
from hw1227_空空_京东类测试.p2p_jingdng.p2p_jd import JingDong


class TestMethod(unittest.TestCase):

    # 登录失败
    def test_login_faild(self):
        login_result = JingDong('京东', '自营', '刘强东').login_jd('HUAHUA', '123456')
        try:
            self.assertFalse(login_result)
            print("登录失败 !")
        except Exception as e:
            print('断言失败，原因：%s' %e)
            raise e

    # 登录成功
    def test_login_pass(self):
        login_result = JingDong('京东', '自营', '刘强东').login_jd('huahua', '123456')
        try:
            self.assertTrue(login_result)
            print("登录成功 !")
        except Exception as e:
            print('断言失败，原因：%s' % e)
            raise e

    # 使用支付宝进行支付，结果失败
    def test_payment_zhifubao(self):
        result = JingDong().count(500,'2')
        try:
            self.assertFalse(result)
        except Exception as e:
            print('断言失败，原因：%s' % e)
            raise e


