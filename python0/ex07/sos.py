import sys

def main():
	try:
		if (len(sys.argv) != 2):
			raise AssertionError("AssertionError: the arguments are bad")
		arr = []
		for i in range(0, len(sys.argv[1])):
			if (97 <= ord(sys.argv[1][i]) <= 122):
				arr.append(chr(ord(sys.argv[1][i]) - 32))
			elif (65 <= ord(sys.argv[1][i]) <= 97 or ord(sys.argv[1][i]) == 32):
				arr.append(sys.argv[1][i])
			else:
				raise AssertionError("AssertionError: the arguments are bad")
	except AssertionError as e:
		print(e)
		exit()

	morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', ' ': '/ '}
	ret = ' '.join(morse_code_dict[i] for i in arr)
	print(ret)

if __name__ == "__main__":
	main()
