if __name__ == "__main__":
    # 字典 dict
    # 1.创建一个字典
    a = {}
    print(a)
    print(type(a))
    a = dict()
    print(a)
    print(type(a))

    # 2.向字典添加元素
    # 直接采用索引赋值的形式
    # 字典：键值对的集合
    a[9] = 0
    a["fsaklfh"] = 78
    a["abcdef"] = 20
    print(a)

    # 3.从字典删除元素
    del a[9]
    print(a)