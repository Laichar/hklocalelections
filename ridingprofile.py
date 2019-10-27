import csv
print('file name please')
file_name = input()

def collectnames(fn):
	ridingnames = []
	sheet = open(fn)
	sheet_reader = csv.DictReader(sheet)
	for row in sheet_reader:
		ridingnames.append(row['Constituency'])
	ridingnames = list(dict.fromkeys(ridingnames))
	return ridingnames

print(collectnames(file_name))
