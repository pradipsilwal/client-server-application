from updateFile import update

def getActiveUsers():
	activeUsersList = list()
	try:
		activeUsersFile = open("active_users", "r")
		for users in activeUsersFile:
			tempList = users.split()
			activeUsersList.append(tempList)
	except IOError:
		print("Error in opening file.")
	except Exception:
		print("Error in processing.")	
	return activeUsersList

def updateActiveUsers(activeUsersList):
	listToupdate = list()
	listToupdate.append(activeUsersList)
	update(listToupdate, "active_users.txt", "a")