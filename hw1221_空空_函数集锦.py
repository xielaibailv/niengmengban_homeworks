import random
#新手练习
#1：编写一个名为 make_shirt()的函数，它接受一个尺码以及要印到 T 恤上的字样。这个函数应打印一个句子，概要地说明 T 恤的尺码和字样。

def make_shirt(size,words):
    print("""定制T 恤参数如下：
          尺码：%s
          字样：%s""" %(size,words))

make_shirt(39,"朕就是这样的汉子")

#--------------------------------------------------------------------------------------------------
#2：编写一个名为 describe_city()的函数，它接受一座城市的名字以及该城市所属的国家。
# 这个函数应打印一个简单的句子，如 Reykjavik is in Iceland。给用于存储国家的形参指定默认值。
# 为三座不同的城市调用这个函数，且其中至少有一座城市不属于默认国家。

def describe_city(city,country = 'China'):
    print("{} is in {}。".format(city,country))

describe_city('上海')
describe_city('New York','America')
describe_city('杭州','中国')

#-----------------------------------------------------------------------------------------------------

#3：编写一个名为 city_country()的函数，它接受城市的名称及其所属的国家。这个函数应返回一个格式类似于下面这样的字符串：
# "长沙, 中国"
#至少使用三个城市国家对调用这个函数，并打印它返回的值。

def city_country(city,country):
    city_country = '"{},{}"'.format(city,country)
    return city_country

print(city_country('武汉','中国'))
print(city_country('成都','中国'))
print(city_country('巴黎','法国'))

#-----------------------------------------------------------------------------------------------------
#4：编写一个名为 make_album()的函数，它创建一个描述音乐专辑的字典。
# 这个函数应接受歌手的名字和专辑名，并返回一个包含这两项信息的字典。
# 使用这个函数创建三个表示不同专辑的字典，并打印每个返回的值，以核实字典正确地存储了专辑的信息。

def make_album(name,album):
    album = {name:album}
    return album

print(make_album('朴树','生如夏花'))
print(make_album('平安','倒带人生'))
print(make_album('王力宏','龙的传人'))

#-----------------------------------------------------------------------------------------------------

#5：编写一个函数，它接受顾客要在三明治中添加的一系列食材。
# 这个函数只有一个形参（它收集函数调用中提供的所有食材），并打印一条消息，对顾客点的三明治进行概述。
# 调用这个函数三次，每次都提供不同数量的实参。

def sandwich(*args):
    print("您点的三明治要添加的食材如下：",end='')
    for item in args:
        print(item + ' ',end='')

    print('')

sandwich('火腿','培根')
sandwich('火腿','培根','洋葱','鸡蛋')
sandwich('火腿','培根','鸡蛋','土豆','牛肉')

#-----------------------------------------------------------------------------------------------------

#初级题型
#1：定义一个函数，成绩作为参数传入。
# 如果成绩小于60，则输出不及格。如果成绩在60到80之间，则输出良好；
# 如果成绩高于80分，则输出优秀，如果成绩不在0-100之间，则输出 成绩输入错误。

def grade(num):
    if num.isdigit():
        num = int(num)
        if num < 60 and num >= 0:
            print("不及格 T_T")
        elif num >=60 and num < 80:
            print("良好~_~")
        elif num >= 80 and num <= 100:
            print("优秀 ^_^")
        else:
            print("成绩输入错误-_-")

    else:
        print("请输入0-100之间的整数！")

grade('90')
grade('80')
grade('59')
grade('109')
grade('-9')

#-----------------------------------------------------------------------------------------------------

# 2：用函数实现：
# 企业发放的奖金根据利润提成。
# 利润(I)低于或等于10万元时，奖金可提10%；
# 利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可可提成7.5%；
# 20万到40万之间时，高于20万元的部分，可提成5%；
# 40万到60万之间时高于40万元的部分，可提成3%；
# 60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，
# 从键盘输入当月利润I，求应发放奖金总数？

def bonus(I):
    bonus_num = 1
    if I <= 100000:
        bonus_num = I * 0.1
    elif I > 100000 and I <= 200000:
        bonus_num= 100000 * 0.1 + (I - 100000) * 0.075
    elif I > 200000 and I <= 400000:
        bonus_num = 100000 * 0.1 + 100000 * 0.075 + (I - 200000) * 0.05
    elif I > 400000 and I <= 600000:
        bonus_num = 100000 * 0.1 + 100000 * 0.075 + 200000 * 0.05 + (I - 400000) * 0.03
    elif I > 600000 and I <= 1000000:
        bonus_num = 100000 * 0.1 + 100000 * 0.075 + 200000 * 0.05 + 200000 * 0.03 +  (I - 600000) * 0.015
    elif I > 1000000:
        bonus_num = 100000 * 0.1 + 100000 * 0.075 + 200000 * 0.05 + 200000 * 0.03 + 400000 * 0.015 + (I - 1000000) * 0.01

    print("应发放奖金总数：%d" % bonus_num)


