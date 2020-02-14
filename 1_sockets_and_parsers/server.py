import socket
import re

# Create a socket instance
# AF_INET: use IP protocol version 4
# SOCK_STREAM: full-duplex byte stream
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Allow reuse of addresses
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Bind the socket to any address, port 8080, and listen
s.bind(('', 8080))
s.listen()

HEAD_200 = "HTTP/1.1 200 OK\n\n"
HEAD_404 = "HTTP/1.1 404 Not Found\n\n"

# Serve forever
while True:
    # Accept the connection
    conn, addr = s.accept()

    # Receive data from this socket using a buffer of 1024 bytes
    data = conn.recv(1024)

    request = data.decode('utf-8')

    # Print out the data
    print(request)

    resource = re.match(r'GET /(.*) HTTP', request).group(1)
    try:
        with open(resource, 'r') as f:
            content = HEAD_200 + f.read()
        print('Resource {} correctly served'.format(resource))
    except FileNotFoundError:
        content = HEAD_404 + "Resource /{} cannot be found\n".format(resource)
        print('Resource {} cannot be loaded'.format(resource))

    print('--------------------')

    conn.sendall(bytes(content, 'utf-8'))

    # Close the connection
    conn.close()
