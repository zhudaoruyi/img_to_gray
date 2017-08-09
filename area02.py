import openslide
import matplotlib.pyplot as plt
from PIL import Image
from pylab import *
import numpy as np

# 读取包含有肿瘤区域的大图（全切片病理图像）
origin_images_path = "Tumor_005.tif"
origin_slide = openslide.open_slide(origin_images_path)

# 读取该肿瘤区域的标注图
annotation_images_path = "Tumor_005_Mask.tif"
mask_slide = openslide.open_slide(annotation_images_path)

# location = (0, 124700)
level = 6
# size = (1536, 210)

origin_size = origin_slide.dimensions
origin_widths = origin_size[0]
origin_heights = origin_size[1]

object_size = origin_slide.level_dimensions[level]
object_widths = int(object_size[0])
object_heights = object_size[1]
# color_mean = {}
color_aver = []
effec_num = []
color_std = []

for i in range(0,100):
    slide = origin_slide.read_region((0, i*origin_heights//100), level, (object_widths, object_heights//50))     # 循环顺序读取50高的区域
    img = slide.convert("L")      # 转为灰度图
    img1 = array(img)             # 转为像素矩阵
    # color_mean['a']=int(img1.mean())
    # a = round(img1.mean())
    color_aver.append(img1.mean())        # 将矩阵的像素值平均数作为数组记录下来
    color_std.append(img1.std())          # 将矩阵的像素值标准差作为数组记录下来
    # plt.imshow(img1)
    # plt.show()
    # if img1.mean()<225:
    #     effec_num.append(i)           # 判断矩阵的像素值平均数是否小于某个阈值，如果是，则表示找到了感兴趣区域
    if img1.std()>34:
        effec_num.append(i)            # 判断矩阵的像素值标准差是否大于某个阈值，如果是，则表示找到了感兴趣区域


print(np.transpose(color_std))
print(np.transpose(color_aver))
print(np.transpose(effec_num))

effective_y = effec_num[0]*origin_heights//100        #有效区域的左上顶点y坐标找到了
print(effective_y,effec_num[-1])
effective_heights = (effec_num[-1]-effec_num[0]+2)*origin_heights//100 + origin_heights//50        #有效区域的高度也出来了
print(effective_heights)

# plt.plot(range(100), color_aver[:100], label='color_mean_curve')
# plt.legend()
# plt.show()
# plt.plot(range(100), color_std[:100], label='color_std_curve')
# plt.legend()
# plt.show()
# effective_img = origin_slide.read_region((17600,effective_y),0,(9000, effective_heights))
# plt.imshow(effective_img)
# plt.show()