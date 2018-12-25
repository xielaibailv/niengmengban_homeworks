#enconding: utf-8
#name:  huahua

#编写机器人类:智能机器人属性和功能
#颜色  品牌  大小  移动速度  价格
# 人脸识别    #语音对讲  #紧急呼叫   #语音播报   #播放歌曲

class IntelligentRobot:
    '这是个智能机器人类，有机器人的属性和功能'
    color='blue'
    brand='优必选'
    size='1243*925*1110mm'
    speed='0-1m/s'
    price=6599

    def  face_recognition(self):  # 人脸识别  对象方法 (只能通过对象访问)
        print("你好呀，我可以做人脸识别！")

    @staticmethod
    def  voice_intercom(name):  #语音对讲   静态方法 (类和对象来访问)
        print("你好呀，我可以语音对讲，你可以和{}进行通话对讲".format(name))

    def  emergency_call(self,phone_number=110):    #紧急呼叫   对象方法
        print("你好呀，我可以进行紧急呼叫，当前呼叫的号码为:",phone_number)

    @classmethod
    def  voice_announcements(cls,*args):   #语音播报   类方法 (类和对象来访问)
        print("你好呀，我可以进行语音播报，当期播报的内容是:",args)

    @classmethod
    def   sing_song(cls,song):    #播放歌曲    类方法
        print("你好呀，我可以播放歌曲，即将播放的歌曲是:",song)

robot=IntelligentRobot()   #创建对象

print("机器人价格是:",robot.price)   #对象调用属性
print("机器人品牌是:",IntelligentRobot.brand)   #类调用属性
print("机器人颜色是:",robot.color)    #对象调用属性
print("机器人移动速度是:",IntelligentRobot.speed)   #类调用属性

robot.face_recognition()

robot.voice_intercom('花花')
IntelligentRobot.voice_intercom("小明")

robot.emergency_call()
robot.emergency_call(119)

robot.voice_announcements('今天可能会有雨','提醒大家出门带雨伞','别忘记啦！')
IntelligentRobot.voice_announcements('下午三点要开会','请大家不要迟到了')

robot.sing_song('传奇')
IntelligentRobot.sing_song('沙漠骆驼')

