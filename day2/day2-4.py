# 程序结果
# 顺序结构，条件结构，循环结构

if __name__ == "__main__":
    # 单条件分支
    # a = 1
    # if a > 1:
    #     print("haha")
    # print("end")

    # 双条件：如果..否则..
    # a = 1
    # if a > 1:
    #     print("大于")
    # else:
    #     print("小于等于")
    # print("end")

    # 多条件
    # a = 1
    # if a > 1:
    #     print("大于")
    # elif a == 1:
    #     print("等于")
    # else:
    #     print("小于")
    # print("end")

    # 循环结构
    # while语句
    # while 条件表达式:
    #       jsdfkl....
    # 例题：计算从1加到100
    # i = 1
    # sum = 0
    # while i <= 100:
    #     sum += i # sum = sum + i
    #     i += 1
    # print(sum)
    # # break
    # i = 0
    # sum = 0
    # while True:
    #     i += 1
    #     if i > 100:
    #         break
    #     sum += i
    # print(sum)
    # # continue
    # # 例题：1+3+5+7+9+..+99
    i = 0
    sum = 0
    while True:
        i += 1
        if i > 99:
            break
        if i % 2 == 0:
            continue
        sum += i
    print(sum)
    # for..in..循环语句
    # 可以用来遍历列表和数组
    # a = [1, 3, 9, 22]
    # for i in a:
    #     print(i)
    # a = [1, 7, 8, 22]
    # for i in a:
    #     print(i)

    # range函数
    # range函数可以返回一个“序列”，初学者暂理解为一种类似列表或元组的东西
    a = range(5)
    print(type(a))
    b = list(a)
    print(b)
    # 单参数：
    #   range(end)
    #   返回一个[0, end)步长为1的序列
    # 双参数
    #   range(start, end)
    #   返回一个[start, end)步长为1的序列
    # 三参数
    #   range(start, end, step)
    #   返回一个[start, end)步长为step的序列
    # a = range(5, 9)
    # b = list(a)
    # print(b, end="\n")
    #
    # a = range(5, 47, 3)
    # b = list(a)
    # print(b)
    #
    # a = range(10, 5, -3)
    # b = list(a)
    # print(b)
    #
    # for i in range(5):
    #     print(i)

    # while循环：输出一个小九九
    # i = 1
    while True:
        j = 1
        while True:
            print("{:1d}x{:1d}={:2d}".format(j, i, i * j), end=" ")
            j += 1
            if j > i:
                break
        print("")
        i += 1
        if i > 9:
            break
    # 用for...in写
    for i in range(1, 10):
        for j in range(1, i + 1):
            print("{:1d}x{:1d}={:2d}".format(j, i, i * j), end=" ")
        print("")





