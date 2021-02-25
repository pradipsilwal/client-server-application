from getOrganizationDetailFromUser import getDetails
from updateFile import update

def add(detailList):
	organizationDetailList = list()
	organizationDetailList.append(detailList)
	update(organizationDetailList, "organizations.txt", "a")

# add()