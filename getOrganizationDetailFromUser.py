def getDetails():
	name = input("Enter organization name: ")
	domain = input("Enter organization domain name: ")
	ipAddress = input("Enter organization ipAddress: ")
	loop = True
	while (loop):
		try:
			noOfMinutes = int(input("Enter number of minutes of service given by server: "))
			loop = False
		except Exception as e:
			print(e)
			print("Invalid Input. Enter as a number.")
	detailList = [name, domain, ipAddress, noOfMinutes]
	print(detailList)
	return detailList