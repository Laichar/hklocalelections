import csv
import json

print('file name please')
file_name = input()

def organise(fn):
	sheet = open(fn)
	sheetreader = csv.DictReader(sheet)
	for row in sheetreader:
		print(row['Name of Nominees (Surname First)'] + " is running in " + row['Constituency'])

# actually run the program
organise(file_name)
