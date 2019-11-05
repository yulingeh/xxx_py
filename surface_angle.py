import hole_module
import numpy as np
import math
import matplotlib.pyplot as plt
'''
该函数负责找出"坑"上每一点面和x y平面构成的夹角
'''
# 图像大小


def surface_angle():
    file = open("angle_xy.txt", 'a')
    f = [0 for i in range(900)]
    max_cache = 0
    min_cache = 90
   # matrix = [[0 for i in range(size)] for i in range(size)]
    X = hole_module.Normalvector_Cal("./datafile/cr39_20_1.csv")
    for i in range(size):
        for j in range(size):
            X[i][j] = np.array(X[i][j])

    a = np.array([0, 0, 1])
    for i in range(77, 180):
        for j in range(70, 160):
            cosangle = abs(a.dot(X[i][j])) / math.sqrt(X[i][j].dot(X[i][j]))
            # cos值转弧度值
            angle = math.acos(cosangle)
            # 弧度值转角度值
            angle = round(math.degrees(angle), 1)   # 保留小数点后一位
            # matrix[i][j] = angle
            f[int(angle*10)] += 1
            file.write(str(i)+" ")
            file.write(str(j)+" ")
            file.write(str(angle)+"\n")
            # 找到角度最小、大值
            if angle > max_cache:
                max_cache = angle
            if angle < min_cache:
                min_cache = angle
    print("max angle: ", max_cache)
    print("min angle: ", min_cache)

    # 作图
    max_cache = int(max_cache*10)
    f = np.array(f, dtype=int)
    x = range(0, 900)
    plt.plot(x, f)
    max_indx = np.argmax(f)  # 出现次数最多的角度
    plt.plot(max_indx, f[max_indx], 'ks')   # 画出出现次数最多的角度对应的点
    plt.plot(max_cache, f[max_cache], 'ks')    # 画出角度最大值对应的点
    show_max_indx = '[' + str(max_indx) + ']'
    show_max_value = '[' + str(max_cache) + ']'
    plt.annotate(show_max_indx, xytext=(max_indx, f[max_indx]), xy=(max_indx, f[max_indx]))  # 显示出现次数最多的点坐标
    plt.annotate(show_max_value, xytext=(max_cache, f[max_cache]), xy=(max_cache, f[max_cache]))  # 显示最大值对应点坐标

    plt.title("incident angle  20°")
    plt.ylabel("counts")
    plt.xlabel("surface angle of pit")
    plt.show()


size = 256
surface_angle()
