from PIL import Image
import random, os

# 创建文件夹
# os.mkdir("img_lib", exist_ok=True) 这个会报错，mkdir没有exist属性
os.makedirs("img_lib", exist_ok=True)


for i in range(200):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    img = Image.new("RGB", (200, 200), (r, g, b))
    img.save(f"img_lib/{i}.jpg")
