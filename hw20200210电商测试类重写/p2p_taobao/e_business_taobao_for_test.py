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
    def choose_pay(pay_way):
        # pay_way = {1:'微信',2:'支付宝',3:'银联'}
            try:
                pay_way = int(pay_way)
                if pay_way in (1,2,3):
                    return pay_way
                else:
                    print("请选择正确的支付方式。")
            except ValueError:
                print("输入错误，只允许输入数字")


    # 计算优惠
    @staticmethod
    def discounts():
        account = random.randint(1, 50)
        return account


class TaoBao(E_Business):

    # 收银
    # 正常的程序，应该不用考虑需要重复输入的情况，应该是重新调用接口，所以不需要写那么多while循环
    # 也应该尽量不要在方法中出现需要用户输入的代码？应该由函数作为参数传进来
    def login_tb(self, username, password):
        login_result = self.login(username, password)
        return login_result

    def count(self, login_result, account, pay_way):
        # account:消费金额
        # pay_way: 支付方式
        if login_result:
            try:
                account = float(account)
            except ValueError:
                print('请输入数字')
                return False
            # 调用选择支付方式的接口，获取支付方式
            choose = self.choose_pay(pay_way)
            if choose == 1:
                print("不好意思，本店不支持微信支付")
                return False
            elif choose == 2:
                # 选择支付宝，则进行随机金额的优惠
                discount = self.discounts()
                if discount < account:
                    final_amount = float('% 0.2f' %(account - discount))
                else:
                    # 如果优惠金额大于消费金额，则不优惠
                    final_amount = float('% 0.2f' % account)
                    discount = 0
                print("恭喜你本次获得优惠{}，最终需要支付的金额为：{}".format(discount, final_amount))
                return True
            # 如果是银联支付，则无优惠
            elif choose == 3:
                final_amount = float('% 0.2f' % account)
                print("您本次需要支付的金额为：{}".format(final_amount))
                return final_amount



if __name__ == "__main__":
    tb = TaoBao("淘宝")
    login = tb.login_tb("admin","123456")
    money = tb.count(login,"200","1")
    print(money)


