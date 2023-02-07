# Day 1：Python变量与数据类型
## 一、Python变量
### 1.感性认识Python变量
编程语言的变量与数学意义的变量有一定区别。
* 数学意义的变量：也叫未知数，是一个抽象概念。通常在代数式中指代不确定的数，比如方程y=kx+b;
* 编程语言的变量：更像是一个“容器”，是一种实体概念。当一个变量存在时，在计算机硬件层面，一定有一个真实存在的物理空间与其对应。比如一段简单的python程序：

```python
a = 5
b = 7
```

* 当这一指令执行时，计算机会在内存中开辟两块内存空间，分别命名为a和b，用于存储数据5和7。

> **说人话环节**：对于非计算机专业的同学，这可能难以理解。简单来说， 现代计算机上都装有一个非常重要的部件，叫做“内存”。我们将其比作一个“酒店”，“酒店”中有许多独立的“客房”，“客房”里住着数据。上面的例程，就是开了两个房，房号是a和b，分别住了一位客人“5”和“7”。

### 2.标识符及其命名规范
为了区分不同的内存空间，我们为其设定一个指代的变量名称，称为“标识符”。其命名有一定规则，总结如下：
* 仅可以使用字符、数字和下划线"_"；
* 不允许数字开头；
* 不允许与关键字冲突。
> **友情提示**：\
> 字符可以使用英文字符（区分大小写），和中文字符；\
> 下划线是唯一可以使用的特殊字符；（怎么打出来？【“shift”+“-”】）\
> 中文标识符仅Python 3.x支持\
> 关键字：if、else、while等，不需要死记硬背，多用自然熟。使用IDE，关键字会自动变色。

[[例程day1-1.py]](day1-1.py)
* 举例：
```python
# 英文字符作标识符
a = 5
print(a)
```
**output**:\
5

```python
# 中文字符作标识符
圆周率 = 3.1415926
print(圆周率)
```
**output**:\
3.1415926

```python
# 使用字符、数字、下划线作标识符
a1 = 1
a_1 = 2
呵呵_1= 3
print(a1)
print(a_1)
print(呵呵_1)
```
**output**:\
1\
2\
3

```python
# 不允许使用数字开头
1a = 5
```
**output**:\
SyntaxError: invalid syntax

```python
# 不允许使用关键字作标识符
while = 5
```
**output**:\
SyntaxError: invalid syntax

## 二、Python数据类型
酒店中有不同类型的客房，比如单人间、双人间、三人间……不同类型的房间的面积、基础设施是不同的。\
变量也有不同的数据类型。不同的数据类型会用不同大小的内存单元进行存储。\
具体的数据类型，可以用type(*)函数查看。
### 1.基础数据类型
#### （1）整数型
* 也叫做int型，integer的缩写
* 可以用来存储整数
* 与C语言不同，理论上只要电脑内存足够大，可存储的整数范围是无限的

[[例程day1-2.py]](day1-2.py)
##### 举例：
```python
print(type(5))
```
**output**:\
int
```python
a = 10
print(type(a))
```
**output**:\
<class 'int'>

```python
a = 467476786827356283482323462386452358123424
print(type(a))
```
**output**:\
<class 'int'>

#### （2）实数型
* 英文名称“float”，用以形象地描述可以“漂浮”的小数点，所以也叫“浮点型”；
* 对于浮点型，是有一定范围和精度局限的。但对于不是从事专门数据计算的人员来说，暂时认为是无穷大的。

[[例程day1-3.py]](day1-3.py)
##### 举例：
```python
a = 3.14
print(type(a))
```
**output**:\
<class 'float'>

```python
a = 1.
print(a)
print(type(a))
```
**output**:\
1.0\
<class 'float'>

> **友情提示**：\
> "1"和"1.","1.0"在数值上是相等的，具体表现在做逻辑运算的时候，可以判定为相等。
```python
print(1 == 1.)
print(1 == 1.0)
```
**output**:\
True\
True

