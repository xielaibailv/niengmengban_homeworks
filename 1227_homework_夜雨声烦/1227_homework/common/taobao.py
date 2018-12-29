#！/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     :2018/12/25 23:24
# @Author   :Yosef
# E-mail    :wurz529@foxmail.com
# File      :taobao.py
# Software  :PyCharm Community Edition
from common.base import Base
class Taobao(Base):

    def count(self):
        res = self.login()
        while True:
            if res:
                price = input("请输入您的账单金额：")
                while True:
                    try:
                        price = int(price)
                        print("您的账单金额是{}元".format(price))
                        offer = self.pay_model()
                        if price - offer > 0:
                            print("您的最后金额是{}元".format(price-offer))
                        else:
                            print("您的最后金额是0元")
                        break
                    except:
                        price = input("输入不合法，请重新输入您的账单金额：")
                break
            else:
                res = self.login()



    def wechatpay(self):
        print("不支持微信支付")

    def pay_model(self):
        choice = input("请输入您想要的支付方式：1[支付宝支付]2[银联支付]3[微信支付]")
        while True:
            if choice == "1":
                self.alipay()
                offer = self.post_coupon()
                break
            elif choice == "2":
                self.UnionPay()
                offer = 0
                break
            elif choice == "3":
                self.wechatpay()
                choice = input("请输入您想要的支付方式：1[支付宝支付]2[银联支付]3[微信支付]")
            else:
                choice = input("请输入您想要的支付方式：1[支付宝支付]2[银联支付]3[微信支付]")
        return offer