import socket
from tqdm import tqdm, trange
import time

# create a socket w/ IPV4(AF_INET) and TCP(SOCK_STREAM)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect socket to server on same IP an PORT Address
# client.connect((socket.gethostbyname(socket.gethostname()), 419))
client.connect(("192.168.35.87", 2200)) # 192.168.43.87

# receive file name
file_name  = client.recv(1024).decode("utf-8")

#  receive file size
file_size = float(client.recv(1024).decode("utf-8"))
print(f"{file_name} ---> {file_size}MB")

# progress bar
progress = tqdm(total=file_size*1000000, desc="Receiving ", unit="B")

with open("1_"+file_name, "wb") as file:
    while True:
        data = client.recv(4096) # receive data in chunks
        if not data:
            break
        file.write(data)

        progress.update(len(data))

progress.close()

client.close()