> 但是，"1","1.","1.0"并**不完全相等**，因为数据类型不一致，具体体现在利用is运算符作判定时，结果不一致。
```python
print(1 is 1.0)
print(1 is 1.)
```
**output**:\
False\
False

#### （3）布尔型
* 也叫”逻辑型“，英文名称bool
* 非真即假，要么是True，要么是False，注意首字母大写

[[例程day1-4.py]](day1-4.py)
##### 举例：
```python
type(True)
```
**output**:\
<class 'bool'>

```python
a = False
print(type(a))
```
**output**:\
<class 'bool'>

#### （4）字符串型
* 暂且理解为”文本型“吧。
* 英文名称为string。
* 可以用一对单引号，或双引号来声明。

[[例程day1-5.py]](day1-5.py)
##### 举例：
```python
s1 = "abcdefg"
s2 = 'abccdef'
s3 = "sadhfis说的话覅沙发sdfa"
print(s1)
print(s2)
print(s3)
```
**output**:\
abcdefg\
abccdef\
sadhfis说的话覅沙发sdfa

##### 格式化字符串：
```python
a = 5
b = 6
s1 = "a={},b={}".format(a, b)
a += 1
s2 = "a={},b={}".format(a, b)
```
**output**:\
a=5,b=6\
a=6,b=6


### 2.高级数据类型
#### （1）列表
* 英文名称list
* 是一个可以用来存放一些列”项“的容器，每一项也可以叫做一个”元素“
* Python并不要求所有元素的数据类型保持一致（与C语言数组不同）

[[例程day1-6.py]](day1-6.py)
##### a.创建一个列表
* 列表通常使用一对方括号[]来创建
```python
# 声明一个全是整数的列表
a = [1, 2, 3, 4] # 每一项之间用英文逗号隔开
print(a)
```
**output**:\
[1, 2, 3, 4]

```python
# 声明全是浮点数的列表：
a = [1., 2.0, 3.5, 4.789, 5.]
print(a)
```
**output**:\
[1., 2.0, 3.5, 4.789, 5.]

```python
# Python不要求所有元素类型保持一致
a = [1, 2.0, "sdjfhkasdhf", True]
print(a)
```
**output**:\
[1, 2.0, "sdjfhkasdhf", True]

```python
# 列表可以嵌套
a = [1, 2.0, ["dsafsf", 1., [2]]]
print(a)
```
**output**:\
[1, 2.0, ["dsafsf", 1., [2]]]

##### b.取出列表元素
* 列表中每一个元素，都有一个序号，学名”索引“。
* 与日常习惯不同，索引从0开始计数。
```python
# 创建一个列表
a = [1, 3, 4]

# 取出元素并打印
print(a[0])
print(a[2])
```
**output**:\
1\
4

```python
print(a[3]) # 超出索引，会报错
```
**output**:\
IndexError: list index out of range

```python
print(a[-1]) # 取出倒数第一个元素，并打印
print(a[-3]) # 取出倒数第三个元素，并打印
```
**output**:\
4\
1

```python
print(a[-4]) # 超出索引
```
**output**:\
IndexError: list index out of range

##### c.列表切片
* 可以使用切片的方法，取出列表中连续的某几个元素
```python
a = [1, 2, 3, 4, 5, 6, 7]

# 取出第0个到第2个元素
print(a[0:3]) # 索引用冒号隔开，冒号左边是起始索引，右边为终止索引，区间左闭右开
```
**output**:\
[1, 2, 3]

```python
# 取出第3个，到倒数第一个
print(a[3:-1])
```
**output**:\
[4, 5, 6]

```python
print(a[3:])
```
**output**:\
[4, 5, 6, 7]

```python
# 取出第1个到第5个，每隔2个取一个
print(a[1:5:2]) # 两个冒号隔开三个数，第一个是起始索引，第二个是终止索引，第三个是步长。
```
**output**:\
[2, 4]

