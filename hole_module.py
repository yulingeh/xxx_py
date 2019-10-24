import numpy as np
import csv
import pandas as pd
from array_crossing import array_crossing
import seaborn as sns

'''
获取"坑洞"模型原始数据
'''


def hole_module(filename):
    df = pd.read_csv(filename)  # 返回一个DataFrame的对象，这个是pandas的一个数据结构
    df.values
    Y = np.array(df, dtype=np.float)  # X矩阵，i，j代表位置，[i][j]值代表深度
    # 矩阵大小100 * 100
    return Y


'''
为了算出储存有每一个点的法向量的二维矩阵
'''


def Normalvector_Cal(filename):
    X = hole_module(filename)
    Normalvector_Matirx = lawarray()

    # 要用两个向量叉乘来算每一点的法向量
    # 关注点附近取的两个点都是上 右这样的简单关系
    # 两点组成的向量（x，y，z）的x，y值都只是差1，
    # （a1，b1,c1)代表第一个参考向量，x方向
    # （a2,b2,c2)代表第二个参考向量，y方向
    for i in range(100):
        a1 = 1  # 对应绝大多数情况，关注点和右边一点的x差值，见下方算c1
        b1 = 0  # 对应绝大多数情况，关注点和右边一点的y差值，见下方算c1
        a2 = 0
        b2 = 1
        # 统一用x方向叉乘y方向
        for j in range(100):
            if i < 99 and j < 99:  # 绝大多数点
                c1 = X[i][j + 1] - X[i][j]  # 右边的点构成的向量，算向量z值
                c2 = X[i + 1][j] - X[i][j]  # 下方的点构成的向量，算向量z值
                # 法向量坐标由a3,b3,c3表示  全部取反得到向"上"的向量
                '''
                a3 = (b1 * c2 - b2 * c1)
                b3 = (c1 * a2 - a1 * c2)
                c3 = (a1 * b2 - a2 * b1)
                Normalvector_Matirx[i][j] = [a3, b3, c3]
                '''
                a = np.array([0, 1, c1])
                b = np.array([1, 0, c2])
                Normalvector_Matirx[i][j][0] = (array_crossing(a, b))[0]
                Normalvector_Matirx[i][j][1] = (array_crossing(a, b))[1]
                Normalvector_Matirx[i][j][2] = (array_crossing(a, b))[2]
                # 不这样赋值，最后矩阵中每一项输出都带一个array，实际上只需要一个[]
                Normalvector_Matirx[i][j] = positive(Normalvector_Matirx[i][j])  # 检查是否是向上的向量，否则取反

            elif 99 == j and i < 99:
                # 最右方那一列
                c1 = X[i][j - 1] - X[i][j]
                c2 = X[i + 1][j] - X[i][j]
                # 法向量坐标由a3,b3,c3表示
                '''
                a1 = -1                     #因为边界，只能用左边的点
                a3 = b1 * c2 - b2 * c1
                b3 = c1 * a2 - a1 * c2
                c3 = a1 * b2 - a2 * b1
                Normalvector_Matirx[i][j] = [a3, b3, c3]
                '''
                a = np.array([0, -1, c1])
                b = np.array([1, 0, c2])
                Normalvector_Matirx[i][j][0] = (array_crossing(a, b))[0]
                Normalvector_Matirx[i][j][1] = (array_crossing(a, b))[1]
                Normalvector_Matirx[i][j][2] = (array_crossing(a, b))[2]
                Normalvector_Matirx[i][j] = positive(Normalvector_Matirx[i][j])

            elif 99 == i and j < 99:
                # 最下方那一行
                c1 = X[i][j + 1] - X[i][j]
                c2 = X[i - 1][j] - X[i][j]  # 最下方那一行
                '''
                b2 = -1                     #因为边界，只能用上方的点
                a3 = b1 * c2 - b2 * c1
                b3 = c1 * a2 - a1 * c2
                c3 = a1 * b2 - a2 * b1
                Normalvector_Matirx[i][j] = [a3, b3, c3]
                '''
                a = np.array([0, 1, c1])
                b = np.array([-1, 0, c2])
                Normalvector_Matirx[i][j][0] = (array_crossing(a, b))[0]
                Normalvector_Matirx[i][j][1] = (array_crossing(a, b))[1]
                Normalvector_Matirx[i][j][2] = (array_crossing(a, b))[2]
                Normalvector_Matirx[i][j] = positive(Normalvector_Matirx[i][j])

            elif 99 == i and 99 == j:
                c1 = X[i - 1][j] - X[i][j]
                c2 = X[i][j - 1] - X[i][j]  # 最右下角那一个格子
                '''
                b2 = -1
                a1 = -1
                a3 = (b1 * c2 - b2 * c1)
                b3 = (c1 * a2 - a1 * c2)
                c3 = (a1 * b2 - a2 * b1)
                Normalvector_Matirx[i][j] = [a3,b3,c3]
                '''
                a = np.array([0, -1, c1])
                b = np.array([-1, 0, c2])
                Normalvector_Matirx[i][j][0] = (array_crossing(a, b))[0]
                Normalvector_Matirx[i][j][1] = (array_crossing(a, b))[1]
                Normalvector_Matirx[i][j][2] = (array_crossing(a, b))[2]
                Normalvector_Matirx[i][j] = positive(Normalvector_Matirx[i][j])
    # print(Normalvector_Matirx[][])
    return Normalvector_Matirx


def lawarray():
    # 生产100x100矩阵，每个元素都是一个列表，用来存法向量坐标
    num_list = [[[0, 0, 0] for i in range(100)] for j in range(100)]
    return num_list


# 只是为了减少代码量
def positive(X):
    if X[2] < 0:
        X[0] = -X[0]
        X[1] = -X[1]
        X[2] = -X[2]
        return X
    else:
        return X


'''
把坑洞用热力图的形式画出来



def show_hole():
    Y = hole_module("output.csv")
    for i in range(100):
        for j in range(100):
            Y[i][j] = int(Y[i][j] + 100)
    sns.heatmap(Y, annot=True)

# Normalvector_Cal('output.csv')
# show_hole()
'''