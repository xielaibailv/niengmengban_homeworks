# 基础题：
#
# 人和机器猜拳游戏写成一个类，有如下几个函数：
# 1）函数1：选择角色1 曹操 2张飞 3 刘备
# 2）函数2：角色猜拳1剪刀 2石头 3布 玩家输入一个1-3的数字
# 3）函数3：电脑出拳 随机产生1个1-3的数字，提示电脑出拳结果
# 4）函数4：角色和机器出拳对战，对战结束后，最后出示本局对战结果...赢...输,然后提示用户是否继续？按y继续，按n退出。
# 5）最后结束的时候输出结果 角色赢几局 电脑赢几局，平局几次 游戏结束


import random


gesture = ['剪刀','石头','布']


class Computer:#电脑类，定义电脑出拳
    @staticmethod
    def computer_play():
        temp = random.randint(1, 3)
        if temp == 1:
            co_ges = '剪刀'
        elif temp == 2:
            co_ges = '石头'
        elif temp == 3:
            co_ges = '布'
        return temp,co_ges


class Role:#角色类，包含角色选择何角色出拳
    def __init__(self):
        self.rolelist =['曹操','张飞','刘备']

    #选择角色
    def choose_role(self):
        choose = input('请选择角色：（1：曹操；2：张飞；3：刘备）')
        if choose == '1':
            self.role = self.rolelist[0]
        elif choose == '2':
            self.role = self.rolelist[1]
        elif choose == '3':
            self.role = self.rolelist[2]
        else:
            print('输入有误！')
        return self.role
    #角色出拳
    def role_play(self,ro_temp):
        if ro_temp.isdigit :
            ro_temp = int(ro_temp)
            if ro_temp not  in (1,2,3):
                print('请按照规则输入！')
        if ro_temp == 1:
            self.ro_ges = gesture[0]
        elif ro_temp == 2:
            self.ro_ges = gesture[1]
        elif ro_temp == 3:
            self.ro_ges = gesture[2]

        return self.ro_ges


# #角色赢的次数：role_win
# #电脑赢的次数：computer_win
# #平局次数：dogfall


def playbegin(dogfall=0,computer_win = 0,role_win = 0):
    print('欢迎进入猜拳游戏！')
    r = Role()
    role = r.choose_role()
    while True:
        ro_temp = input('开始猜拳！请输入你要出的手势：（1：剪刀； 2：石头； 3：布）')
        ro_ges = r.role_play(ro_temp)
        ro_temp = int(ro_temp)
        c = Computer().computer_play()
        co_temp = c[0]
        co_ges =c[1]
        print('电脑出拳，出的是：{}'.format(co_ges))

        if ro_temp == co_temp:
            print('本轮出拳：{}对{}，平局 ！'.format(ro_ges, co_ges))
            dogfall += 1
        elif ro_ges == gesture[0] and co_ges == gesture[1]:
            print('本轮出拳：{}对{}，电脑获胜！ ！'.format(ro_ges, co_ges))
            computer_win +=1
        elif ro_ges == gesture[1] and co_ges == gesture[0]:
            print('本轮出拳：{}对{}，{}获胜！ ！'.format(ro_ges, co_ges,role))
            role_win += 1
        elif ro_ges == gesture[2] and co_ges == gesture[1]:
            print('本轮出拳：{}对{}，{}获胜！ ！'.format(ro_ges ,co_ges, role))
            role_win += 1
        elif ro_ges == gesture[0] and co_ges == gesture[2]:
            print('本轮出拳：{}对{}，{}获胜！ ！'.format(ro_ges, co_ges, role))
            role_win += 1
        elif ro_ges == gesture[1] and co_ges == gesture[2]:
            print('本轮出拳：{}对{}，电脑获胜！ ！'.format(ro_ges, co_ges))
            computer_win += 1
        elif ro_ges == gesture[2] and co_ges == gesture[0]:
            print('本轮出拳：{}对{}，电脑获胜！ ！'.format(ro_ges, co_ges))
            computer_win += 1
        qt = input('是否继续？按y继续，按n退出：')
        if qt == 'y':
            continue
        if qt == 'n':
            break

    print('角色赢{}局 ;电脑赢{}局;平局{}次 ,游戏结束。'.format(role_win,computer_win,dogfall))


playbegin()