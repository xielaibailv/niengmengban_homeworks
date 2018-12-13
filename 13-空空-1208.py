# 1：一家商场在降价促销。
# 如果购买金额50-100元(包含50元和100元)之间，会给10%的折扣
# 如果购买金额大于100元会给20%折扣。
# 编写一程序，询问购买价格，再显示出折扣（%10或20%）和最终价格


def sales():
    money = input('请输入购买金额：')
    if money.isdigit():
        money = int(money)
        if money >= 50 and money <=100:
            discount = 0.1
        elif money > 100:
            discount = 0.2
        else:
            discount = 0

        price = money * (1-discount)
        # return(price, discount)
        print('您获得的折扣是：{:0.1%}' .format(discount))
        print('最终价格为：%d' % price)

    else:
        print('输入错误！')
sales()


#2、输出99乘法表

def Multipication_Table():
    num = 1
    while num <10:
        for i in range(num,10):
            print('%d * %d = %d' %(num,i,(num * i)))
        num += 1

Multipication_Table()

# 3、输入num为四位数，对其按照如下的规则进行加密：
# 1）每一位分别加5，然后分别将其替换为该数除以10取余后的结果
# 2）将该数的第1位和第4为互换，第二位和第三位互换
# 3）最后合起来作为加密后的整数输出

num = input('请输入四位数：')
result = []
for i in num:
    a = int(i) + 5
    b = a%10
    result.append(b)
result[0],result[3] = result[3],result[0]
result[1],result[2] = result[2],result[1]

x1 = result[0]*1000
x2 = result[1]*100
x3 = result[2]*10
x4 = result[3]*1

print(x1+x2+x3+x4)



# 4：用户的登录信息存在在字典里面，例如{" admin ":"lemon","huahua":"123456"}，
#
# 用户名：admin 对应密码：lemon
#
# 用户名：huahua对应密码：123456
#
# 根据上述信息以及下列条件写出符合题目的程序代码：
#
# 1）设计1个登陆的程序， 不同的用户名和对成密码存在个字典里面， 输入正确的用户名和密码去登陆，
#
# 2）首先输入用户名，如果用户名不存在或者为空，则一直提示输入正 确的用户名
#
# 3）当用户名正确的时候，提示去输入密码，如果密码跟用户名不对应， 则提示密码错误请重新输入。
#
# 4）如果密码输入错误超过三次，中断程序运行。
#
# 5）当输入密码错误时，提示还有几次机会
#
# 6）用户名和密码都输入正确的时候，提示登陆成功!'''

user = {'admin':'lemon','huahua':'123456'}


def login():
    while 1:
        name = input('请输入用户名：')
        if name in user.keys():
            count = 3
            while count:
                pwd = input('请输入密码：')
                if pwd == user[name]:
                    print('登录成功~~~，欢迎进入python世界^_^')
                    break
                else:
                    print('密码错误！请重新输入！', end='')
                    count -= 1
                    print('您还有%d次机会！' % (count))
            break
        else:
            print('请输入正确的用户名！', end='')

login()