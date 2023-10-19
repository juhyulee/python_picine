import sys

def main():

	try:
		if (len(sys.argv) == 1):
			print("What is the text to count?")
			data = sys.stdin.readline()
		elif (len(sys.argv) > 2):
			raise AssertionError("AssertionError: more than one argument is provided")
		else:
			data = sys.argv[1]
	except AssertionError as e:
		print(e)


	lenght = len(data)
	upper = 0
	mark = 0
	lower = 0
	digit = 0
	space = 0

	for i in range(0, len(data)):
		x = ord(data[i])
		if (x >= 65 and x <= 90):
			upper += 1
		elif(x >= 97 and x <= 122):
			lower += 1
		elif(x == 32 or x >= 9 and x <= 13):
			space += 1
		elif (x >= 48 and x <= 57):
			digit += 1
		else:
			mark += 1


	print("The text contains " + str(lenght) + " charactoers:")
	print(str(upper)  + " upper letters")
	print(str(lower)  + " lower letters")
	print(str(mark) + " punctuation marks")
	print(str(space) + " spaced")
	print(str(digit) + " digits")

if __name__ == "__main__":
	main()
