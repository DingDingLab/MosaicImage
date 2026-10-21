from PIL import Image

def creat_image_grid(images, dims):
	"""
	创建照片并且拼接照片
	:param images: 处理好的照片列表
	:param dims: 最终照片的大小，与原照片大小相等
	"""
	# dims = 网格的尺寸
	m, n = dims
	# 断言检查，True -> 通过，False -> 报错
	assert m*n == len(images)
	
	# 列表推导式
	width = max([img.size[0] for img in images])
	height = max([img.size[1] for img in images])
	
	grid_img = Image.new('RGB', (n*width, m*height))
	
	for index in range(len(images)):
		row = int(index/n)
		col = index - n*row
		grid_img.paste(images[index], (col*width, row*height))
	
	return grid_img