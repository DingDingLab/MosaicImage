from PIL import Image
import numpy as np
from split_image import split_image
from average_RGB import average_RGB
from best_match_index import best_match_index
from get_image import get_image
from create_image_grid import creat_image_grid

def creat_photomosaic(target_image, input_images, grid_size, reuse_images=True):
    """
    创建图片马赛克
    :param target_image: 需要替换的照片
    :param input_iamge: 输入的照片库
    :param grid_size: 照片的尺寸
    :param reuse_image: 处理flag
    """
    print('splitting input image..')
    # 照片切小了之后的列表
    target_images = split_image(target_image, grid_size)
    print('finding image matches')
    # for each file, pick one matching input image
    output_images = []
    # user feedback(反馈)
    count = 0
    batch_size = max(1, len(target_images) // 10)

    # 计算照片的平均值，并存入 avgs中
    avgs = []
    for img in input_images:
        avgs.append(average_RGB(img))

    for img in target_images:
        # 计算每一张照片的平均像素
        avg = average_RGB(img)
        # 找到匹配(mathcing)的照片
        match_index = best_match_index(avg, avgs)
        # 输出列表 += 匹配的项目
        output_images.append(input_images[match_index].resize(img.size))

        # feedback
        if count > 0 and batch_size > 10 and count % batch_size == 0:
            print('processed %d of %d...',(count, len(target_images)))
        count += 1
    print('creating mosaic...')
    # 组合成照片
    mosaic_image = creat_image_grid(output_images, grid_size)
    return mosaic_image

if __name__ == "__main__":
    img = Image.open(open('test_1.png', "rb"))
    imgs = getImage('img_lib_noise')
    # print (imgs)
    creat_photomosaic(img, imgs, (1024, 1024))