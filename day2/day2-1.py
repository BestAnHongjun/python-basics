# "()+()"
# z = f(x, y)
if __name__ == "__main__":
    # 一、算数运算符
    # 加法运算
    a = 1
    b = 1
    c = a + b
    # 整型+整型=整型
    print(c)
    print(type(c))
    # 整型+浮点型=浮点型
    a = 1
    b = 1.
    c = a + b
    print(c)
    print(type(c))
    # 浮点型+浮点型=浮点型
    a = 1.0
    b = 2.0
    c = a + b
    print(c)
    print(type(c))
    # 减法
    # 乘法
    # *
    c = 1.0 * 2.0
    print(c)
    print(type(c))
    # 除法：浮点数 attention：跟C不一样
    # float a = 8 / 3.0;
    a = 8
    b = 3
    c = a / b
    print(c)
    print(type(c))
    # 取余
    a = 8
    b = 5
    c = a % b #8 / 5 = 1……3
    print(c)
    print(type(c))
    # 整除
    a = 8
    b = 3
    c = a // b
    print(c)
    print(type(c))
    # 幂运算
    # c = a^b;
    a = 3
    b = 4
    c = a ** b
    print(c)
    print(type(c))