```python
# 嵌套列表如何取出元素？
b = [1, 2, [4, 5, [6]]]
print(a[2])
print(a[2][2])
print(a[2][2][0])
```
**output**:\
[4, 5, [6]]\
[6]\
6

##### d.向列表最后追加元素
* 使用append方法
```python
a = [3, 4]
print(a)
a.append(6)
print(a)
```
**output**:\
[3, 4]\
[3, 4, 6]

##### e.删除列表中的元素
* 使用del方法
```python
a = [3, 4, 5]
print(a)
del a[1]
print(a)
```
**output**:\
[3, 4, 5]\
[3, 5]

##### f.修改指定索引文件
```python
a = [1, 2, 3]
print(a)
a[1] = 5
print(a)
```
**output**:\
[1, 2, 3]\
[1, 5, 3]

##### g.列表排序
```python
a = [1, 3, 1, 9, 5, 6]
a.sort()
print(a)
```
**output**:\
[1, 1, 3, 5, 6, 9]

```python
a.sort(reversed=True)
print(a)
```
**output**:\
[9, 6, 5, 3, 1, 1]

##### h.向列表中插入数据
* 使用insert方法
```python
a = [0, 4, 6, 8]
a.insert(1, 99)
print(a)
```
**output**:\
[0, 99, 4, 6, 8]

#### （2）元组
* 英文名称tuple
* 原组合列表非常相似，不要求所有元素保持一致

[[例程day1-7.py]](day1-7.py)
##### a.声明一个元组
* 用一对圆括号声明
```python
a = (3, 4, 5)
print(a)
```
**output**:\
(3, 4, 5)

##### b.元组和列表的相同点
* 可用相似的方法，利用索引取出元素、切片
```python
a = (3, 4, 5)
print(a[0])
print(a[-1])
print(a[0:2])
```
**output**:\
3\
5\
(3, 4)

##### c.元组和列表使用上的区别
* 元组一旦创建，其元素值不能被修改
```python
a = (3, 4, 6, 8)
a[2] = 88
```
**output**:\
TypeError: 'tuple' object does not support item assignment

#### （3）字典
* 英文名称dict

[[例程day1-8.py]](day1-8.py)
##### a.创建字典
* 可用用一对花括号创建
```python
a = {}
print(a)
print(type(a))
```
**output**:\
{}\
dict

* 也可用用dict方法
```python
a = dict()
print(a)
print(type(a))
```
**output**:\
{}
dict

##### b.添加元素
* 直接采用索引赋值的方式。字典与列表的不同是，**支持字符串索引**。
```python
a = dict()
a[1] = 9
a["haha"] = 789
print(a)
```
**output**:\
{1:9, "haha":789}

##### c.删除字典元素
* 使用del方法
```python
a = dict()
a[9] = 78
a["aaaaa"] = "bcd"
print(a)
del a[9]
print(a)
```
**output**:\
{9:78, "aaaaa":"bcd"}

#### （4）集合
* 英文名称set
* 集合类型也和列表非常相似，但一个集合中，不允许出现相同的元素

[[例程day1-9.py]](day1-9.py)
##### a.创建集合
* 使用set方法
```python
a = set()
print(a)
print(type(a))
```
**output**:\
set()\
set 

##### b.向集合中添加元素
* 使用add方法
```python
a = set()
a.add("asdfa")
a.add(5)
a.add(5)
print(a)
```
**output**:\
{"asdfa", 5}

##### c.添加多个元素
* 使用update方法
```python
a = set()
a.update((6, 7, 8))
print(a)
```
**output**:\
{6, 7, 8}

##### d.从集合中移除元素
* 使用remove方法
```python
a = set()
a.add("asdfa")
a.add(5)
a.add(5)
a.remove("asdfa")
print(a)
```
**output**:\
{5}

##### e.清空集合
* 使用clear方法
```python
a.clear()
print(a)
```
**output**:\
{}
