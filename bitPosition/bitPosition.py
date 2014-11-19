import sys
with open(sys.argv[1], 'r') as f:
	for line in f:
		nums = line.split(",")
		num, p1, p2 = int(nums[0]), int(nums[1]), int(nums[2])
		bit = "{0:b}".format(num)
		if bit[p1] == bit[p2]:
			print("true")
		else:
			print("false")