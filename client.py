import socket
from menu import menu

SERVER = "127.0.0.1"
PORT = 8080
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER, PORT))
message = ""
tries = 0
while True:
	if (message == "LOGIN_SUCCESS"):
		print("entered in menu.")
		menu(client)
		print("Now exiting:")
		client.sendall(bytes("EXIT","UTF-8"))
		break
	elif (message == "USER_ACTIVE"):
		if (tries == 3):
			break
		else:
			username = input("Username: ")
			password = input("Password: ")
			usrPass = username + "\t" + password
			client.sendall(bytes(usrPass,"UTF-8"))
			message  = client.recv(1024).decode()
			tries = tries + 1
	else:
		if (message == "LIMIT_EXCEED" or tries == 3):
			break
		else:
			username = input("Username: ")
			password = input("Password: ")
			usrPass = username + "\t" + password
			client.sendall(bytes(usrPass,"UTF-8"))
			message  = client.recv(1024).decode()
			tries = tries + 1

client.close()