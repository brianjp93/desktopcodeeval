import sys
with open(sys.argv[1], 'r') as f:
	for line in f:
		nums = line.split(",")
		num, p1, p2 = int(nums[0]), int(nums[1]) - 1, int(nums[2]) - 1
		bit = "{0:b}".format(num)
		if bit[::-1][p1] == bit[::-1][p2]:
			print("true")
		else:
			print("false")