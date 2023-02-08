# 逻辑运算符
if __name__ == "__main__":
    # 关系逻辑: 返回值一定是布尔型
    a = 1
    b = 2

    print(a == b) # 恒等判断
    print(type(a == b))
    print(a < b)
    print(a > b)
    print(a <= b)
    print(a >= b)
    print(a != b)

    # 数理逻辑
    # 逻辑与：当且仅当两者均为真时才为真
    print(True and True)
    print(True and False)
    print(False and True)
    print(False and False)
    a = 5
    print(a > 1 and a < 6)
    print(1 < a < 6)

    # 逻辑或：当且仅当两者均为假时才为假
    print(True or True)
    print(True or False)
    print(False or True)
    print(False or False)

    # 非：
    print(not True)
    print(not False)

    # 严格相等判断
    print(1 is 1.)
    print(1 is 1.0)
    print(1 is 1)

    # 附属关系
    a = [1, 2, 3]
    b = (1, 2, 3)
    print(1 in a)
    print(2 in b)
    print(70 in a)