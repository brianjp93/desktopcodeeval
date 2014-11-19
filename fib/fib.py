import sys

def fib(n):
	if n == 0:
		return 0
	else:
		total = 1
		last = 1
		temp = 0
		for i in range(1, n):
			total += temp
			temp = last
			last = total
	return total

with open(sys.argv[1], 'r') as f:
	for line in f:
		n = int(line.strip())
		print(fib(n))