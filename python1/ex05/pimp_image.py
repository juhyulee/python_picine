import array
from PIL import Image


def ft_invert(array) -> array:
    for i in range(0, image.size[0]):
		for j in range(0, image.size[1]):
			rgb = image.getpixel((i, j))
			rgb_a = (255 - rgb[0], 255 - rgb[1], 255 - rgb[2])
			image.putpixel((i, j), (rgb_a))

def ft_red(array) -> array:
    for i in range(0, image.size[0]):
		for j in range(0, image.size[1]):
			rgb = image.getpixel((i, j))
			rgb_a = (rgb[0], 0, 0)
			image.putpixel((i, j), (rgb_a))

def ft_green(array) -> array:
    for i in range(0, image.size[0]):
		for j in range(0, image.size[1]):
			rgb = image.getpixel((i, j))
			rgb_a = (0, rgb[1], 0)
			image.putpixel((i, j), (rgb_a))

def ft_blue(array) -> array:
    for i in range(0, image.size[0]):
		for j in range(0, image.size[1]):
			rgb = image.getpixel((i, j))
			rgb_a = (0, 0, rgb[2])
			image.putpixel((i, j), (rgb_a))

def ft_grey(array) -> array:
    for i in range(0, image.size[0]):
        for j in range(0, image.size[1]):
            rgb = image.getpixel((i, j))
            rgb_a = round((rgb[0] + rgb[1] + rgb[2]) / 3)
            image.putpixel((i, j), (rgb_a, rgb_a, rgb_a))