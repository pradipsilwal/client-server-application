def update(updatedList, filename, mode):
	try:
		updatedFile = open(filename, mode)
	except Exception as e:
		print(e)
	else:
		for items in updatedList:
			lineToWrite = ""
			for details in items:
				lineToWrite +=str(details) + "\t"
			updatedFile.write(lineToWrite + "\n")
		print("File updated")
		try:
			updatedFile.close()
		except Exception as e:
			print(e)
