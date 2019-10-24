import numpy as np

'''
封装向量叉乘函数
'''


def array_crossing(array_a, array_b):
    array_result = np.array([0,0,0], dtype=np.float)
    array_result[0] = array_a[1] * array_b[2] - array_b[1] * array_a[2]
    array_result[1] = array_a[2] * array_b[0] - array_a[0] * array_b[2]
    array_result[2] = array_a[0] * array_b[1] - array_b[0] * array_a[1]
    #print (array_result[1])
    return array_result

if __name__ == "main":
    a = np.array([1, 0, -0.00005])

    b = np.array([0, 1, -0.0092])

    c = array_crossing(a, b)
    print(c[1])

