def findOrganization(organizationName):
	if (isFound(organizationName)):
		return getDetails(organizationName)
	else:
		print("Organization is not known to server.")
		return []

def isFound(organizationToFind):
	organizationToFind = organizationToFind.strip().lower()
	if (getOrganizationDetails() != -1):
		organizationsDetailsList = getOrganizationDetails()
		for organizations in organizationsDetailsList:
			if (organizationToFind == organizations[0]):
				return True
	else:
		return False
	return False

def getDetails(organizationToFind):
	organizationToFind = organizationToFind.strip().lower()
	sendOrgNameIPDomain = list()
	if (getOrganizationDetails() != -1):
		organizationsDetailsList = getOrganizationDetails()
		for organizations in organizationsDetailsList:
			if (organizationToFind == organizations[0]):
				message = "Organization found. Returning details..."
				sendOrgNameIPDomain = [organizations[0], organizations[1], organizations[2]]
				print(message)
				print(sendOrgNameIPDomain)
				return sendOrgNameIPDomain
	else:
		message = "Organization Detail list is empty."
		print(message)
		return sendOrgNameIPDomain
	message = "Organization not known to server."
	print(message)
	return sendOrgNameIPDomain


def getOrganizationDetails():
	organizationsDetailsList = list()
	newList = list()
	try:
		organizationFile = open("organizations.txt", "r")
		for organizations in organizationFile:
			singleOrgDetails = organizations.split()
			organizationsDetailsList.append(singleOrgDetails)

		for details in organizationsDetailsList:
			tempDetails = list()
			try:
				tempdetails = [details[0], details[1], details[2], int(details[3])]
			except Exception as e:
				print(e)
			newList.append(tempdetails)

		organizationsDetailsList=list(newList)
		return organizationsDetailsList

	except Exception as e:
		print(e)
		return -1

# findOrganization("google")