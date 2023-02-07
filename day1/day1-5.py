if __name__ == "__main__":
    # 集合 set
    a = set()
    print(a)
    print(type(a))

    # 向集合添加元素 add
    a.add("sdhfhsdjfkl")
    a.add(5)
    a.add(5)
    print(a)

    # 添加多个元素
    a.update((34, 234, "dfsjk"))
    print(a)

    # 移除元素
    a.remove(234)
    print(a)

    # 清空
    a.clear()
    print(a)
