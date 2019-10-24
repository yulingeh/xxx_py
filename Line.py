import numpy as np
from sympy import *

'''
线段对象 同时有函数可以返回对称向量上的对称点
'''


class Line():
    # vector参数是所求线段的，dot参数是面与法向量的交点
    def __init__(self, vector_x, vector_y, vector_z, dot_x, dot_y, dot_z):
        self.vector_x = vector_x
        self.vector_y = vector_y
        self.vector_z = vector_z
        self.dot_x = dot_x
        self.dot_y = dot_y
        self.dot_z = dot_z
        # 提前设置符号，可以代表未知数
        self.line_x = Symbol('line_x', real=True)  # 指定表示实数
        self.line_y = Symbol('line_y', real=True)
        self.line_z = Symbol('line_z', real=True)
        '''
        过A点 且方向为ab（光向量的反方向）的直线方程表示
        按照标准式，可以有三组方程确立x，y，z坐标关系
        首先考虑3种特殊情况（标准式有一个分母为0）
        '''

        if self.vector_x == 0:
            self.line_x = 0
            self.line_y = ((self.vector_y / self.vector_z)
                           * (self.line_z - self.dot_z) + self.dot_y)
            self.line_z = ((self.vector_z / self.vector_y)
                           * (self.line_y - self.dot_y) + self.dot_z)
        elif self.vector_y == 0:
            self.line_y = 0
            self.line_x = ((self.vector_x / self.vector_z)
                           * (self.line_z - self.dot_z) + self.dot_x)
            self.line_z = ((self.vector_z / self.vector_x)
                           * (self.line_x - self.dot_x) + self.dot_z)
        elif self.vector_z == 0:
            self.line_z = 0
            self.line_x = ((self.vector_x / self.vector_y)
                           * (self.line_y - self.dot_y) + self.dot_x)
            self.line_y = ((self.vector_y / self.vector_x)
                           * (self.line_x - self.dot_x) + self.dot_y)
        else:
            self.line_x = ((self.vector_x / self.vector_y)
                           * (self.line_y - self.dot_y) + self.dot_x)

            self.line_y = ((self.vector_y / self.vector_z)
                           * (self.line_z - self.dot_z) + self.dot_y)
            self.line_z = ((self.vector_z / self.vector_x)
                           * (self.line_x - self.dot_x) + self.dot_z)

    # 找对称点
    def dot_choose(self, dx, dy, i, j):
        if self.vector_x == 0:
            self.line_x = i
            self.line_y = dy
            self.line_z = ((self.vector_z / self.vector_y)
                           * (self.line_y - self.dot_y) + self.dot_z)
        elif self.vector_y == 0:
            self.line_x = dx
            self.line_y = j
            self.line_z = ((self.vector_z / self.vector_x)
                           * (self.line_x - self.dot_x) + self.dot_z)

        # elif self.vector_z == 0:
        #    self.line_x = dx
        #    self.line_y = dy
        #    self.line_z = 0
        else:
            self.line_x = dx
            self.line_y = dy
            self.line_z = ((self.vector_z / self.vector_x)
                           * (self.line_x - self.dot_x) + self.dot_z)

        new_dot = [self.line_x, self.line_y, self.line_z]
        # print("B:",new_dot)
        return (new_dot)


if __name__ == "main":
    x = Symbol("xx")
    print(x.is_real)
    test = Line(0, 1, 1, 0, 0, 0)
    test.dot_choose(0, 1)
