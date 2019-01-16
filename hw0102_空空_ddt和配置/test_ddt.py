# DDT的用法
import unittest
from ddt import ddt,data,unpack
from hw0102_空空_ddt和配置.configuration import ReadConfig

# 获取配置文件里的值
res = eval(ReadConfig('config.conf').get_value('Section', 'b'))
# 创建测试类
@ddt
class TestMethod(unittest.TestCase):

    @data(*res)   #脱一层外套
    # @unpack   # 再脱一层
    def test_001(self,t):
        print('开始打印参数')
        print(t)
