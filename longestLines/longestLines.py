import sys

# index, value
lines = []

all_lines = []

with open(sys.argv[1], 'r') as f:
	first = True
	counter = 0
	for line in f:
		if first:
			num_lines = int(line.strip())
			for i in range(num_lines):
				lines.append([0,0])
			first = False
		else:
			line = line.strip()
			all_lines.append(line)
			mini = lines[0][1]
			index = 0
			for i, tup in enumerate(lines):
				if tup[1] < mini:
					mini = tup[1]
					index = i
			if len(line) > mini:
				lines[index][0] = counter
				lines[index][1] = len(line)
			counter += 1
			
myList = sorted(lines, key = lambda x: x[1])
for i in reversed(myList):
	print(all_lines[i[0]])