def authentication(unamePasswordForVerification):
	# unamePasswordForVerification = ["rabindra", "rabindra23"]
	if ( getAuthenticatedUsersList() != -1 ):
		verifiedUsersList = getAuthenticatedUsersList()
		for verifiedUsers in verifiedUsersList:
			if (verifiedUsers == unamePasswordForVerification):
				message = "AUTH_SUCCESS"
				print(message)
				return True, message
	else:
		message = "NO_DATA" 
		print(message)
		return False, message
	message = "AUTH_ERROR" 
	print(message)
	return False, message


def getAuthenticatedUsersList():
	verifiedUsersList = list()
	try:
		verifiedUsersFile = open("user.txt", "r")
		for verifiedUsers in verifiedUsersFile:
			usernamePassword = list()
			usernamePassword = verifiedUsers.split()
			verifiedUsersList.append(usernamePassword)
		verifiedUsersFile.close()
		return verifiedUsersList
	except IOError:
		message = "Error in opening user file." 
		print(message)
		return -1
	except:
		message = "Error"
		print(message)
		return -1