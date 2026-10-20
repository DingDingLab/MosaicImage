import os
from PIL import Image
import numpy as np

def splitImage(image, size):
	W, H = image.size[0], image.size[1]
	m, n = size
	w, h = int(W/n), int(H/m)
	# image list
	imgs = []
	for j in range(m):
		for i in range(n):
			imgs.append(image.crop((i*w, j*h, (i+1)*w, (j+1)*h)))
	return imgs

fp = open('test1.png', "rb")
result = splitImage(Image.open(fp), (4, 4))
for i in range(len(result)):
	result[i].save(f"test1_{i}.png")