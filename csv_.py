import csv

with open('example_.csv', newline='') as csvfile:
	csv_data = csv.reader(csvfile, delimiter=',', quotechar='"')
	headers = {}
	col = 0
	for row in csv_data:
		if col==0:
			headers=set(row)
			print(headers)
			col += 1
		else:
			print(', '.join(row))


#via DictReater
with open('example_.csv', newline='') as csvfile:
	csv_data = csv.DictReader(csvfile, delimiter=',', quotechar='"')
	for row in csv_data:
		print(f"Row={int(row['ID'])} Name={row['Name'].strip()} About={row['About'].strip()}")
