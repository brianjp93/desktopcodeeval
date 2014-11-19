import sys

with open(sys.argv[1],'r') as f:
	for line in f:
		word = line.strip()
		for letter in word:
			if word.count(letter) < 2:
				print(letter)
				break
