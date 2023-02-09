import numpy as np

if __name__ == "__main__":
    a = np.array([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [10, 11, 12]
    ])

    b = np.array([
        [23, 8, 0],
        [14, 5, 7],
        [11, 9, 10]
    ])

    print(a)
    print(a.shape)
    print(b)
    print(b.shape)

    print(a + a)
    print(a - a)
    print(a * a)
    print(a / a)

    c = np.power(a, 3)
    print(c)

    print(a.shape)
    print(b.shape)
    c = a @ b
    d = np.dot(a, b)
    print(c)
    print(d)

    c = np.linalg.inv(b)
    print(c)