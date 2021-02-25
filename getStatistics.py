from findOrganization import getOrganizationDetails

def getStatistics():
	if (getOrganizationDetails() != -1):
		organizationDetailList = getOrganizationDetails()
		total = 0.0
		try:
			minimum = int(organizationDetailList[0][3])
			maximum = int(organizationDetailList[0][3])
			for details in organizationDetailList:
				if (int(details[3]) > maximum):
					maximum = int(details[3])
				if (int(details[3]) < minimum):
					minimum = int(details[3])
				total += int(details[3])
			mean = total / len(organizationDetailList)
			# print("Minimum: ", minimum)
			# print("Maximum: ", maximum)
			# print("Mean: ", mean)
			return minimum, maximum, mean
		except Exception as e:
			print(e)
	else:
		message = "LIST_EMPTY"
		print(message)
		return message

# getStatistics()
