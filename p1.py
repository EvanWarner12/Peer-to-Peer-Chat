import socket

addr = socket.gethostbyname(socket.gethostname())
port = 1099
var = True
HEADER = 1024
search = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("Type 'c' to copy program, Type 'f' to find copy, and Type 's' to cancel. ")
while var:
    command = input('Type your command: ')
    if command == 'c':
        search = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        msg = "Hello World"
        search.bind((addr, port))
        search.listen(1)
        print("Waiting for connection...")

        while True:
            conn, add = search.accept()
            print("A copy has been found on the socket.")
            conn.send(msg.encode())
            msg = conn.recv(HEADER)
            print(msg.decode())
            conn.close()
            quit()
    elif command == 'f':
        while 1 <= port <= 1500:
            try:
                try:
                    search = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                except:
                    print("Error: Can't open socket.\n")
                    break
                search.connect((addr, port))
                Connect = True
            except ConnectionRefusedError:
                Connect = False
            finally:
                if Connect and port != search.getsockname()[1]:  # If connected,
                    print("{} : {} socket is open \n".format(addr, port))  # print port.
                    print("A copy has been located.")
                    msg = search.recv(HEADER)
                    print(msg.decode())
                    msg = "World says hello to you :)".encode()
                    search.send(msg)
                port = port + 1  # Increase port.
                search.close()
                quit()
    elif command == 's':
        break