I = int(input("请输入当月利润："))
bonus(I)

#-----------------------------------------------------------------------------------------------------

# 3：用python函数实现如下:
# 随机产生一个数，让用户来猜，猜中结束，若猜错，则提示用户猜大或猜小。

secret = random.randint(0, 9)
temp = input("来猜猜小公主我现在心里想的是哪一个数字：")
while not temp.isdigit():
    print("输入不合法，请重新输入!")
    temp = input('请输入整数：')
    guess = int(temp)
else:
    temp = int(temp)
    if temp == secret:
        print("我擦，你是小公主我肚子里的蛔虫吗？？！！")
        print("哼，猜中了也没有奖励！")
    else:
            if temp > secret:
                print("大了大了~~~")
            else:
                print("小了小了！！")

    print("游戏结束！")

#-----------------------------------------------------------------------------------------------------
# 4：写函数，判断用户传入的对象（字符串、列表、元组）长度是否大于5

def panduan(what):
    print("判断对象是否大于5")
    if len(what) > 5:
        return True
    if len(what) < 5:
        return False
what = input("输入：")
print(panduan(what))

#-----------------------------------------------------------------------------------------------------

# 5：写函数，将姓名、性别，城市作为参数，并且性别默认为f(女)。
# 如果城市是在长沙并且性别为女，则输出姓名、性别、城市，并返回True,否则返回False

def people(name,city,sex = 'f'):
    if city =='长沙' and sex == 'f':
        print('''
        name: %s
        sex: %s
        city:%s''' %(name,sex,city))
        return True
    else:
        return False

print(people('华华','长沙'))
print(people('唐长老','长沙','m'))

#-----------------------------------------------------------------------------------------------------
# 6：写函数，检查传入列表的长度，如果大于2，那么仅仅保留前两个长度的内容，并将新内容返回

def check(list_t):
    if len(list_t) > 2:
        list_f = list_t[0:2]
        return list_f
    else:
        return list_t

list_t = ['a','b','c','d']
print(check(list_t))

#-----------------------------------------------------------------------------------------------------
# 7：定义一个函数，传入一个字典和字符串，判断字符串是否为字典中的值，如果字符串不在字典中，则添加到字典中，并返回新的字典。

def check1(str,dict):
    if str in dict:
        return dict[str]
    else:
        dict.setdefault(str)  #没有直接加一条
        return dict

str = '鲁迅'
dict = {'张爱玲':'出名要趁早','穆旦':'我要赞美'}
print(check1(str,dict))

#-----------------------------------------------------------------------------------------------------
# 中级题型：
# 1：有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？

count = 0
numbers = []
for item1 in range(1,5):
    for item2 in range(1,5):
        for item3 in range(1,5):
            if item1 != item2 and item2 != item3 and item1 != item3:
                num = item1*100 + item2 * 10 + item3 *1
                numbers.append(num)
                count += 1

print(count)
print(numbers)

#-----------------------------------------------------------------------------------------------------
# 2：一个足球队在寻找年龄在m岁到n岁的男生or女生（包括m岁和n岁，到底是找男生还是女生，可指定性别）加入。
# 编写一个程序，询问用户的性别（m表示男性，f表示女性）和年龄，
# 然后显示一条消息指出这个人是否可以加入球队，询问k次后，输出满足条件的总人数。

def find_partners(m,n,sex,k):
    temp = k
    team = []
    while temp:
        sex0 = input("请输入你的性别(m表示男性，f表示女性)：")
        if sex0.isalpha():
            if sex0 != sex:
                print("性别不符合要求！")
            elif sex0 == sex:
                age = input("请输入你的年龄：")
                if age.isdigit():
                    age = int(age)
                    if age <= n and age >= m:
                        team.append(age)
                    else:
                        print("年龄不符合要求！")
                else:
                    print("请输入正整数！")
            else:
                print("输入有误！")
        else:
            print("请输入符合条件的字母！")
        temp -= 1
    print("本次合格的人数有：%d" %(len(team)))

find_partners(10,12,'f',3)
