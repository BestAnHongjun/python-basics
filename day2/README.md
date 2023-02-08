# Day 2：Python运算符与程序结构
## 一、运算符
### 1.算术运算符
#### （1）加法运算
[[day2-1.py]](day2-1.py)
* 整数加整数，结果还是整数
```python
a = 1
b = 1
c = a + b
print(c)
print(type(c))
```
**output**:\
3\
<class 'int'>

* 整数加浮点数，结果是浮点数
```python
a = 1
b = 2.
c = a + b
print(c)
print(type(c))
```
**output**:\
3.0\
<class 'float'>

* 浮点数加浮点数，结果还是浮点数
```python
a = 1.
b = 2.
c = a + b
print(c)
print(type(c))
```
**output**:\
3.0\
<class 'float'>

#### （2）减法运算
* 整数减整数还是整数
```python
print(type(1-2))
```
**output**:\
<class 'int'>

* 整数与浮点数的减法是浮点数
```python
print(type(1-2.))
```
**output**:\
<class 'float'>

* 浮点数减浮点数还是浮点数
```python
print(type(1.-2.))
```
**output**:\
<class 'float'>

#### （3）乘法运算
```python
print(type(1 * 2))
print(type(1. * 2))
print(type(1. * 2.))
```
**output**:\
<class 'int'>\
<class 'float'>\
<class 'float'>

#### （4）除法运算
* 无论输入参数是整数还是浮点数，结果一律是浮点数
```python
a = 8
b = 3
print(a / b)
print(type(a / b))
```
**output**:\
2.6666666666666665\
<class 'float'>

* 除数不能是0
```python
a = 8 / 0
```
**output**:\
ZeroDivisionError: division by zero

#### （5）取余运算
* 要求被除数和除数都是整数，返回值也是整数
```python
a = 8
b = 3
c = a % b
print(c)
print(type(c))
```
**output**:\
2\
<class 'int'>

#### （6）整除运算
* 输入和输出都是整数
```python
a = 8
b = 6
c = a // b
print(c)
print(type(c))
```
**output**:\
1\
<class 'int'>

#### （7）幂运算
```python
a = 3
b = 4
c = a ** b # a^b
print(c)
print(type(c))
```
**output**:\
81\
<class 'int'>

### 2.逻辑运算符
* 逻辑运算符的返回值，均为布尔型

[[day2-2.py]](day2-2.py)
#### (1)关系逻辑
```python
a = 1
b = 2

print(a == b)
print(a < b)
print(a > b)
print(a <= b)
print(a >= b)
print(a != b)
```
**output**:\
False\
True\
False\
True\
False\
True

#### （2）数理逻辑
* 逻辑与，当且仅当两者均为真时才为真
```python
print(True and True)
print(True and False)
print(False and True)
print(False and False)
a = 5
print(a > 1 and a < 6)
print(1 < a < 6)
```
**output**:\
True\
False\
False\
False\
True\
True 

* 逻辑或，当且仅当两者均为假时才为假
```python
print(True or True)
print(True or False)
print(False or True)
print(False or False)
a = 5
print(a > 1 or a < 6)
```
**output**:\
True\
True\
True\
False\
True 

* 逻辑非，非假即真，非真即假
```python
print(not True)
print(not False)
```
**output**:\
False\
True

#### (3)严格相等判断
* 既要求数值相等，也要求数据类型一致
```python
print(1 is 1)
print(1 is 1.)
print(1 is 1.0)
```
**output**:\
True\
False\
False

#### （4）附属逻辑判断
```python
a = [1, 2, 3]
b = (1, 2, 3)
print(1 in a)
print(2 in b)
print(70 in a)
```
**output**:\
True\
True\
False

### 3.高级数据类型的运算

[[day2-3.py]](day2-3.py)
#### （1）列表可以相加
```python
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)
```
**output**:\
[1, 2, 3, 4, 5, 6]

#### （2）集合的交、并、补
```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a)
print(type(a))
print(b)
print(type(b))
```
**output**:\
{1, 2, 3, 4}\
<class 'set'>\
{3, 4, 5, 6}\
<class 'set'>

* 集合的交集
```python
c = a & b 
print(c)
```
**output**:\
{3, 4}

* 集合的并集
```python
c = a | b 
print(c)
```
**output**:\
{1, 2, 3, 4, 5, 6}

* 集合的补集
```python
c = a - b
print(c)
```
**output**:\
{1, 2}

## 二、程序结构
计算机程序一般具有三种结构
* 顺序结构
* 条件结构
* 循环结构

### 1.顺序结构
最常用的结构，即程序按照指令顺序逐条执行
[[day2-4.py]](day2-4.py)
```python
a = 1
b = 2
c = a + b
```

### 2.条件结构
可以控制程序流的走向
#### （1）单条件分支
```python
a = 1
if a > 1:
    print("haha")
print("end")
```
**output**:\
end 

