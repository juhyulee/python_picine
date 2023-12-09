import array
from PIL import Image


def ft_load(path: str) -> array:
	image = Image.open(path)
	if (not image):
		print("error wrong image")
		return 0
	print("The shape of image is: (", image.size[1], ", ",image.size[0],", ",len(image.getpixel((0,0))), ")", sep="")

	resized = image.rotate(90)
	resized = resized.convert('L')
	resized.show()
	arr = []
	for i in range(0, image.size[0]):
		for j in range(0, image.size[1]):
			rgb = image.getpixel((i, j))
			arr.append(rgb)
	return arr

print(ft_load("animal.jpeg"))