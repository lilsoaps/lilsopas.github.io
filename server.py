import socket
import sys
port = 5050
server = "127.0.0.1"
thread = 10
# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((server, port))
server_socket.listen(1)
print(f"Listening as {server}:{port} ...")
while True:
    # Wait for a connection
    print('Waiting for a connection ...')
    client_socket, client_address = server_socket.accept()
    print(f"Connection from {client_address[0]}:{client_address[1]}")
    #get the request from browser
    requests = client_socket.recv(1024).decode()
    print(f"From connected user: {requests}")

    # Parse HTTP headers
    headers = requests.split('\n')
    filename = headers[0].split()[1]

    # Get the content of the file
    if filename == '/':
        filename = '/index.html'

    #get the content of the html requested
    try:
        fin = open("site.html", "rb")
        content = fin.read()
        fin.close()
    except:
        response = "HTTP/1.1 404 Not Found\n\n"
        client_socket.sendall(response.encode())
        client_socket.close()
        continue

    #send response
    response = "HTTP/1.1 200 OK\n\n" + content.decode()
    client_socket.sendall(response.encode())

    # Close the client socket
    client_socket.close()    
















