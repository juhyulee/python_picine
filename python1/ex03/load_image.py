import array
from PIL import Image

def ft_load(path: str) -> array:
	image = Image.open(path)
	if (not image):
		print("error wrong image")
		return 0
	print("The shape of image is: (", image.size[1], ", ",image.size[0],", ",len(image.getpixel((0,0))), ")", sep="")

	left = 200
	upper = 200
	right = 600
	lower = 600
	resized = image.crop((left, upper, right, lower))
	resized = resized.convert('L')
	print("New shape after slicing: (", right-left, ", ",lower - upper, ") or (", right-left, ", ", lower-upper,", 1)", sep="")
	resized.show()
	arr = []
	for i in range(0, image.size[0]):
		for j in range(0, image.size[1]):
			rgb = image.getpixel((i,j))
			arr.append(rgb)
	return arr
