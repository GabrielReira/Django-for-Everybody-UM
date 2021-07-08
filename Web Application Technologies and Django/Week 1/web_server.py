from socket import *

def createServer():
    server_socket = socket(AF_INET, SOCK_STREAM)
    try:
        server_socket.bind(('localhost', 3000))
        server_socket.listen(5)

        while True:
            (client_socket, address) = server_socket.accept()
            rd = client_socket.recv(5000).decode()

            # Print the GET requests
            pieces = rd.split('\n')
            if (len(pieces) > 0):
                print(pieces[0])
            
            data = 'HTTP/1.1 200 OK\r\n'
            data += 'Content-Type: text/html; charset=utf-8\r\n\r\n'
            data += '<html><body>Hey man, whats up?</body><html>\r\n\r\n'
            client_socket.sendall(data.encode())
            client_socket.shutdown(SHUT_WR)
    
    except KeyboardInterrupt:
        print('\nShutting down...\n')
    except Exception as exc:
        print(f'Error:\n{exc}')

    server_socket.close()

print('Acess http://localhost:3000')
createServer()
            