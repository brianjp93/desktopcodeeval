import sys

def find_cycle(num_list):
	pass

with open(sys.argv[1],'r') as f:
	for line in f:
		nums = line.strip().split()
		print(find_cycle(nums))