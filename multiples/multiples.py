import sys
with open(sys.argv[1], 'r') as f:
	for line in f:
		nums = line.split(",")
		x = int(nums[0])
		n = int(nums[1])
		if x == n:
			print(x)
		else:
			bigger = n*(x//n + 1)
			print(bigger)