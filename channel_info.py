import PIL.Image as Image
import matplotlib.pyplot as plt
import cv2
#画出各个通道的灰度图
def channel_show(channel,im):
    b,g,r = im.split()
    if (channel == 'r' or channel == 'R'):
        plt.imshow(r,cmap = 'gray')
    elif (channel == 'g' or channel == 'G'):
        plt.imshow(g,cmap = 'gray')
    elif (channel == 'B' or channel == 'b'):
        plt.imshow(b,cmap ='gray')
    else:
        print("error")
    plt.show()
#输出通道信息的细节
def output_detail(width,height,im_matrix,num,channel):
    filename = channel+'_channel.txt'
    i = 0
    for i in range(width):
        j = 0
        for j in range(height):
            with open(filename, 'a')as file:
                file.write(str(i) + "," + str(j) + "," + str(im_matrix[i, j, num]) + "\n")
                j = j + 1
        i = i + 1
#通道信息输出
def channel_dataoutput(width,height,im_matrix,channel):
    if (channel == 'r' or channel == 'R'):
        num = 0
        output_detail(width,height,im_matrix,num,channel)
    elif(channel == 'g' or channel == 'G'):
        num = 1
        output_detail(width, height, im_matrix, num, channel)
    elif (channel == 'b' or channel == 'B'):
        num = 2
        output_detail(width, height, im_matrix, num, channel)
    else:
        print("error")
'''
im = cv2.imread('test.jpg')
b,g,r = cv2.split(im)
cv2.imshow("red",r)
print(r)
cv2.waitKey(0)
'''