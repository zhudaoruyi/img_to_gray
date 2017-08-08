import openslide
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

# 读取包含有肿瘤区域的大图（全切片病理图像）
origin_images_path = "Tumor_005.tif"
origin_slide = openslide.open_slide(origin_images_path)

# 读取该肿瘤区域的标注图
annotation_images_path = "Tumor_005_Mask.tif"
mask_slide = openslide.open_slide(annotation_images_path)

origin_dimensions = origin_slide.dimensions

# 自动定位到有效区域
judge_area = origin_slide.read_region((0,effective_x),0,(origin_dimensions[0],origin_dimensions[1]/20.0))



widths = 299
heights = 299

random_x = np.random.randint(0,origin_dimensions[0]-widths)
random_y = np.random.randint(0,origin_dimensions[1]-heights)

random_x,random_y
#人为给定有效区域
effective_x = 17650
effective_y = 125100

effective_widths = 44800
effective_heights = 57600

# 定义随机坐标


random_x = np.random.randint(effective_x,effective_x+effective_widths-widths)
random_y = np.random.randint(effective_y,effective_y+effective_heights-heights)

print(random_x,random_y)

random_img = (origin_slide.read_region((random_x,random_y),0,(widths,heights)))  #注意 openslide 的读取方式
random_img
