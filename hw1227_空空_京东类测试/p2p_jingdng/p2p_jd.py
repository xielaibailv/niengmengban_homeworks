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

# 父类，电商平台
#这个写的不好，设计不太合理


class P2P:
    def __init__(self, name=None, feature=None, creater=None):
        self.name = name  # 平台名称
        self.feature = feature  # 平台特征
        self.creater = creater  # 平台创始人
        self.username = 'huahua'
        self.password = '123456'

    # 登录功能
    def login(self,username,password):
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


# 子类：京东
class JingDong(P2P):
    def login_jd(self,username,password):
        login_result = self.login(username,password)
        return login_result

    def count(self,account,pay):
        while 1:
            try:
                account = float(account)
            except ValueError:
                print('请输入数字！')
                continue
            else:
                payment = self.mode_payment(pay)
                if payment == '微信':
                    num = self.discounts()
                    if num < account :
                        print('你可以享受优惠！优惠是{}'.format(num))
                    else:
                        num = 0
                    result = account - num
                    print('您最终需要支付的金额为：{}'.format(result))
                    return result
                elif payment == '银联':
                    print('您本次不享受优惠，谢谢！')
                    print('您最终需要支付的金额为：{}'.format(account))
                    return account
                elif payment == '支付宝':
                    print('支付宝提示不能支付，请重新选择支付')
                    return False
            break



if __name__ == "__main__":
    j = JingDong(name="京东", feature="电商", creater="刘强东")
    j.count(500, "1")