#### （2）如果...否则...
```python
a = 2
if a > 1:
    print("大于")
else:
    print("小于等于")
print("end")
```
**output**:\
大于\
end

#### （3) 多条件分支
```python
a = 1
if a > 1:
    print("大于")
elif a == 1:
    print("等于")
else:
    print("小于")
print("end")
```
**output**:\
等于\
end

### 3.循环结构
#### （1）while语句
while语句是最基本的循环控制语句，基本格式为：
```python
while 条件表达式:
    语句1
    语句2
    ...
```
当条件表达式为真时，循环一直执行，或者结束。
> 例题：计算从1加到100
```python
i = 1
sum = 0
while i <= 100:
    sum += i
    i += 1
print(sum)
```
**output**:\
5050

#### （2）break子句
当执行break时，立即跳出当前层循环
```python
i = 0
sum = 0
while True:
    i += 1
    if i > 100:
        break
    sum += i
print(sum)
```

> 例题：输出小九九乘法表
```python
i = 1
while True:
    # i
    j = 1
    while True:
        # j
        print("{:1d}x{:1d}={:2d}".format(j, i, i * j), end=" ")
        j += 1
        if j > i:
            break 
    print("")
    i += 1
    if i > 9:
        break
```
**output**:\
1x1= 1\
1x2= 2 2x2= 4\
1x3= 3 2x3= 6 3x3= 9\
1x4= 4 2x4= 8 3x4=12 4x4=16\
1x5= 5 2x5=10 3x5=15 4x5=20 5x5=25\
1x6= 6 2x6=12 3x6=18 4x6=24 5x6=30 6x6=36\
1x7= 7 2x7=14 3x7=21 4x7=28 5x7=35 6x7=42 7x7=49\
1x8= 8 2x8=16 3x8=24 4x8=32 5x8=40 6x8=48 7x8=56 8x8=64\
1x9= 9 2x9=18 3x9=27 4x9=36 5x9=45 6x9=54 7x9=63 8x9=72 9x9=81

#### （3）continue子句
当执行continue子句时，程序会立刻结束本次循环，进入下一轮的循环判断并继续执行
> 例题：计算1+3+5+7+...+99
```python
i = 0
sum = 0
while True:
    i += 1
    if i > 100:
        break
    if i % 2 == 0:
        continue
    sum += i
print(sum)
```
**output**:\
2500

#### （4）for...in...语句
for...in...语句可以用来遍历列表和元组
```python
a = [1, 3, 9, 222]
for i in a:
    print(i)
```
**output**:\
1\
3\
9\
222

```python
a = (1, 7, 8, 22)
for i in a:
    print(i)
```
**output**:\
1\
7\
8\
22

#### （5）range函数
range函数可以返回一个“序列”，初学者暂时可以把他理解为一种类似列表或元组的东西。
```python
a = range(5)
print(type(a))
```
**output**:\
<class 'range'>

强制将其转换为列表，看看里面有什么
```python
b = list(a)
print(b)
```
**output**:\
[0, 1, 2, 3, 4]

下面正式介绍range函数：
* 单参数
  * range(end)
  * 返回一个[0, end)步长为1的序列
* 双参数
  * range(start, end)
  * 返回一个[start, end)步长为1的序列
* 三参数
  * range(start, end, step)
  * 返回一个[start, end)步长为step的序列
```python
a = range(5)
b = list(a)
print(b)

a = range(5, 9)
b = list(a)
print(b)

a = range(5, 47, 3)
b = list(a)
print(b)

a = range(10, 5, -2)
b = list(a)
print(b)
```
**output**:\
[0, 1, 2, 3, 4]\
[5, 6, 7, 8]\
[5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35, 38, 41, 44]\
[10, 8, 6]

* range经常与for...in...搭配使用，实现一些循环结构
> 例题：输出小九九
```python
for i in range(1, 10):
    for j in range(1, i + 1):
        print("{:1d}x{:1d}={:2d}".format(j, i, i * j), end=" ")
    print("")
```
**output**:\
1x1= 1\
1x2= 2 2x2= 4\
1x3= 3 2x3= 6 3x3= 9\
1x4= 4 2x4= 8 3x4=12 4x4=16\
1x5= 5 2x5=10 3x5=15 4x5=20 5x5=25\
1x6= 6 2x6=12 3x6=18 4x6=24 5x6=30 6x6=36\
1x7= 7 2x7=14 3x7=21 4x7=28 5x7=35 6x7=42 7x7=49\
1x8= 8 2x8=16 3x8=24 4x8=32 5x8=40 6x8=48 7x8=56 8x8=64\
1x9= 9 2x9=18 3x9=27 4x9=36 5x9=45 6x9=54 7x9=63 8x9=72 9x9=81
