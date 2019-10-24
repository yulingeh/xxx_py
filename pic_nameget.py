import cv2
import os


def get_filename(path,filetype):
    #运行时间起点记录
    start = cv2.getTickCount()
    name =[]
    final_name = []
    for root,dirs,files in os.walk(path):
        for i in files:
            if filetype in i:
                name.append(i)# 生成不带‘.jpg’后缀的文件名组成的列表
    name.sort()
    # for j in name:
    #    print(j)
    end = cv2.getTickCount()  # 结束时间
    t = '%.10f' % ((end - start) / cv2.getTickFrequency())  # 时间间隔除以周期，换算成秒为单位
    print("名字获取运行总计： " + t + 's')
    return name
    # final_name = [item +'.jpg' for item in name]#生成‘.jpg’后缀的文件名组成的列表
    # return final_name#输出由有‘.jpg’后缀的文件名组成的列表


if __name__ == '__main__':
    path = '/Users/hedidi/PycharmProjects/xxx/raw_pic/'# 指定文件所在路径
    filetype ='.jpg' # 指定文件类型
    get_filename(path,filetype)

