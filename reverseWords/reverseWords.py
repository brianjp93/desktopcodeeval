import sys

with open(sys.argv[1], "r") as f:
	for line in f:
		if line == "":
			pass
		else:
			backwards = ""
			for word in reversed(line.split()):
				backwards += word + " "
			print(backwards.strip())