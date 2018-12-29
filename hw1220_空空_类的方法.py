#1：编写手机类 机器人类 要求至少有5个属性，5个方法（要包含对象方法 类方法 静态方法）

class Phone:
    name = '华为'
    model = 'P 20'
    color = '极光色'
    size = '6.2'
    system = 'Android'

    @staticmethod
    def call(num = 110):     #静态方法不需要传self
        print('请输入电话号码...拨打紧急电话请按1')
        print('正在拨打紧急电话{}...'.format(num))
        Phone.photo()     #调用类方法

    def wechat(self):
        print('给吴亦凡发信息：今晚吃烤肉好不好呀？')
        print('发送成功...')

    @classmethod
    def photo(cls):    #类方法一般使用 cls作为默认参数
        print('准备拍照')
        cls.call()     #调用静态方法
        cls().wechat()  #调用对象方法

    def study(self,app):
        print('准备打开%s...' %(app))
        print('开始学习...')

    def music(self,songname):
        print('正在寻找{}...'.format(songname))
        print('开始播放{}...'.format(songname))


