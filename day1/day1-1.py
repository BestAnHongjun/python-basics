# 整数型
# 实数型
# 布尔型
# 字符串型


if __name__ == "__main__":
    # 整数型int
    a = 5
    print(type(a))

    print(type(10))

    # 实数型float，浮点型
    a = 3.14
    print(type(a))

    a = 1.
    print(a)
    print(type(a))

    print(1 == 1.)
    print(1 == 1.0)
    print(1 is 1.)
    print(1 is 1.0)

    # 布尔型bool
    # True
    # False
    print(type(True))
    print(type(False))

    # 字符串型string
    a = "dsakfh683648hsduifyhsdi"
    b = 'fsdlfhjoiasf237947239'
    print(a)
    print(b)

    a = 1
    b = 2
    print("a={} b={}".format(a, b))
    a += 1
    b += 1
    print("a={} b={}".format(a, b))
