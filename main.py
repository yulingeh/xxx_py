import cv2
import PIL.Image as Image
import numpy as np
import channel_info
import os
from pic_nameget import get_filename
from pic_match import pic_match


#原始图像存储的文件路径
read_dirpath = '/Users/hedidi/PycharmProjects/xxx/raw_pic/'
#对齐加裁剪图片保存路径
MATCHsave_dirpath = '/Users/hedidi/PycharmProjects/xxx/result_pic/'


# 获取文件下所有图像按顺序排好的名字
read_picname = []
read_picname = get_filename(read_dirpath,'.jpg')
# 确定标准图像为第一幅
im_base = cv2.imread(read_dirpath+read_picname[0])

def PIC_MATCH():
    # 将第一幅图像存到save文件夹中
    crop_flag = int(input("pic_match mode,crop or not?1/0"))
    if crop_flag:
        im_base_croped = im_base[10:470,10:630]
        cv2.imwrite(MATCHsave_dirpath+read_picname[0],im_base_croped)
    else:
        cv2.imwrite(MATCHsave_dirpath+read_picname[0],im_base)

    #图片配准程序运行时间记录起点
    start = cv2.getTickCount()

    for i in range(1,100):
        im2 = cv2.imread(read_dirpath+read_picname[i])
        pic_match(im_base,im2,MATCHsave_dirpath+read_picname[i],i,crop_flag)

    end = cv2.getTickCount()         #结束时间
    t='%.10f'%((end-start)/cv2.getTickFrequency()) #时间间隔除以周期，换算成秒为单位
    print("图片配准运行总计： "+t+'s')

PIC_MATCH()









'''
for i in range(2,4):
#调用对齐模块，返回的result为img2对齐后移动的图像
    read_path = '/Users/hedidi/PycharmProjects/xxx/raw_pic/'+'test'+str(i)+'.jpg'
    save_path = '/Users/hedidi/PycharmProjects/xxx/result_pic/'+'test'+str(i)+'.jpg'
    img2 = cv2.imread(read_path)
    result,_,_ = SF.siftImageAlignment(img1,img2)
    cv2.imwrite(save_path,result)
    image_list.append(result)
拼接数组用于显示，axis=1横向拼接
allImg = np.concatenate((img1,img2,result),axis=1)
cv2.namedWindow('Result',cv2.WINDOW_NORMAL)
cv2.imshow('Result',allImg)

cv2.imshow('result',result)

cv2.waitKey(0)

allImg = np.concatenate((img1,image_list[0],image_list[1]),axis=1)
cv2.imshow('result',allImg)
cv2.waitKey(0)
'''