import array
from PIL import Image

def	ft_load(path: str) -> array:
	image = Image.open(path)
	if (not image):
		print("error wrong image")
		return	0
	#print("The shape of image is: (", image.size[1], ", ",image.size[0],", ",len(image.getpixel((0,0))), ")", sep="")
	print(image.size)


	for i in range(0, image.size[0]):
		for j in range(0, image.size[1]):
			rgb = image.getpixel((i, j))
			rgb_a = (0, rgb[1], 0)
			image.putpixel((i, j), (rgb_a))
	image.show()
	arr = []
	# for i in range(0, image.size[0]):
	# 	for j in range(0, image.size[1]):
	# 		rgb = image.getpixel((i,j))
	# 		arr.append(rgb)
	return arr

print(ft_load("landscape.jpg"))
