import hole_module as h_m
import Symmetry_Vector as S_V
import numpy as np
from sympy import *
import cv2
import math
import symmetryvector_qk as s_q


def get_detectimage(phi):

    # 法向量计算运行时间起点记录
    start = cv2.getTickCount()

    # 获取"坑"洞每一点的法向量矩阵
    normalvector_matrix = h_m.Normalvector_Cal('./datafile/cr39_10_1.csv', img_size)

    end = cv2.getTickCount()  # 结束时间
    t = '%.5f' % ((end - start) / cv2.getTickFrequency())  # 时间间隔除以周期，换算成秒为单位
    print('坑洞法向量矩阵计算时间： ' + t + 's')
    theta = 0

    start = cv2.getTickCount()
    while theta < 360:
        cal_core(normalvector_matrix, theta, phi)
        theta = theta+10
    end = cv2.getTickCount()  # 结束时间
    t = '%.5f' % ((end - start) / cv2.getTickFrequency())  # 时间间隔除以周期，换算成秒为单位
    print('36个角度计算总耗时： ' + t + 's')


def cal_core(Normalvector_matrix, theta, phi):
    file = open("./imagelist30_5/image_list_" + str(theta) + ".txt", 'a')

    # z方向单位向量
    _001 = np.array([0, 0, 1])

    # 每个点的入射光线向量定义
    light = np.array([math.sin(math.pi * theta/180), -math.cos(math.pi * theta/180), -math.tan(math.pi * phi / 180)],
                     dtype=float)

    # 光线向量投影到xy平面
    light_xy = np.array([light[0], light[1], 0], dtype=float)

    # 运行时间起点记录
    start1 = cv2.getTickCount()

    count = 0  # 用于打印进度
    match_num = 0   # 用于记录有几个符合条件的点
    for i in range(0, img_size):
        for j in range(0, img_size):
            # 先考虑每个点法向量投影到x y平面的新向量
            # 与light_xy的夹角
            nv_xy = np.array([Normalvector_matrix[i][j][0], Normalvector_matrix[i][j][1], 0], dtype=float)
            if nv_xy.dot(light_xy) < 0:
                # 计算每个点的反射向量
                Ref_Vector = s_q.Symmetry_qk(light, Normalvector_matrix[i][j])

                # Ref_Vector = S_V.Symmetry_cal(light, i, j, hole[i][j],
                #                              Normalvector_matrix[i][j])  # i ,j传当前计算点x y坐标过去

                L_RefVector = (Ref_Vector[0]**2+Ref_Vector[1]**2+Ref_Vector[2]**2)**0.5
                # 每一个面点反射光线向量与（0，0，1）向量夹角cos值计算

                # 反射向量与法向量夹角cos值计算
                theta_R_001 = Ref_Vector[2] / L_RefVector

                if theta_R_001 > 0:
                    # cos值转弧度值
                    Radiantheta_R_001 = math.acos(theta_R_001)
                    # 弧度值转角度值
                    angletheta_R_001 = math.degrees(Radiantheta_R_001)

                    if angletheta_R_001 < 20:
                        file.write(str(i) + " " + str(j) + " "+"255" + "\n")   # 说明上方对应该点亮
                        match_num = match_num+1
                        continue
                    else:
                        file.write(str(i) + " " + str(j) + " " + "0" + "\n")   # 说明上方对应该点不亮
                        continue
            # 往文件中暂存信息
            file.write(str(i)+" "+str(j) + " " + "0" + "\n")       # 说明上方对应该点不亮

            # 刷新进度条
            count = count + 1
            print("\r角度"+str(theta)+"进度百分比：{0}%".format(round(100*count/65536, 2)), end=" ", flush=True)

    end1 = cv2.getTickCount()  # 结束时间
    t = '%.3f' % ((end1 - start1) / cv2.getTickFrequency())  # 时间间隔除以周期，换算成秒为单位
    print('\n探测图像'+str(theta)+'计算时间： ' + t + 's')
    # print("a : ", match_num)


# 图像尺度
img_size = 256
# 参数为fai角，即光线和x y平面的夹角
get_detectimage(70)