#！/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     :2018/12/27 21:44
# @Author   :Yosef
# E-mail    :wurz529@foxmail.com
# File      :test_JD.py
# Software  :PyCharm Community Edition
import unittest
from common.jindong import Jindong

class Test_JD_Pay(unittest.TestCase):

    def setUp(self):
        print("********测试开始*********")

    def tearDown(self):
        print("********测试结束*********")

    """
    支付宝支付ok?
    """
    def test_alipay(self):
        isOK = Jindong("","","","").pay_model("1")[1]
        print(isOK)
        try:
            self.assertTrue(isOK)
            print("京东可以使用支付宝")
        except Exception as e:
            print("京东不可以使用支付宝")
            print("错误信息是{}".format(e))
            raise e

    """
    银联支付ok?
    """
    def test_unionpay(self):
        isOK = Jindong("","","","").pay_model("2")[1]
        try:
            self.assertTrue(isOK)
            print("京东可以使用银联")
        except Exception as e:
            print("京东不可以使用银联")
            print("错误信息是{}".format(e))
            raise e

    """
    微信支付ok?
    """
    def test_wechatpay(self):
        isOK = Jindong("","","","").pay_model("3")[1]
        try:
            self.assertTrue(isOK)
            print("京东可以使用微信支付")
        except Exception as e:
            print("京东不可以使用微信支付")
            print("错误信息是{}".format(e))
            raise e

    """
    银联支付有offer？
    """
    def test_offer(self):
        offer = Jindong("", "", "", "").pay_model("2")[0]
        try:
            # print(offer)
            self.assertIsNot(offer,0)
            print("银联支付有优惠券哟")
        except Exception as e:
            print("银联支付没有优惠券")
            print("错误信息是{}".format(e))
            raise e



if __name__ == '__main__':
    unittest.main()