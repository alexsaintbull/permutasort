def B(elements):
	array = list(elements)
	for i in range(0, len(array)-1):
		if array[i]>array[i+1]:
			array[i], array[i+1] = array[i+1], array[i] 			
	return array
