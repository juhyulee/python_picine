from typing import List, Callable

def give_bmi(height: list[int | float], weight: List[int | float]) -> List[int | float]:
	bmi = []
	if (len(height) != len(weight)):
		print("error: diffrent lst size")
		return 0
	for i in range(0, len(height)):
		if not (isinstance(weight[i], (int, float)) or isinstance(height[i], (int, float))):
			print("error: wrong type")
			return 0
		bmi.append(weight[i] / (height[i] * height[i]))
	return bmi

def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
	lst = []
	for i in range(0,len(bmi)):
		if bmi[i] < limit:
			lst.append(False)
		else:
			lst.append(True)
	return lst
