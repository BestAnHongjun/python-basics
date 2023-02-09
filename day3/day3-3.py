import numpy as np
# 函数方法
# 面向对象 class

# ACM、蓝桥杯：《数据结构》、《算法分析与设计》

if __name__ == "__main__":
    # 创建矩阵
    a = np.array([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [10, 11, 12]
    ])

    b = np.array([
        [28, 8, 9],
        [14, 5, 7],
        [11, 9, 10]
    ])

    print(a)
    print(a.shape)
    print(b)
    print(b.shape)

    # 按元素加减乘除
    print(a + a)
    print(a - a)
    print(a * a)
    print(a / a)

    # 按元素幂运算
    c = np.power(a, 3)
    print(c)

    # 矩阵乘法
    c = a @ b
    d = np.dot(a, b)
    print(c)
    print(d)

    # 矩阵求逆
    e = np.linalg.inv(b)
    print(e)