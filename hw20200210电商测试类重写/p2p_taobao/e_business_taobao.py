# 父类：电商平台

# 平台名称
# 功能：登录 支付方式 计算优惠的功能

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


class E_Business:
    def __init__(self, platform_name):
        self.platform_name = platform_name
        self.username = 'admin'
        self.password = '123456'

    # login
    def login(self, username, password):
        if username == self.username and password == self.password:
            print('{},wolcome to {}'.format(username, self.platform_name))
            return True
        else:
            print('登录错误')
            return False

    # 支付方式选择
    @staticmethod
    def choose_pay():
        # pay_way = {1:'微信',2:'支付宝',3:'银联'}
        while True:
            try:
                choose = int(input("请选择支付方式：1:'微信',2:'支付宝',3:'银联'"))
            except ValueError:
                print("请按照提示输入!")
                continue
            if choose in (1, 2, 3):
                return choose
            else:
                print("请按照提示输入!")
                continue

    # 计算优惠
    @staticmethod
    def discounts():
        account = random.randint(1,50)
        return account


class TaoBao(E_Business):

    # 之前在子类里重写了登录类，后来发现没必要，可以直接调用父类的一样可以实现功能
    # 收银
    def count(self, username, password):
        login_result = self.login(username, password)

        while login_result:
            try:
                account = float(input("请输入您本次的消费金额："))
                break
            except ValueError:
                print('请输入数字')
                continue

        while True:
            choose = self.choose_pay()
            if choose == 1:
                print("不好意思，本店不支持微信支付，请选择其他支付方式")
                continue
            elif choose == 2:
                discount = self.discounts()
                if discount < account:
                     final_amount = float('% 0.2f' %(account - discount))
                print("恭喜你本次获得优惠{}，最终需要支付的金额为：{}".format(discount, final_amount))
                break
            elif choose == 3:
                print("您本次需要支付的金额为：{}".format(account))
                break


if __name__ == "__main__":
    tb = TaoBao("淘宝")
    tb.count("admin","123456")

