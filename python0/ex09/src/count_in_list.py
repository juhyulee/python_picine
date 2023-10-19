from ast import List


def count_in_list(lst : List, str) -> int:
	j = 0
	for i in lst:
		if (i == str):
			j += 1
	return j
