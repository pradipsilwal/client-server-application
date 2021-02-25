import socket
import pickle
from getOrganizationDetailFromUser import *

def menu(client):
	menuItems()
	choice = input("Enter your choice (1, 2, 3, 4, 5 or 6): ")
	while (True):

		if (choice == "1"):
			print("Get domain name and IP.")
			client.sendall(bytes("1", "UTF-8"))
			msg = client.recv(1024).decode()
			if (msg == "GET_NAME"):
				orgName = input("Enter organization name: ")
				client.sendall(bytes(orgName, "UTF-8"))
				orgNameIPDomainStr = client.recv(1024).decode()
				if (orgNameIPDomainStr == "NOT_FOUND"):
					print("Organization Not found.")
				else:
					print("The details are: ")
					print(orgNameIPDomainStr)
				# print(pickle.loads(client.recv(4096)))
			#findOrganization.py

		elif (choice == "2"):
			print("Get statistics")
			client.sendall(bytes("2", "UTF-8"))
			msg = client.recv(1024).decode()
			if (msg == "LIST_EMPTY"):
				print(msg)
			else:
				print(msg)
			#getStatistics()

		elif (choice == "3"):
			print("Sort data")
			client.sendall(bytes("3", "UTF-8"))
			msg = client.recv(1024).decode()
			if (msg == "SORT"):
				print("1. Sort by name.")
				print("2. Sort by minutes.")
				while True:
					sortChoice = input("Enter your choice (1 or 2): ")
					if (sortChoice == "1" or sortChoice == "2"):
						client.sendall(bytes(sortChoice, "UTF-8"))
						# msg = client.recv(1024).decode()
						# print(msg)
						sortedList = pickle.loads(client.recv(4096))
						print(sortedList)
						break
					else:
						print("Invalid input.")
			#sort()

		elif (choice == "4"):
			addOrgCount = 3
			while True:
				if (addOrgCount < 1):
					print("Attempt exceeded.")
					print("Terminating session.")
					client.sendall(bytes("TERMINATE", "UTF-8"))
					break
				elif ((addOrgCount >= 1) and (addOrgCount <= 3)):
					print("Add organization")
					client.sendall(bytes("4", "UTF-8"))
					msg = client.recv(1024).decode()
					if (msg == "GET_DETAILS"):
						print("Client: GET_DETAILS")
						detail = pickle.dumps(getDetails())
						client.send(detail)
						msg = client.recv(1024).decode()
						if (msg == "ADDING"):
							print("Adding organization...")
							client.sendall(bytes("CONTINUE", "UTF-8"))
							break
						elif (msg == "DUPLICATE"):
							addOrgCount = addOrgCount - 1
							print("Tries left: " + str(addOrgCount))
							print("Duplicate value. Cannot Add")
			if (addOrgCount < 1):
				break

		elif (choice == "5"):
			removeOrgCount = 3
			while True:
				if (removeOrgCount < 1):
					print("Attempt exceeded.")
					print("Terminating session.")
					client.sendall(bytes("TERMINATE", "UTF-8"))
					break
				elif ((removeOrgCount >= 1) and (removeOrgCount <= 3)):	
					print("Remove organization")
					client.sendall(bytes("5", "UTF-8"))
					msg = client.recv(1024).decode()
					if (msg == "GET_ORG_NAME"):
						orgName = input("Enter organization name: ").lower()
						client.sendall(bytes(orgName, "UTF-8"))
						msg = client.recv(1024).decode()
						if (msg == "REMOVING"):
							print("Removing Organization...")
							client.sendall(bytes("CONTINUE", "UTF-8"))
							break
						elif (msg == "ABSENT"):
							removeOrgCount = removeOrgCount - 1
							print("Tries left: " + str(removeOrgCount))
							print("Organization not available. Cannot remove")
			if (removeOrgCount < 1):
				break

		elif (choice == "6"):
			print("Quitting session...")
			client.sendall(bytes("6", "UTF-8"))
			print("Program closed")
			break
		else:
			print("Invalid input. Enter again.")
		menuItems()
		choice = input("Enter your choice (1, 2, 3, 4, 5 or 6): ")
		

def menuItems():
	print("1. Get domain name and IP")
	print("2. Get statistics")
	print("3. Sort data")
	print("4. Add organization")
	print("5. Remove organization")
	print("6. Quit")