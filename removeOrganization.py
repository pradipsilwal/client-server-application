from findOrganization import getOrganizationDetails
from updateFile import update

def removeOrganization(orgName):
	getOrganizationDetailList = getOrganizationDetails()
	if (getOrganizationDetails != -1):
		for organizations in getOrganizationDetailList:
			if (organizations[0] == orgName):
				getOrganizationDetailList.remove(organizations)
	update(getOrganizationDetailList, "organizations.txt", "w")