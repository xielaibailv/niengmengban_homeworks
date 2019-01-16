import configparser       # 配置类，专门来读取配置文件的

# section  :  片段 / 区域  【区域名】
# option  :  一个一个的配置选项

# 1，对于读取出来的值没有要求，字符串OK
# cf = configparser.ConfigParser()
# cf.read('file',encoding = 'utf-8')     # 打开配置文件，相当于 open()
# value = cf.get('section','option_key')
# # value = cf['section']['option_key']          # 两种方法读取


# # 2，配置文件里存在列表，字典等格式，想要读取出来的值仍然是列表，字典等格式
# cf = configparser.ConfigParser()
# cf.read('file',encoding = 'utf-8')     # 打开配置文件，相当于 open()
# # 第一种方法
# value = eval(cf.get('section','option_key'))
# 第二种方法(只有这3种，其他格式没有)
# value = cf.getfloat('section','option_key')
# value = cf.getint('section','option_key')
# value = cf.getboolean('section','option_key')


class ReadConfig:

    def __init__(self,file):
        self.cf = configparser.ConfigParser()
        self.cf.read(file,encoding = 'utf-8')

    # 读普通值
    def get_value(self,section,option):
        return self.cf.get(section, option)

    # 读整数
    def get_int(self,section,option):
        return self.cf.getint(section, option)

    # 读浮点数
    def get_float(self,section,option):
        return self.cf.getfloat(section, option)

    # 读布尔值
    def get_boolean(self,section,option):
        return self.cf.getboolean(section, option)


if __name__ == '__main__':
    res = ReadConfig('config.conf').get_value('Section','a')
    print(res,type(res))
    res = ReadConfig('config.conf').get_int('Section', 'a')
    print(res, type(res))
    res = ReadConfig('config.conf').get_value('Section', 'b')
    print(res, type(res))
    res = ReadConfig('config.conf').get_value('Section', 'c')
    print(res, type(res))
    res = ReadConfig('config.conf').get_value('Section', 'd')
    print(res, type(res))