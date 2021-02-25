from findOrganization import getOrganizationDetails
from updateFile import update

def sortByname():
	return sort(False,0)

def sortByMinutes():
	return sort(True, 3)

def sort(ascDsc, sortElementIndex):
	if (getOrganizationDetails() != -1):
		organizationDetailList = getOrganizationDetails()
		if (sortElementIndex == 0):
			organizationDetailList.sort(reverse=ascDsc, key = casInsensitiveSort)
		elif (sortElementIndex == 3):
			organizationDetailList.sort(reverse=ascDsc, key = lambda x: x[sortElementIndex])
		print("Sorted")
		update(organizationDetailList,"organizations.txt", "w")
		# print(organizationDetailList)
		return organizationDetailList
	else:
		message = "LIST_EMPTY"
		print(message)
		return message

def casInsensitiveSort(x):
	return x[0].lower()

# sortByname()