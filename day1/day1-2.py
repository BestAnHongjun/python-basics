# 列表
# 元组
# 字典
# 集合

if __name__ == "__main__":
    # 列表 list
    # 1. 创建列表
    a = [1, 1.0, 2.0, True, "sdfbsjaf"]
    b = [1, 1.0, [True, "sdfb", [1]]]
    print(a)
    print(b)
    print(type(a))

    # 2.取出列表中的元素
    # 索引 index：从0开始计数
    b = a[0]
    c = a[2]
    print(b)
    print(c)

    # 反着取
    d = a[-1]
    print(d)

    # 嵌套列表取数：逐级取
    b = [1, 1.0, [True, "sdfb", [1]]]
    print("-------")
    print(b[2])
    print(b[2][2])
    print(b[2][2][0])

    # 3.列表切片
    a = [1, 2, 3, 4, 5, 6, 7]
    # 取出从第0个，到第2个元素
    print(a[0:2]) # 左闭右开[0, 2)
    # 取出从第3个，到导数第一个
    print(a[3:-1])
    print(a[3:])
    print(a[:3])
    # 取出从第1个，到第5个，每隔2个取一个
    print(a[1:5:2])
    print(a[-1:0:-2])

    # 4.向列表追加元素
    a = [1, 2, 3, 4, 5, 6, 7]
    print(a)
    a.append(8)
    print(a)

    # 5.删除列表中的元素
    del a[2]
    print(a)

    # 6.修改指定索引的数据
    a[3] = 99
    print(a)

    # 7.列表排序
    a = [78, 2, 1, 5, 78, 9]
    print(a)
    a.sort()
    print(a)
    a.sort(reverse=True)
    print(a)

    # 8.向列表插入元素
    a = [1, 2, 3, 4, 5, 6, 7]
    a.insert(2, 99)
    print(a)

