import os
from PIL import Image
import numpy as np

def get_image(imageDir):
    """把图片库里的图片筛选并放入一个列表里面"""

    # 读取一个文件夹中的所有文件和子文件夹名称，返回一个列表
    files = os.listdir(imageDir)
    images = []
    for file  in files:
        # 来获取图片的完整文件名，能确保代码在两种路径都不会出错
        filePath = os.path.abspath(os.path.join(imageDir, file))
        try:
            fp = open(filePath, "rb")
            # 打开图片
            im = Image.open(fp)
            images.append(im)
            # 损坏直接抛出异常
            im.load()
            fp.close()
        except:
            print("不支持的文件: %s" % (filePath,))
    return images

if __name__ == "__main__":
    result = getImage("img_lib_noise")
    print(result)