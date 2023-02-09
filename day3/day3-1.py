a = "sfhklsdfjasj1234\n"
# \n:换行符
# \t:缩进符号 tab

import pickle

# 文件操作
if __name__ == "__main__":
    # 读取文本文件
    # f = open("read_test.txt", "r")
    # data = f.read()
    # f.close()
    # print(data)

    # 读取一行
    # f = open("read_test.txt", "r")
    # data1 = f.readline()
    # data2 = f.readline()
    # data3 = f.readline()
    # data4 = f.readline()
    # f.close()
    # print(data1, end="")
    # print(data2, end="")
    # print(data3, end="")
    # print(data4, end="")

    # f = open("read_test.txt", "r")
    # data = f.readlines()
    # f.close()
    # print(data)

    # 写文本文件
    # f = open("write_test.txt", "w")
    # data = "abcdefg\nfhdksfkjsfks\n35672345723\njjj"
    # f.write(data)
    # f.close()

    a = [1234, 23423, 234234]
    f = open("obj_test.pkl", "wb")
    pickle.dump(a, f)
    f.close()

    f = open("obj_test.pkl", "rb")
    data = pickle.load(f)
    print(data)
    f.close()



