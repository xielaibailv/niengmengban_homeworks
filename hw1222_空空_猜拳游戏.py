# 基础题：
#
# 人和机器猜拳游戏写成一个类，有如下几个函数：
# 1）函数1：选择角色1 曹操 2张飞 3 刘备
# 2）函数2：角色猜拳1剪刀 2石头 3布 玩家输入一个1-3的数字
# 3）函数3：电脑出拳 随机产生1个1-3的数字，提示电脑出拳结果
# 4）函数4：角色和机器出拳对战，对战结束后，最后出示本局对战结果...赢...输,然后提示用户是否继续？按y继续，按n退出。
# 5）最后结束的时候输出结果 角色赢几局 电脑赢几局，平局几次 游戏结束


import random



# gesture = ['剪刀','石头','布']
#
#
# class Computer:#电脑类，定义电脑出拳
#     @staticmethod
#     def computer_play():
#         temp = random.randint(1, 3)
#         if temp == 1:
#             co_ges = '剪刀'
#         elif temp == 2:
#             co_ges = '石头'
#         elif temp == 3:
#             co_ges = '布'
#         return temp,co_ges
#
#
# class Role:#角色类，包含角色选择何角色出拳
#     def __init__(self):
#         self.rolelist =['曹操','张飞','刘备']
#
#     #选择角色
#     def choose_role(self):
#         choose = input('请选择角色：（1：曹操；2：张飞；3：刘备）')
#         if choose == '1':
#             self.role = self.rolelist[0]
#         elif choose == '2':
#             self.role = self.rolelist[1]
#         elif choose == '3':
#             self.role = self.rolelist[2]
#         else:
#             print('输入有误！')
#         return self.role
#     #角色出拳
#     def role_play(self,ro_temp):
#         if ro_temp.isdigit :
#             ro_temp = int(ro_temp)
#             if ro_temp not  in (1,2,3):
#                 print('请按照规则输入！')
#         if ro_temp == 1:
#             self.ro_ges = gesture[0]
#         elif ro_temp == 2:
#             self.ro_ges = gesture[1]
#         elif ro_temp == 3:
#             self.ro_ges = gesture[2]
#
#         return self.ro_ges
#
#
# # #角色赢的次数：role_win
# # #电脑赢的次数：computer_win
# # #平局次数：dogfall
#
#
# def playbegin(dogfall=0,computer_win = 0,role_win = 0):
#     print('欢迎进入猜拳游戏！')
#     r = Role()
#     role = r.choose_role()
#     while True:
#         ro_temp = input('开始猜拳！请输入你要出的手势：（1：剪刀； 2：石头； 3：布）')
#         ro_ges = r.role_play(ro_temp)
#         ro_temp = int(ro_temp)
#         c = Computer.computer_play()   # 这是一个静态方法，可直接用类调用
#         co_temp = c[0]
#         co_ges =c[1]
#         print('电脑出拳，出的是：{}'.format(co_ges))
#
#         if ro_temp == co_temp:
#             print('本轮出拳：{}对{}，平局 ！'.format(ro_ges, co_ges))
#             dogfall += 1
#         elif ro_ges == gesture[0] and co_ges == gesture[1]:
#             print('本轮出拳：{}对{}，电脑获胜！ ！'.format(ro_ges, co_ges))
#             computer_win +=1
#         elif ro_ges == gesture[1] and co_ges == gesture[0]:
#             print('本轮出拳：{}对{}，{}获胜！ ！'.format(ro_ges, co_ges,role))
#             role_win += 1
#         elif ro_ges == gesture[2] and co_ges == gesture[1]:
#             print('本轮出拳：{}对{}，{}获胜！ ！'.format(ro_ges ,co_ges, role))
#             role_win += 1
#         elif ro_ges == gesture[0] and co_ges == gesture[2]:
#             print('本轮出拳：{}对{}，{}获胜！ ！'.format(ro_ges, co_ges, role))
#             role_win += 1
#         elif ro_ges == gesture[1] and co_ges == gesture[2]:
#             print('本轮出拳：{}对{}，电脑获胜！ ！'.format(ro_ges, co_ges))
#             computer_win += 1
#         elif ro_ges == gesture[2] and co_ges == gesture[0]:
#             print('本轮出拳：{}对{}，电脑获胜！ ！'.format(ro_ges, co_ges))
#             computer_win += 1
#         qt = input('是否继续？按y继续，按n退出：')
#         if qt == 'y':
#             continue
#         if qt == 'n':
#             break
#
#     print('角色赢{}局 ;电脑赢{}局;平局{}次 ,游戏结束。'.format(role_win,computer_win,dogfall))


#
#
# if __name__ == '__main__':
#     playbegin()





#之前的方法分类不是很清，整个逻辑也不流畅，重新写了一下

