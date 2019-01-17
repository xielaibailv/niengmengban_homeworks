import logging
from hw0104_空空_配置and日志.config_file.read_case import ReadCase

# 自己改写日志系统
# 基本步骤就是创建日志收集器和输出渠道，分别指定级别，然后将两者对接

# 获取配置文件里的日志相关参数
file = '../config_file/case.ini'
name = ReadCase(file).get_value('LOG', 'name')
in_level = ReadCase(file).get_value('LOG', 'in_level')
out_level = ReadCase(file).get_value('LOG', 'out_level')
out_file_level = ReadCase(file).get_value('LOG', 'out_file_level')


class MyLog:

    def mylog(self, level, msg):

        # 创建一个日志收集器
        my_logger = logging.getLogger(name)
        # 给日志收集器指定收集的级别
        my_logger.setLevel(in_level)
        '''-------------------------------------------------'''

        # 输出格式
        # 格式化输出：asctime：系统时间；levelname：级别信息；
        # name：日志所在的文件名称；message：日志信息
        # 详见笔记[日志]
        formatter = logging.Formatter('%(asctime)s-'
                                      '[%(levelname)s]-'
                                      '[%(name)s]-'
                                      '[[line:]%(lineno)d]-'
                                      '[日志信息]:%(message)s')

        # 指定输出渠道-------输出到控制台
        ch = logging.StreamHandler()
        # 给日志输出渠道设置输出的级别
        ch.setLevel(out_level)
        ch.setFormatter(formatter)

        # 指定输出渠道-------输出到文件
        fh = logging.FileHandler('../test_result/test_log', mode='a',encoding='utf-8')
        # 给日志输出渠道设置输出的级别
        fh.setLevel(out_file_level)
        fh.setFormatter(formatter)
        '''---------------------------------------------------------'''

        # 日志收集器与输出渠道进行对接
        # my_logger.addHandler(ch)
        my_logger.addHandler(fh)

        if level == 'DEBUG':
            my_logger.debug(msg)
        elif level == 'INFO':
            my_logger.info(msg)
        elif level == 'ERROR':
            my_logger.error(msg)
        elif level == 'WARNING':
            my_logger.warning(msg)
        else:
            my_logger.critical(msg)

        # 每一次日志收集完毕后，记得要移除掉日志收集器
        my_logger.removeHandler(ch)
        my_logger.removeHandler(fh)

    def debug(self,msg):
        self.mylog('DEBUG',msg)

    def info(self,msg):
        self.mylog('INFO',msg)

    def warning(self,msg):
        self.mylog('WARNING',msg)

    def error(self,msg):
        self.mylog('ERROR',msg)

    def critical(self,msg):
        self.mylog('CRITICAL',msg)


if __name__ == '__main__':
    # MyLog().mylog('ERROR','error级别的错误日志')
    # 不过上面这样有点麻烦，我们还可以优化
    my_logger = MyLog()
    my_logger.debug('debug级别的日志')
