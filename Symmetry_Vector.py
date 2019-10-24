from sympy import *
import numpy as np
from Line import Line
from array_crossing import array_crossing
import math
from hole_module import positive
'''
需要给计算对称向量的函数，传入公共点坐标，光线向量
'''


def Symmetry_cal(Vector_Light, Intersec_x, Intersec_y, Intersec_z, Normal_vector):
    # 光线和面交点
    A = np.array([Intersec_x, Intersec_y, Intersec_z])

    ab = Vector_Light
    L_ab = math.sqrt(ab[0]**2 + ab[1]**2 + ab[2]**2)
    N_V = np.array([Normal_vector[0], Normal_vector[1], Normal_vector[2]])
    L_NV = math.sqrt(N_V[0] ** 2 + N_V[1] ** 2 + N_V[2] ** 2)
    '''
    #向量长度计算 一维向量dot()是点乘 高维向量是矩阵乘法
    L_ab = np.sqrt(ab.dot(ab))
    L_Normal_vector = np.sqrt(N_V.dot(N_V))
    #ab向量与法向量夹角cos值计算
    theta_ab_n = (ab.dot(N_V)) / (L_ab * L_Normal_vector)
    #cos值转弧度值
    Radiantheta_ab_n = np.arccos(theta_ab_n)
    #弧度值转角度值
    angletheta_ab_n = Radiantheta_ab_n*360 /(2*np.pi)
    '''

    test = Line(Vector_Light[0], Vector_Light[1], Vector_Light[2],
                Intersec_x, Intersec_y, Intersec_z)
    # 前两个参数是对应dx ，dy 后两个参数对应i ， j
    B = test.dot_choose(Intersec_x + 1, Intersec_y + 1,
                        Intersec_x, Intersec_y)

    # 指定表示B关于法向量的对称点的向量C 的未知数
    x1 = Symbol('x1', real=True)  # 指定表示实数
    y1 = Symbol('y1', real=True)
    z1 = Symbol('z1', real=True)
    # C点和ac向量
    C = np.array([x1, y1, z1])
    ac = np.array([x1 - A[0], y1 - A[1], z1 - A[2]])
    bc = np.array([x1 - B[0], y1 - B[1], z1 - B[2]])
    ab2 = np.array([B[0] - A[0], B[1] - A[1], B[2] - A[2]])

    # 求ab向量和法向量的叉乘
    ab_Nomal_crossing = array_crossing(ab, N_V)

    c1 = np.array([])
    c2 = np.array([])
    '''
    检查信息的输出
    print("A:", A)
    print("ac:", ac)
    print("bc:", bc)
    print("N-v:", N_V)
    print("ab2:", ab2)
    print("ab_Normal_crossing:", ab_Nomal_crossing)
    print("方程1：", ab_Nomal_crossing.dot(ac))
    print("方程2：", bc.dot(N_V))
    print("方程3：", (ac[0] ** 2 + ac[1] ** 2 + ac[2] ** 2) ** 0.5 - (ab2[0] ** 2 + ab2[1] ** 2 + ab2[2] ** 2) ** 0.5)
    '''

    # start = cv2.getTickCount()
    c1, c2 = solve([ab_Nomal_crossing.dot(ac),  # 方程1 ac向量与上一步叉乘向量垂直
                    bc.dot(N_V),  # 方程2 bc与法向量垂直
                    (ac[0] ** 2 + ac[1] ** 2 + ac[2] ** 2) ** 0.5
                    - (ab2[0] ** 2 + ab2[1] ** 2 + ab2[2] ** 2) ** 0.5],  # 方程3 AB AC线段长度相等
                   [x1, y1, z1])
    # end = cv2.getTickCount()  # 结束时间
    # t = '%.3f' % ((end - start) / cv2.getTickFrequency())  # 时间间隔除以周期，换算成秒为单位
    # print('\n方程计算时间： ' + t + 's')

    '''
    除了排除算出一样的点,还需注意，某些方向(9点钟)来的光线入射到某些点时，
    dot_choose出的点在光线与面交点的延长线上，也就导致算出来的ac向量和理想条件是反的
    详细见2019/10/17日   笔记图
    因为只考虑坑洞的“内”面，所以坑洞面每一点的法向量必定朝上，这一步已经在hole_module中positive过
    '''

    c1 = np.array(c1)
    c2 = np.array(c2)
    c1[0] = round(c1[0], 6)
    c2[0] = round(c2[0], 6)
    c1[1] = round(c1[1], 6)
    c2[1] = round(c2[1], 6)
    c1[2] = round(c1[2], 6)
    c2[2] = round(c2[2], 6)

    if c1[0] == B[0] or c1[1] == B[1]:
        # 上一步把c点求出来了，则对称向量ac也就可以找到了
        ac = np.array([c2[0] - A[0], c2[1] - A[1], c2[2] - A[2]])
        ac = positive(ac)         # 按照物理意义取反
    else:
        ac = np.array([c1[0] - A[0], c1[1] - A[1], c1[2] - A[2]])  # 扔掉和ab向量相等的向量
        ac = positive(ac)
    '''
    print("A: ", A)
    print("B: ", B)
    print("ab2: ", ab2)
    print("c1: ", c1)
    print("c2: ", c2)
    print("ac", ac)
    print("N_V: ", N_V)
    '''
    return ac


if __name__ == "main":
    light = np.array([0, 1, -math.tan(math.pi * 30 / 180)])

    Symmetry_cal(light, 32, 52, -10.76,
                         [0.577, -0.216, 1])
