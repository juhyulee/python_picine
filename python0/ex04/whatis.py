import sys

try:
	if (len(sys.argv) >= 3):
		raise AssertionError("AssertionError: more than one argument is provided")
except AssertionError as a:
	print(a)
	sys.exit()


if (len(sys.argv) == 1):
	sys.exit()

try:
	if not(48 <= ord(sys.argv[1]) <= 57):
		raise AssertionError("AssertionError: argument is not an interger")
	value = int(sys.argv[1])

	if value % 2 == 0:
		print("I'm Even.")
	else:
		print("I'm odd.")
except AssertionError as e:
	print(e)

