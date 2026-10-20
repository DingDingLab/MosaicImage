"""生成随机噪点图片"""
from PIL import Image
import random, os

os.makedirs("img_lib_noise", exist_ok=True)
for i in range(200):
    img = Image.new("RGB", (200, 200))
    pixels = img.load()
    for x in range(200):
        for y in range(200):
            pixels[x, y] = (random.randint(0, 255), random.randint(0, 255), random.randint(0,255))
    img.save(f"img_lib_noise/{i}.jpg")
    # img.save(f"img_noise/{i}.jpg") 错误写法