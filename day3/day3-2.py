import pandas as pd

if __name__ == "__main__":
    # 读取excel文件DataFrame
    df = pd.read_excel("test.xlsx")
    print(df)
    print(df.shape)

    # 添加一列 insert
    df.insert(df.shape[1], "sum", 0)
    print(df)

    # 按行求和
    for i in range(df.shape[0]):
        df.loc[i, 'sum'] = df.loc[i, '语文'] + df.loc[i, '数学'] + df.loc[i, '英语']
    print(df)

    # 输出excel
    df.to_excel("test_out.xlsx")