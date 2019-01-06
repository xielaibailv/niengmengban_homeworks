
# 1：写一段程序，分别求出0-100之间的所有偶数的和和所有奇数的和。
#第一中方法
even = []
odd = []
for i in range(1,101):
    if i % 2 != 0:
        odd.append(i)
    else:
        even.append(i)

even_sum = 0
odd_sum = 0
for index in even:
    even_sum += index
for index in odd:
    odd_sum += index

print("1-100里偶数的和是：%d" %even_sum)
print("1-100里奇数的和是：%d" %odd_sum)


#第二种方法

odd_sum1 = 0
even_sum1 = 0
for i in range(1,100,2):
    odd_sum1 += i
for i in range(0,101,2):
    even_sum1 += i
print(odd_sum1)
print(even_sum1)

# 2：一个足球队在寻找年龄在10岁到12岁的小女孩（包括10岁和12岁）加入。
# 编写一个程序，询问用户的性别（m表示男性，f表示女性）和年龄，
# 然后显示一条消息指出这个人是否可以加入球队，询问10次后，输出满足条件的总人数。

temp = 10
team = []
while temp:
    sex = input("请输入你的性别(m表示男性，f表示女性)：")
    if sex.isalpha():
        if sex == 'm':
            print("性别不符合要求！")
        elif sex == 'f':
            age = input("请输入你的年龄：")
            if age.isdigit():
                age = int(age)
                if age <=12 and age >=10:
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




# 3：请输出如下直角三角形：

row = 1
for i in range(6):
    if row <= 6:
        print('*'*i)
        row += 1
