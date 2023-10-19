import sys
from typing import List, Callable
from ft_filter import ft_filter

def main():
	try:
		if (len(sys.argv) != 3):
			raise AssertionError("AssertionError: wrong argument")
	except AssertionError as e:
		print(e)
	arr0 = list(sys.argv[1].split(' '))
	print(arr0)
	arr1 = list(ft_filter(lambda x: len(x) > int(sys.argv[2]), arr0))
	print(arr1)

if __name__ == "__main__":
	main()
