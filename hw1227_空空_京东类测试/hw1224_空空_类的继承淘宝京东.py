# 父类：电商平台

# 平台名称 特征 feature 销售模式 创始人
# 功能：登录 支付方式 计算收银的功能

# 登录功能：
# 1. 用户名统一规定为 huahua 密码统一规定为 123456
# 2.如果输入用户名和密码正确 就提示登录成功，返回True(布尔值类型）
# 3.如果用户名和密码不匹配或者不正确，那么就显示登录失败，用户名或密码不正确，返回False(布尔值类型）

# 支付方式：
# 有3种 一种是微信支付 一种是支付宝支付 一种是银联支付

# 一个优惠的功能：随机发送不同额度金额的优惠金额（金额范围在10-50之间）


# 写2个子类：京东类 和 淘宝类

# 京东类 用户购买了东西 只能选择微信支付 银联支付 不支持支付宝支付


# 一个结算的功能：结算的时候根据用户选择 结算的时候根据用户输入用户信息以及金额以及支付方式作出如下的反馈
# 先判断用户是否登录成功 登录成功后提示用户名 然后用户输入金额
# 1）微信支付 就可以享受优惠
# 2）选择银联支付就不享受优惠
# 3） 选择支付宝提示不能支付，请重新选择支付


# 淘宝类 用户购买了东西 只能选择支付宝支付 银联支付 不支持微信支付

# 一个结算的功能：结算的时候根据用户输入的金额以及支付方式作出如下的反馈
# 先判断用户是否登录成功 登录成功后提示用户名 然后用户输入金额
# 1）支付宝支付 就可以享受优惠
# 2）选择银联支付就不享受优惠
# 3） 选择微信提示不能支付，请重新选择支付
import random


# #父类，电商平台
# class P2P:
#     def __init__(self,name,creater):
#         self.name = name  #平台名称
#         self.feature = 'p2p'  #平台特征
#         self.creater = creater  #平台创始人
#         self.username = 'huahua'
#         self.password = '123456'
#
#     #登录功能
#     def login(self):
#         username = input('请输入用户名：')
#         if username == self.username:
#             password = input('请输入密码：')
#             if password == self.password:
#                 print('登录成功！欢迎来到{}'.format(self.name))
#                 return True
#             else:
#                 print('密码错误！')
#                 return False
#         else:
#             print('用户名错误！')
#             return False
#
#     #支付方式选择
#     def mode_payment(self):
#         while True:
#             payment = input('请选择支付方式（微信；支付宝；银联）：')
#             if payment == '微信':
#                 return payment
#             elif payment == '支付宝':
#                 return payment
#             elif payment == '银联':
#                 return payment
#             else:
#                 print('选择错误！重新选择！')
#
#     #优惠
#     def discounts(self):
#         self.num = random.randint(10,50)
#         return self.num
#
#
# #子类1：淘宝
# class Taobao(P2P):
#     login_result = P2P('淘宝','马云').login()
#     if login_result:
#         print('huahua您好！')
#         try:
#             account = float(input('请输入你购买的金额：'))
#         except TypeError as e:
#             print('请输入数字！')
#         while True:
#             payment = P2P('淘宝','马云').mode_payment()
#             if payment == '支付宝':
#                 num = P2P('淘宝','马云').discounts()
#                 print('你可以享受优惠！优惠是{}'.format(num))
#                 result = account - num
#                 print('您最终需要支付的金额为：{}'.format(result))
#                 break
#             elif payment == '银联':
#                 print('您本次不享受优惠，谢谢！')
#                 print('您最终需要支付的金额为：{}'.format(account))
#                 break
#             else:
#                 print('微信提示不能支付，请重新选择支付')
#
#     else:
#         print('登录失败！')
#
# #子类2：京东
# class JingDong(P2P):
#     global account
#     login_result = P2P('京东','刘强东').login()
#     if login_result:
#         print('huahua您好！')
#         try:
#             account = float(input('请输入你购买的金额：'))
#         except TypeError as e:
#             print('请输入数字！')
#         while True:
#             payment = P2P('京东','刘强东').mode_payment()
#             if payment == '微信':
#                 num = P2P('京东','刘强东').discounts()
#                 print('你可以享受优惠！优惠是{}'.format(num))
#                 result = account - num
#                 print('您最终需要支付的金额为：{}'.format(result))
#                 break
#             elif payment == '银联':
#                 print('您本次不享受优惠，谢谢！')
#                 print('您最终需要支付的金额为：{}'.format(account))
#                 break
#             else:
#                 print('支付宝提示不能支付，请重新选择支付')
#
#     else:
#         print('登录失败！')
#
#

