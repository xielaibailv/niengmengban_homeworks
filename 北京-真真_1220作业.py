#-*-coding:utf-8-*-
#@Time    :2018/12/21 11:02
#@Author  :liu_zhenzhen
#@File    :北京-真真_1220作业.py

#编写机器人类
#特征：品牌、价格、颜色、材质、尺寸
#功能：聊天、学前教育、扫地、端水、做饭、智能跟随

#对象：
#特征：新威尔NWELL、583、白色、塑料、46*28*30
#功能：聊天、放音乐、扫地、早教、智能跟随

class Robot:
    #这个是机器人的属性和功能
    brand='NWELL'
    price=538
    colour='white'
    material='plastic'
    size='46*28*30'

    def chat(self,name='露露'):    #对象方法
        print('可以和{}聊天'.format(name))

    @staticmethod       #静态方法   在静态方法中访问对象方法，需要创建一个对象再访问
    def music():
        Robot().chat('小孩儿')  #创建一个对象
        print('可以听音乐')

    @classmethod         #类方法    在类方法中访问静态方法、对象方法
    def sweep(cls):
        cls.music()             #cls是类本身
        Robot.music()
        cls().chat('老人')      #cls是类本身，故cls()和Robot()是一样的，都是创建一个对象
        Robot().chat('爸爸')
        print('可以扫地')

    def education(self):
        self.music()    #对象方法   在对象方法中访问静态方法、类方法、对象方法（self就是r）
        Robot.sweep()
        Robot.chat('妈妈')
        print('可以早教')

    def follow(self):
        print('可以跟随')

r=Robot()
#访问类的属性：类和对象可以直接访问属性，并获得它们的值
# print(r.brand)      #对象.属性名
# print(Robot.size)   #类名.属性名
#
# #访问类的方法
# r.chat('dawei')    #利用对象---访问对象方法
# r.music()       #利用对象---访问静态方法
# Robot.music()   #利用类---访问静态方法
# r.sweep()        #利用对象---访问类方法
# Robot.sweep()    #利用类---访问类方法
r.education()
