import sys
with open(sys.argv[1], 'r') as f:
	for num in f:
		total = 0
		for n in str(num.strip()):
			total += int(n)
		print(total)