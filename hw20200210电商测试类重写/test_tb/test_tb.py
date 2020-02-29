import unittest
from  hw20200210电商测试类重写.p2p_taobao.e_business_taobao_for_test import TaoBao


class TestMethod(unittest.TestCase):

    def test_login_success(self):
        login_result = TaoBao("淘宝").login("admin", "123456")
        try:
            self.assertTrue(login_result)
        except Exception as e:
            print("断言失败：%s" %e)
            raise e

    def test_login_failed(self):
        login_result = TaoBao("淘宝").login("admin", "123")
        try:
            self.assertFalse(login_result)
        except Exception as e:
            print("断言失败：%s" % e)
            raise e

    # 使用微信支付
    def test_count_wechat_pay(self):
        login_result = TaoBao("淘宝").login("admin", "123456")
        count_result = TaoBao("淘宝").count(login_result, 500, 1)
        try:
            self.assertFalse(count_result)
        except Exception as e:
            print("断言失败：%s" % e)
            raise e

    # 使用支付宝支付
    def test_count_ali_pay(self):
        login_result = TaoBao("淘宝").login("admin", "123456")
        count_result = TaoBao("淘宝").count(login_result, 500, 2)
        try:
            self.assertTrue(count_result)
        except Exception as e:
            print("断言失败：%s" % e)
            raise e

    # 使用银联支付
    def test_count_bank_pay(self):
        login_result = TaoBao("淘宝").login("admin", "123456")
        count_result = TaoBao("淘宝").count(login_result, 500, 3)
        pay_amount = 500
        try:
            self.assertEqual(pay_amount, count_result)
        except Exception as e:
            print("断言失败：%s" % e)
            raise e







