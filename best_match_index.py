def best_match_index(input_avg, avgs):
	"""
	在图片库中找到最佳匹配
	:param input_avg: 需要被匹配的照片，大图片的一小块
	:param avgs: 计算好的图片库的平均值
	"""
	avg = input_avg
	
	index = 0
	min_index = 0
	min_dist = float("inf")
	for val in avgs:
		dist = ((val[0] - avg[0])*(val[0] - avg[0]) + (val[1] - avg[1])*(val[1] - avg[1]) + (val[2] - avg[2])*(val[2] - avg[2]))
		if dist < min_dist:
			min_dist = dist
			min_index = index
		index+=1
	return min_index