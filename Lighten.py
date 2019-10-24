import cv2
import numpy as np
from pic_nameget import get_filename




def Transparent(im1, im2, alpha):
    # python中使用addwighted混合图像
    img = cv2.addWeighted(im1, 0.5, im2, 0.5, 0)  # 两个权重值和一个gamma值
    cv2.imshow("img", img)
    cv2.imshow("im1", im1)
    cv2.waitKey(0)


'''
x1 x2 y1 y2参数是用来确定是否只对ROI区域执行变亮操作
'''


def Lighten_calculate(x1, x2, y1, y2):
    im1 = cv2.imread(read_dirpath + read_picname[0])
    # im1Gray = cv2.cvtColor(im1,cv2.COLOR_BGR2GRAY)
    # im2Gray = cv2.cvtColor(im2,cv2.COLOR_BGR2GRAY)

    im1size = im1.shape  # 获取图像height和width
    im1_copy = im1.copy()

    start = cv2.getTickCount()

    # 若x1,x2,y1,y2全部为0 ， 对整张图片实行变亮处理
    if 0 == x1 and 0 == x2 and 0 == y1 and 0 == y2:
        for a in range(1, 100):  # 100张图片循环
            im2 = cv2.imread(read_dirpath + read_picname[a])  # 读取待比较图片

            b2, g2, r2 = cv2.split(im2)  # 分离待比较图片通道
            b1, g1, r1 = cv2.split(im1_copy)  # 分离上一次变亮混合结果图片通道

            for i in range(im1size[0]):        # im1size[1] 代表长
                for j in range(im1size[1]):    # im1size[0] 代表款
                    if r2[i, j] > r1[i, j]:  # 用红通道做比较依据
                        im1_copy[i, j] = im2[i, j]
            print("\r-----picture" + str(a) + " finished-----", end=" ", flush=True)
    # 对ROI执行变亮处理
    else:
        for a in range(1, 100):  # 100张图片循环
            im2 = cv2.imread(read_dirpath + read_picname[a])  # 读取待比较图片

            b2, g2, r2 = cv2.split(im2)  # 分离待比较图片通道
            b1, g1, r1 = cv2.split(im1_copy)  # 分离上一次变亮混合结果图片通道

            for i in range(y1, y2):
                for j in range(x1, x2):
                    if r2[i, j] > r1[i, j]:
                        im1_copy[i, j] = im2[i, j]
            print("-----picture" + str(a) + " finished-----", end=" ", flush=True)

    end = cv2.getTickCount()  # 结束时间
    t = '%.5f' % ((end - start) / cv2.getTickFrequency())  # 时间间隔除以周期，换算成秒为单位
    print("\n变亮运行总计： "+str(t) + 's')

    cv2.imshow('lighten_result', im1_copy)
    cv2.imwrite("D:/xxx/Lighten_result/Lighten_result.jpg", im1_copy)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

read_dirpath = 'D:/xxx/result_pic/'
# 获取文件下所有图像按顺序排好的名字
read_picname = []
read_picname = get_filename(read_dirpath, '.jpg')
Lighten_calculate(0, 0, 0, 0,)
