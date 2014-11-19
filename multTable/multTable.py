table = ""
for x in range(1, 13):
	row = ""
	for y in range(1, 13):
		product = x*y
		row += (4-len(str(product)))*" " + str(product)
	row = row.strip() + "\n"
	table += row
print(table.strip())