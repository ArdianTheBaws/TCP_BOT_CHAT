import socket, random, threading
host = '127.0.0.1'
port = 8888
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))

clients = []
names = []
s.listen()



def stream(message):
    for c in clients:
        c.send(message)

def getClient():
    while True:
        print('Server is online... ')
        c, address = s.accept()
        print(f'connection is established with {str(address)}')
        c.send('name?'.encode('ascii'))
        name = c.recv(1024)
        names.append(name)
        clients.append(c)
        print(f'The name of this client is {name}'.encode('ascii'))
        stream(f'{name} has connected to the chat room'.encode('ascii'))
        thread = threading.Thread(target=recvClient, args=(c,))
        thread.start()


def recvClient(c):
    while True:
        try:
            message = c.recv(8760)
            stream(message)
        except:
            index = clients.index(c)
            clients.remove(c)
            c.close()
            name = names[index]
            stream(f'{name} has left the chat room!'.encode('ascii'))
            names.remove(name)
            break

if __name__ == "__main__":
    getClient()