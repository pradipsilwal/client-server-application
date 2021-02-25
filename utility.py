def reListToString(reList):
	listInString = ""
	for lists in reList:
		for items in lists:
			listInString = listInString + items + "\t"
		listInString = listInString + "\n"
	print(listInString)

	stringToReList(listInString)

def stringToReList(listInString):
	listA = listInString.split("\t")
	print(listA)

reListToString([["a","b","c"], ["1", "2", "3"], ["A", "B", "C"]])