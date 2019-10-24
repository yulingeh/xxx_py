import numpy as np
import cv2

'''
对称向量快速计算方法
需要给计算对称向量的函数，传入公共点法向量，光线向量
'''


def Symmetry_qk(light_vector, normal_vector):
    ba = light_vector
    L_ab = (ba[0] ** 2 + ba[1] ** 2 + ba[2] ** 2) ** 0.5
    N_V = np.array([normal_vector[0], normal_vector[1], normal_vector[2]], dtype=float)
    L_NV = (N_V[0] ** 2 + N_V[1] ** 2 + N_V[2] ** 2) ** 0.5
    cos_theta = -ba.dot(N_V) / (L_ab * L_NV)
    # 将法向量和光线向量归一化
    N_V[0] = N_V[0] / L_NV
    N_V[1] = N_V[1] / L_NV
    N_V[2] = N_V[2] / L_NV
    ba[0] = ba[0] / L_ab
    ba[1] = ba[1] / L_ab
    ba[2] = ba[2] / L_ab
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
    # ac向量
    ac = np.array([0, 0, 0], dtype=float)

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
    ac[0] = 2 * cos_theta * N_V[0] + ba[0]
    ac[1] = 2 * cos_theta * N_V[1] + ba[1]
    ac[2] = 2 * cos_theta * N_V[2] + ba[2]
    # end = cv2.getTickCount()  # 结束时间
    # t = '%.10f' % ((end - start) / cv2.getTickFrequency())  # 时间间隔除以周期，换算成秒为单位
    # print('\n方程计算时间： ' + t + 's')
    return ac


light = np.array([0, -1, -1], dtype=float)
normal = np.array([0, 0, 1], dtype=float)
Symmetry_qk(light, normal)
