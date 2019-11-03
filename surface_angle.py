import hole_module
import numpy as np
import math

'''
该函数负责找出"坑"上每一点面和x y平面构成的夹角
'''


def surface_angle():
    file = open("angle_xy.txt", 'a')
    Max = 0
    Min = 90
    matrix = [[0 for i in range(256)] for i in range(256)]
    X = hole_module.Normalvector_Cal("cr39_20.csv")
    for i in range(256):
        for j in range(256):
            X[i][j] = np.array(X[i][j])

    a = np.array([0, 0, 1])
    for i in range(0, 256):
        for j in range(0, 256):
            cosangle = abs(a.dot(X[i][j])) / math.sqrt(X[i][j].dot(X[i][j]))
            # cos值转弧度值
            angle = math.acos(cosangle)
            # 弧度值转角度值
            angle = math.degrees(angle)
            matrix[i][j] = angle
            file.write(str(i)+" ")
            file.write(str(j)+" ")
            file.write(str(angle)+"\n")
            # 找到角度最小、大值
            if angle > Max:
                Max = angle
            if angle < Min:
                Min = angle
    print("max angle: ", Max)
    print("min angle: ", Min)

surface_angle()
