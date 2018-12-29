#！/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     :2018/12/25 22:59
# @Author   :Yosef
# E-mail    :wurz529@foxmail.com
# File      :base.py
# Software  :PyCharm Community Edition
import random

class Base:

    def __init__(self,name,feature,model,boss):
        self.name = name
        self.feature = feature
        self.model = model
        self.boss = boss

    def login(self,username,password):
        # username=input("请输入用户名：")
        # password = input("请输入密码：")
        if username=="huahua" and password=="123456":
            print("{}登录成功".format(username))
            res = True
        else:
            print("{}登录失败,用户名或密码不正确".format(username))
            res = False
        return res

    def alipay(self):
        print("您选择支付宝支付")

    def wechatpay(self):
        print("您选择微信支付")

    def UnionPay(self):
        print("你选择银联支付")

    def post_coupon(self):
        res = random.randint(10,50)
        # print("您拿到了{}元额度的优惠券".format(res))
        return res