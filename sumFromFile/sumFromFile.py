import sys
with open(sys.argv[1], 'r') as f:
	total = 0
	for num in f:
		total += int(num.strip())
print(total)