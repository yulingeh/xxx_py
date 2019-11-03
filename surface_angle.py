import hole_module
import numpy as np
import math

'''
该函数负责找出"坑"上每一点面和x y平面构成的夹角
'''


def surface_angle():
    file = open("angle_xy.txt", 'a')

    matrix = [[0 for i in range(100)] for i in range(100)]
    X = hole_module.Normalvector_Cal("output.csv")
    for i in range(100):
        for j in range(100):
            X[i][j] = np.array(X[i][j])

    a = np.array([0, 0, 1])
    for i in range(38, 39):
        for j in range(47, 48):
            cache = X[52][39]
            cosangle = abs(a.dot(X[i][j])) / math.sqrt(X[i][j].dot(X[i][j]))

            # cos值转弧度值
            angle = math.acos(cosangle)
            # 弧度值转角度值
            angle = math.degrees(angle)
            matrix[i][j] = angle
            if 25 < angle < 35:
                file.write(str(i)+" ")
                file.write(str(j)+" ")
                file.write(str(angle)+"\n")
    # 找到角度最小值

    new_data = []

    for i in range(len(matrix)):
        new_data.append(max(matrix[i]))
    print("max angle: ", max(new_data))





surface_angle()
