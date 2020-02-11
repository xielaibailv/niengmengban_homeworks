class MathMethod:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):  # 加法
        res = self.a + self.b
        return res

    def sub(self):  # 减法
        res = self.a - self.b
        return res

    def a_b_s(self):  # 计算两个值差的绝对值
        res = abs(self.a - self.b)
        return res




if __name__ == "__main__":
    r = MathMethod(2, 3)
    print(r.add())
    print(r.sub())
    print(r.a_b_s())
