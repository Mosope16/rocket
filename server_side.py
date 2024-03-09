import socket
import os
from tqdm import tqdm, trange
import time

file = "Monument valley final version-BAMS.png"
file_size = os.path.getsize(file) / 1000000

# create a socket with IPV4(AF_INET) and TCP(SOCK_STREAM)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind the socket to an IP-Address and Port Address
# server.bind((socket.gethostbyname(socket.gethostname()), 419))
server.bind(("localhost", 419))

# allow socket to "listen" for connections
server.listen()
print("SERVER HAS STARTED...")


# allow server to accept connections
client_socket, client_address = server.accept()

# send file name
client_socket.send(file.encode("utf-8"))

# send file size
client_socket.send("{:.3f}".format(file_size).encode("utf-8"))

# progress bar
progress = tqdm(total=file_size*1000000, desc="Sending", unit="B")


# open the file and send in chunks to conservememory
with open(file, "rb") as f:
    while True:
        data = f.read(4096) # send data in chunks
        if not data:
            break
        # send the file
        client_socket.send(data)

        progress.update(len(data))

progress.close()
print("\n...CLOSING SERVER")

server.close()
client_socket.close()

