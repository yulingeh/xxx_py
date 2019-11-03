import matplotlib.pyplot as plt
import numpy as np


def save_show(filename, j):
    file = open(filename)
    a = [[0 for i in range(256)] for j in range(256)]
    a = np.array(a)
    for line in file.readlines():
        curLine = line.strip().split(" ")
        intLine = list(map(int, curLine))  # 这里使用的是map函数直接把数据转化成为int类型
        if intLine[2] == 255:
            a[intLine[0]][intLine[1]] = 255

    a = np.matrix(a)
    # 图片保存路径
    file_path_name = "./detect_image30_5/detect_image" + str(j) + ".png"
    # 直接保存图片，但是没有坐标轴
    # plt.imsave(file_path_name, a, cmap='gray')

    # get_cmap() 设置颜色渐变

    plt.imshow(a, plt.get_cmap('gray'))
    # 画图认定的x y轴和物理意义上的不同
    plt.xlabel('y')
    plt.ylabel('x')
    plt.title("detect_image " + str(j) + "°")
    plt.savefig(file_path_name, dpi=300)
    plt.show()


j = 0
while j < 360:
    save_show("./imagelist30_5/image_list_" + str(j) + ".txt", j)
    j = j + 10
