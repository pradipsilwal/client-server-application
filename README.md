# Client-Server-Application

This is a client server application developed in Python 3.7 using TCP socket programming technique. There are 2 part to this application:
1. Server
2. Client

## Server
After starting, the server waits for client to connect and initiate communication. This server is capable of handling multiple clients simultaneously. The client initiates connection to the server by providing username and password. The server verifies the client by looking at its list of authorized clients which the server stores in a file ***user.txt***.

## Client
After the client is verified by the server and it is connected to the server. Then the user is presented with a list of actons the user can perform as a menu. Selecting the menu item the user interacts with the server. The options are:
1. Get domain name and IP
2. Get statistics
3. Sort data
4. Add organization
5. Remove organization
6. Quit

