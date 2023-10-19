def slice_me(family: list, start: int, end: int) -> list:
	lst = []
	if (type(family) != type(lst)):
		print("error!!!")
		return 0
	for i in family:
		if (len(i) != len(family[0])):
			print("error!!!")
			return 0
	width = len(family)
	height = len(family[0])
	print("My shape is : (",width,", ",height,")",sep ="")
	sliced = family[start:end]
	print("My new shape is : (",len(sliced),", ",len(sliced[0]),")",sep="")
	return(family[start:end])

family = [[1.80, 78.4],
[2.15, 102.7],
[2.10, 98.5],
[1.88, 75.2]]
print(slice_me(family, 0, 2))
print(slice_me(family, 1, -2))
