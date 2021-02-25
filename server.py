import socket, threading
import user_authentication
from findOrganization import findOrganization, isFound
from getStatistics import *
from sort import *
import pickle
from addOrganization import *
from removeOrganization import removeOrganization
from activeUsers import *

class ClientThread(threading.Thread):
    def __init__(self,clientAddress,clientsocket):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        print ("New connection added: ", clientAddress)

    def hello(self):
        print("*************************************HELLO**************************************")

    def serverMenu(self):
        while True:
            choice  = self.csocket.recv(1024).decode()
            print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&TESTING TESTING TESTING &&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
            if (choice == "1"):
                self.csocket.send(bytes("GET_NAME", "UTF-8"))
                orgName = self.csocket.recv(1024).decode()
                orgNameIPDomainList = findOrganization(orgName)
                if (len(orgNameIPDomainList) != 0):
                    orgNameIPDomainStr = orgNameIPDomainList[0] + "\t" + orgNameIPDomainList[1] + "\t" + orgNameIPDomainList[2]
                    self.csocket.send(bytes(orgNameIPDomainStr, "UTF-8"))
                else:
                    self.csocket.send(bytes("NOT_FOUND", "UTF-8"))
                # self.csocket.send(pickle.dumps(orgNameIPDomainList))

            elif (choice == "2"):       # Get Statistics
                if (getStatistics() != "LIST_EMPTY"):
                    minimum, maximum, mean = getStatistics()
                    minMaxMean = str(minimum) + "\t" + str(maximum) + "\t" + str(mean)
                    self.csocket.send(bytes(minMaxMean, "UTF-8"))
                else:
                    self.csocket.send(bytes(getStatistics(), "UTF-8"))

            elif (choice == "3"):       # Sorting
                self.csocket.send(bytes("SORT", "UTF-8"))
                sortChoie = self.csocket.recv(1024).decode()
                if (sortChoie == "1"):
                    if (sortByname() == "LIST_EMPTY"):
                        self.csocket.send(bytes(sortByname(), "UTF-8"))
                    else:
                        sortedList = pickle.dumps(sortByname())
                        self.csocket.send(sortedList)
                elif (sortChoie == "2"):
                    if (sortByMinutes() == "LIST_EMPTY"):
                        self.csocket.send(bytes(sortByMinutes(), "UTF-8"))
                    else:
                        sortedList = pickle.dumps(sortByMinutes())
                        self.csocket.send(sortedList)

            elif (choice == "4"):
                while True:
                    self.csocket.sendall(bytes("GET_DETAILS", "UTF-8"))
                    print("Server: GET_DETAILS")
                    detailList = pickle.loads(self.csocket.recv(4096))
                    print(detailList)
                    if (isFound(detailList[0])):
                        self.csocket.sendall(bytes("DUPLICATE", "UTF-8"))
                    else:
                        self.csocket.sendall(bytes("ADDING", "UTF-8"))
                        add(detailList)
                        break
                    if (self.csocket.recv(1024).decode() == "TERMINATE"):
                        # self.csocket.close()
                        # print ("Disconnecting...")
                        break
                break

            elif (choice == "5"):
                while True:
                    self.csocket.sendall(bytes("GET_ORG_NAME", "UTF-8"))
                    orgName = self.csocket.recv(1024).decode()
                    if (isFound(orgName)):
                        self.csocket.sendall(bytes("REMOVING", "UTF-8"))
                        removeOrganization(orgName)
                        break
                    else:
                        self.csocket.sendall(bytes("ABSENT", "UTF-8")) 
                    if (self.csocket.recv(1024).decode() == "TERMINATE"):
                        break
                break
            elif (choice == "6"):
                break




    def run(self):
        print ("Connection from : ", clientAddress)
        #self.csocket.send(bytes("Hi, This is from Server..",'utf-8'))
        msg = ''
        auth = False
        tries = 3
        while True:
            if (not auth):
                if (tries >= 1):   
                    usrPass = self.csocket.recv(1024).decode().split()
                    print(usrPass)
                    isMatch, message = user_authentication.authentication([usrPass[0], usrPass[1]])
                    activeUsersList = getActiveUsers()
                    if (isMatch):
                        if (usrPass not in activeUsersList):
                            auth = True
                            self.csocket.send(bytes("LOGIN_SUCCESS", "UTF-8"))
                            updateActiveUsers(usrPass)
                        else:
                            tries = tries - 1
                            print("User is active.", tries, "left.")
                            self.csocket.send(bytes("USER_ACTIVE", "UTF-8"))
                    else:
                        tries = tries - 1
                        print("Incorrect username or password.", tries, "left.")
                        self.csocket.send(bytes("AUTH_ERROR", "UTF-8"))

                else:
                    self.csocket.send(bytes("LIMIT_EXCEED", "UTF-8"))
                    self.csocket.close()
                    break
            else:
                if (auth):
                    self.serverMenu()
                    cMessage = self.csocket.recv(1024).decode()
                    if (cMessage == "EXIT"):
                        break
                    # if cMessage=="bye":
                    #   break
                    # print ("from client", cMessage)
                    # self.csocket.send(bytes(cMessage,'UTF-8'))

        print ("Client at ", clientAddress , " disconnected...")
        self.csocket.close()

    

LOCALHOST = "127.0.0.1"
PORT = 8080
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((LOCALHOST, PORT))
print("Server started")
print("Waiting for client request..")
while True:
    server.listen(1)
    clientsock, clientAddress = server.accept()
    newthread = ClientThread(clientAddress, clientsock)
    newthread.start()

