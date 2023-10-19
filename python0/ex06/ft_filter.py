import sys
from typing import List, Callable

def ft_filter(object : Callable,arr : List) -> filter:
	ret = [i for i in arr if object(i) == True]
	for i in ret:
		yield i
	return ret
