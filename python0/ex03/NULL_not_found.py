def NULL_not_found(object: any):
	if (str(type(object)) == "<class 'NoneType'>" ):
		print("Nothing:",object,type(object))
		return 0
	elif (str(type(object)) == "<class 'float'>"):
		print("cheese:",object,type(object))
		return 0
	elif (str(type(object)) == "<class 'int'>"):
		print("Zero:",object,type(object))
		return 0
	elif (str(type(object)) == "<class 'str'>" and not object):
		print("Empty:",object,type(object))
		return 0
	elif (str(type(object)) == "<class 'bool'>"):
		print("Fake:",object,type(object))
		return 0
	else:
		print("Type not found")
		return 1
Nothing = None
Garlic = float("NaN")
Zero = 0
Empty = ""
Fake = False
NULL_not_found(Nothing)
NULL_not_found(Garlic)
NULL_not_found(Zero)
NULL_not_found(Empty)
NULL_not_found(Fake)
print(NULL_not_found("Brian"))