class Gesture:
    def __init__(self):
        self.gesture = {'1' : "剪刀", '2': '石头', '3': '布'}


    # 选择角色
    @staticmethod
    def choose_role():
        while 1:
                choose = input('请选择角色：（1：曹操；2：张飞；3：刘备）')
                if choose not in ('1','2','3'):
                    print('输入有误！')
                else:
                    if choose == '1':
                        role = '曹操'
                        break
                    elif choose == '2':
                        role = '张飞'
                        break
                    elif choose == '3':
                        role = '刘备'
                        break

        return role

    #角色出拳
    def role_play(self,role):
            while 1:
                ro_temp = input('开始猜拳！请输入你要出的手势：（1：剪刀； 2：石头； 3：布）')
                if ro_temp in self.gesture.keys():
                    self.ro_ges = self.gesture[ro_temp]
                    break
                else:
                    print('请按照规则输入！')
            print('{}，你出的是{}'.format(role,self.ro_ges))

            return self.ro_ges

    #电脑出拳
    @staticmethod
    def computer_play(self):
        co_temp = random.randint(1, 3)
        if str(co_temp) in self.gesture.keys():
            co_ges = self.gesture[str(co_temp)]
        print('电脑出的是{}'.format(co_ges))

        return co_ges

    # 对战
    def fight(self,dogfall=0,computer_win = 0,role_win = 0):
        print('欢迎进入猜拳游戏！')
        #获取角色
        role = self.choose_role()
        while 1:
            # 获取角色出拳的手势
            ro_ges = self.role_play(role)
            # 获取电脑出拳的手势
            co_ges =self.computer_play(self)

            if ro_ges == co_ges:
                    print('本轮出拳：{}对{}，平局 ！'.format(ro_ges, co_ges))
                    dogfall += 1
            elif ro_ges == self.gesture['1'] and co_ges == self.gesture['2']:
                print('本轮出拳：{}对{}，电脑获胜！ ！'.format(ro_ges, co_ges))
                computer_win +=1
            elif ro_ges == self.gesture['2'] and co_ges == self.gesture['1']:
                print('本轮出拳：{}对{}，{}获胜！ ！'.format(ro_ges, co_ges,role))
                role_win += 1
            elif ro_ges == self.gesture['3'] and co_ges == self.gesture['2']:
                print('本轮出拳：{}对{}，{}获胜！ ！'.format(ro_ges ,co_ges, role))
                role_win += 1
            elif ro_ges == self.gesture['1'] and co_ges == self.gesture['3']:
                print('本轮出拳：{}对{}，{}获胜！ ！'.format(ro_ges, co_ges, role))
                role_win += 1
            elif ro_ges == self.gesture['2'] and co_ges == self.gesture['3']:
                print('本轮出拳：{}对{}，电脑获胜！ ！'.format(ro_ges, co_ges))
                computer_win += 1
            elif ro_ges == self.gesture['3'] and co_ges == self.gesture['1']:
                print('本轮出拳：{}对{}，电脑获胜！ ！'.format(ro_ges, co_ges))
                computer_win += 1
            qt = input('是否继续？按y继续，按n退出：')
            if qt == 'y':
                continue
            if qt == 'n':
                break

        print('角色赢{}局 ;电脑赢{}局;平局{}次 ,游戏结束。'.format(role_win,computer_win,dogfall))

# 重新写了一次，简化了某些判断，更通用化
class PlayGame:
    def __init__(self):
        self.gesture = {'1' : "剪刀", '2': '石头', '3': '布'}

    def choose_role(self):
        role_list = {"1":"曹操","2":"张飞","3":"刘备"}
        while True:
            choose = input('请输入数字选择角色：1 曹操 2张飞 3 刘备')
            if choose in role_list.keys():
                role = role_list[choose]
                print('您的角色是：{}'.format(role_list[choose]))
                break
            else:
                print('输入有误，请重新输入')
                continue
        return role

    def role_play(self,role):
        while True:
            choose = input('{}请出拳：（1：剪刀； 2：石头； 3：布）'.format(role))
            if choose in self.gesture.keys():
                self.role_fist = self.gesture[choose]
                print('{}出拳：{}'.format(role, self.role_fist))
                break
            else:
                print('输入错误，请重新出拳')
                continue
        return int(choose)

    def computer_play(self):
        com_temp = random.randint(1,3)
        computer_fist = self.gesture[str(com_temp)]
        print('电脑出拳：{}'.format(computer_fist))
        return com_temp

    def play(self):
        dogfall = 0
        com_win = 0
        role_win = 0
        print('wolcome to play fist game!')
        role = self.choose_role()
        while True:
            role_fist = self.role_play(role)
            computer_fist = self.computer_play()
            if (computer_fist - role_fist) in [-2,1]:
                print('电脑获胜！')
                com_win += 1
            elif (computer_fist - role_fist) in [-1,2]:
                print('{}获胜！'.format(role))
                role_win += 1
            elif computer_fist == role_fist:
                print('平局！')
                dogfall += 1
            choose = input('是否继续游戏？y继续，其他任意键退出')
            if choose == 'y':
                continue
            else:
                print('游戏结束。电脑获胜{}，玩家获胜{}，平局{}'.format(com_win, role_win, dogfall))
                break



if __name__ == '__main__':
    Gesture().fight()
    game = PlayGame().play()
