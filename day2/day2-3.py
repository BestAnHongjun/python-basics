# 高级数据类型之间的运算
if __name__ == "__main__":
    # 列表之间做加法运算
    a = [1, 2, 3]
    b = [4, 5, 6]
    c = a + b
    print(c)
    print(type(c))

    # 集合之间的交集、并集、补集
    a = {1, 2, 3, 4}
    b = {3, 4, 5, 6}

    c = a & b # 交集
    print(c)
    print(type(c))

    c = a | b # 并集
    print(c)
    print(type(c))

    c = a - b
    print(c)
    print(type(c))


