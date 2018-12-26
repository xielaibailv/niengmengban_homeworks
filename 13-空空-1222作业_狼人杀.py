# 高级题：

 #写一个警察类：
#警察具有这些属性： 代号 真实姓名 年龄 类别:police
#技能：开枪，但是开枪前先要知道 是否是坏蛋，不能对平民开枪、 指认、 抓坏蛋 、run 跑起来很快

#写一个坏人类：
#坏人具有这些属性：绰号 真实姓名 年龄 类别:badegg
#技能：开枪，可以对警察和平民开枪 、 run 跑起来很快 、偷东西、抢银行

# 写一个平民类： #平民具有这些属性：昵称 真实姓名 年龄 类别:people
#技能：run 跑起来很快 、指认技能

#规则：一共有5个平民 3个坏蛋 2个警察，所有的都只能指认一次，按顺序来。同类人之间不能相互指认
#1：坏蛋：pitt 河畔 海绵---->一起 意见统一才能出击(少数服从多数)，如果指认比例平局就作废没人牺牲，如果去抢银行偷东西，那么就不参与指认。
#2：平民：花花 七月 晴天 简爱 阿牛---->一起 意见统一(少数服从多数)才能出击，不管是指认了警察还是坏蛋都会牺牲， #如果指认比例平局就作废没人牺牲，
#3：警察： 挖矿 月亮---->一起 意见统一才能出击，才能出击，不统一作废。 # 如果正确的指认了坏蛋，开枪，坏蛋牺牲，如果指认了平民，指认无效，这一轮结束

#最后结果：
#如果坏蛋为0 那么警察、平民赢
#如果平民为0 警察、平民输
#如果警察为0 警察、平民输
import random

class Police:
    def __init__(self,code,name,age):
        self.code = code     #代号
        self.name = name   #姓名
        self.age = age          #年龄
        self.sort = 'police'     # 类别

    # 开枪
    def gun(self,man):
        print('抓到坏人！开枪！biubiu~')
        print('警察打死了坏人%s' %man.code)


    # 跑的技能
    def run(self):
        print('我跑的很快~~~')


class BadEgg:
    def __init__(self,code,name,age):
        self.code = code     #绰号
        self.name = name   #姓名
        self.age = age          #年龄
        self.sort = 'badegg'     # 类别

    #开枪
    def gun(self):
        print('管你是谁！开枪！biubiu~')

    #跑的技能
    def run(self):
        print('我跑的很快~~~')

    #偷东西
    def thief(self):
        print('咦，这是个好东西，哈哈，我看见就是我的啦！！！')

    #抢银行
    def rob(self):
        print('都给我蹲下！不许报警，把钱拿出来！')


class People:
    def __init__(self,code,name,age):
        self.code = code     #昵称
        self.name = name   #姓名
        self.age = age          #年龄
        self.sort = 'people'     # 类别

    # 跑的技能
    def run(self):
        print('我跑的很快~~~')

    #指认技能
    def identify(self):#意见统一指认成功
        temp = random.randint(0,1)
        if temp:
            return True
        else:
            return False


def main():
    badegg = []
    police = []
    people = []

    #创建坏人
    for i in range(3):
        #每遍历一次创建一个坏蛋
        new_badegg = BadEgg('刀疤'+str(i),'张三'+str(i),28+i)
        #将坏蛋存进列表
        badegg.append(new_badegg)

    #创建警察
    for i in range(2):
        # 每遍历一次创建一个警察
        new_police = Police('秋叶' + str(i), '王朝' + str(i), 30 + i)
        # 将警察存进列表
        police.append(new_police)

        # 创建平民
    for i in range(5):
        # 每遍历一次创建一个平民
        new_people = People('狗子' + str(i), '李' + str(i), 25 + i)
        # 将平民存进列表
        people.append(new_people)

    print('坏人开始行动！')
    #随机选出一个数，0：开枪；1：跑；2：偷东西；3：抢银行
    while True:
        temp = random.randint(1,3)
        if temp == 1:
            print('坏人选择开枪！')
                #随机选择一个人
            man = random.choice(people or police)
            badegg[0].gun()
            print('坏人开枪打死一个%s,%s' %(man.sort,man.code))
            if man in police:
                police.remove(man)
            else:
                people.remove(man)
        if temp == 2:
            print('坏人选择逃跑！')
            badegg[0].run()
        if temp == 3:
            print('坏人选择偷东西！')
            badegg[0].thief()
        if temp == 4:
            print('坏人选择抢银行！')
            badegg[0].rob()
        print('')
        print('平民开始指认。')
        man = random.choice(badegg or police)
        if man in police:
            police.remove(man)
            print('指认结果：警察。%s牺牲' % man.code)
        elif man in badegg:
            print('指认结果：坏蛋。指认成功！')
            police[0].gun(man)
            badegg.remove(man)
            print('')

        if not badegg:
            print('坏蛋全部牺牲，警察和平民胜利，游戏结束！')
            break
        elif not police:
            print('警察全部牺牲，坏蛋胜利，游戏结束！')
            break
        elif not people:
            print('平民全部牺牲，坏蛋胜利，游戏结束！')
            break


if __name__ == '__main__':
    main()