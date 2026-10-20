"""用于计算一张照片的平均颜色"""
import numpy as np

def getAverageRGB(image):
    im = np.array(image.convert("RGB"))   # 统一转 RGB，防灰度/RGBA
    h, w, d = im.shape                     # 正确的顺序：高、宽、通道
    # 
    return tuple(im.reshape(-1, d).mean(axis=0))