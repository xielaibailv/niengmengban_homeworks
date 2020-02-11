import unittest
from p2p_taobao.e_business_taobao import TaoBao


class TestMethod(unittest.TestCase):

    def test_login_success(self):
        login_result = TaoBao("淘宝").login_tb()
        try:
            self.assertFalse(login_result)
        except Exception as e:
            print("断言失败：%s" %e)
            raise e