# if __name__ == '__main__':
#     Taobao('淘宝','马云')
#     JingDong('京东','刘强东')


# 上面写的不好，在独立的方法里写了很多input，无法做自动化测试，应该减少不必要的控制台输入

# 父类，电商平台
class P2P:
    def __init__(self, name=None, feature=None, creater=None):
        self.name = name  # 平台名称
        self.feature = feature  # 平台特征
        self.creater = creater  # 平台创始人
        self.username = 'huahua'
        self.password = '123456'

    # 登录功能
    def login(self):
        username = input('请输入用户名：')
        password = input('请输入密码：')
        if username == self.username and password == self.password:
            print('登录成功！{},欢迎来到{}。'.format(username, self.name))
            return True
        else:
            print('登录失败！用户名或密码错误！')
            return False

    # 支付方式选择
    @staticmethod
    def mode_payment(pay):
        payment = {'1': "微信", '2': '支付宝', '3': '银联'}
        if pay in payment.keys():
            return payment[pay]
        else:
            print('选择错误！重新选择！')
            return False

    # 优惠
    @staticmethod
    def discounts():
        num = random.randint(10, 50)
        return num


# # 子类1：淘宝
# class TaoBao(P2P):
#     username = input('请输入用户名：')
#     password = input('请输入密码：')
#     t = P2P('淘宝', '天猫', '马云')
#     login_result = t.login(username, password)
#     #获取支付金额
#     @staticmethod
#     def pay_account(login_result):
#         while login_result:
#             try:
#                 account = float(input('请输入你购买的金额：'))
#             except TypeError:
#                 print('请输入数字！')
#                 continue
#             return account
#
#     #获取最终金额
#     def account_result(self,account):
#             pay = input('请选择支付方式（1:微信；2:支付宝；3:银联）：')
#             payment = self.mode_payment(pay)
#             while payment:
#                 if payment == '支付宝':
#                     num = self.discounts()
#                     print('你可以享受优惠！优惠是{}'.format(num))
#                     result = account - num
#                     print('您最终需要支付的金额为：{}'.format(result))
#                     break
#                 elif payment == '银联':
#                     print('您本次不享受优惠，谢谢！')
#                     result = account
#                     print('您最终需要支付的金额为：{}'.format(account))
#                     break
#                 else:
#                     print('微信提示不能支付，请重新选择支付')
#             return result


# 子类2：京东
class JingDong(P2P):
    def count(self):
        j = P2P('京东','自营', '刘强东')
        login_result = j.login()
        while login_result:
            try:
                account = float(input('请输入你购买的金额：'))
            except ValueError:
                print('请输入数字！')
                continue
            while account:
                pay = input('请选择支付方式（1:微信；2:支付宝；3:银联）：')
                payment = j.mode_payment(pay)
                if payment == '微信':
                    num = j.discounts()
                    if num < account :
                        print('你可以享受优惠！优惠是{}'.format(num))
                    else:
                        num = 0
                    result = account - num
                    print('您最终需要支付的金额为：{}'.format(result))
                    break
                elif payment == '银联':
                    print('您本次不享受优惠，谢谢！')
                    print('您最终需要支付的金额为：{}'.format(account))
                    break
                elif payment == '支付宝':
                    print('支付宝提示不能支付，请重新选择支付')
            break

if __name__ == '__main__':
    # login_result = TaoBao(P2P)
    # account =TaoBao(P2P).pay_account(login_result)
    # TaoBao(P2P).account_result(account)

    JingDong(P2P)