import cv2
import numpy as np
from pic_nameget import get_filename

'''对齐的运算内核'''


def pic_match(im1, im2, save_path_name, i, crop_flag):
    # Read the images to be aligned
    # im1 = cv2.imread("test.jpg");
    # im2 = cv2.imread("test2.jpg");

    # 图片实际编号比配准数多1
    i = i + 1

    # 运行时间起点记录
    start = cv2.getTickCount()

    # Convert images to grayscale
    im1_gray = cv2.cvtColor(im1, cv2.COLOR_BGR2GRAY)
    im2_gray = cv2.cvtColor(im2, cv2.COLOR_BGR2GRAY)

    # Find size of image1
    sz = im1.shape

    # Define the motion model
    warp_mode = cv2.MOTION_TRANSLATION

    # Define 2x3 or 3x3 matrices and initialize the matrix to identity
    if warp_mode == cv2.MOTION_HOMOGRAPHY:
        warp_matrix = np.eye(3, 3, dtype=np.float32)
    else:
        warp_matrix = np.eye(2, 3, dtype=np.float32)

    # Specify the number of iterations.
    number_of_iterations = 5000;

    # Specify the threshold of the increment
    # in the correlation coefficient between two iterations
    termination_eps = 1e-10;

    # Define termination criteria
    criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, number_of_iterations, termination_eps)

    # Run the ECC algorithm. The results are stored in warp_matrix.
    (cc, warp_matrix) = cv2.findTransformECC(im1_gray, im2_gray, warp_matrix, warp_mode, criteria)

    if warp_mode == cv2.MOTION_HOMOGRAPHY:
        # Use warpPerspective for Homography
        im2_aligned = cv2.warpPerspective(im2, warp_matrix, (sz[1], sz[0]),
                                          flags=cv2.INTER_LINEAR + cv2.WARP_INVERSE_MAP)
    else:
        # Use warpAffine for Translation, Euclidean and Affine
        im2_aligned = cv2.warpAffine(im2, warp_matrix, (sz[1], sz[0]), flags=cv2.INTER_LINEAR + cv2.WARP_INVERSE_MAP);

    # Show final results
    '''
    cv2.imshow("Image 1", im1)
    cv2.imshow("Image 2", im2)
    cv2.imshow("Aligned Image 2", im2_aligned)
    cv2.waitKey(0)
    '''
    end = cv2.getTickCount()  # 结束时间
    t = '%.10f' % ((end - start) / cv2.getTickFrequency())  # 时间间隔除以周期，换算成秒为单位
    print('图片' + str(i) + '配准运行时间： ' + t + 's')
    # save the aligend image
    top_size, bottom_size, left_size, right_size = (10, 10, 10, 10)
    # reflect = cv2.copyMakeBorder(im2_aligned, top_size, bottom_size, left_size, right_size,
    #                                borderType=cv2.BORDER_WRAP)

    # cv2.imwrite(save_path_name,reflect)
    if (crop_flag):
        # 上下左右各裁剪10像素
        im2_aligned_croped = im2_aligned[10:470, 10:630]
        cv2.imwrite(save_path_name, im2_aligned_croped)
    else:
        cv2.imwrite(save_path_name, im2_aligned)


'''
壳函数
'''


def PIC_MATCH():
    # 原始图像存储的文件路径
    read_dirpath = 'D:/xxx/raw_pic/'
    # 对齐加裁剪图片保存路径
    MATCHsave_dirpath = 'D:/xxx/result_pic/'

    # 获取文件下所有图像按顺序排好的名字
    read_picname = []
    read_picname = get_filename(read_dirpath, '.jpg')
    # 确定标准图像为第一幅
    im_base = cv2.imread(read_dirpath + read_picname[0])
    # 确定裁剪标志
    crop_flag = int(input("pic_match mode,crop or not?1/0"))
    # 先将第一幅基准图像存到save文件夹中
    if (crop_flag):
        im_base_croped = im_base[10:470, 10:630]
        cv2.imwrite(MATCHsave_dirpath + read_picname[0], im_base_croped)
    else:
        cv2.imwrite(MATCHsave_dirpath + read_picname[0], im_base)

    # 图片配准程序运行时间记录起点
    start = cv2.getTickCount()
    # 配齐剩下的图像
    for i in range(1, 100):
        im2 = cv2.imread(read_dirpath + read_picname[i])
        pic_match(im_base, im2, MATCHsave_dirpath + read_picname[i], i, crop_flag)

    end = cv2.getTickCount()  # 结束时间
    t = '%.10f' % ((end - start) / cv2.getTickFrequency())  # 时间间隔除以周期，换算成秒为单位
    print("图片配准运行总计： " + t + 's')


PIC_MATCH()
