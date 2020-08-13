import socket        # importing socket library
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    # socket instance(making a socket) - address family(ipv4), TCP protocol
mysock.connect(('data.pr4e.org', 80))    # connecting to a server using ip address and a port
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)     # requesting for the required data
while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
mysock.close()

