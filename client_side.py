import socket
from tqdm import tqdm
import time

# create a socket w/ IPV4(AF_INET) and TCP(SOCK_STREAM)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect socket to server on same IP an PORT Address
client.connect(("localhost", 10565))

# receive file name
file_name  = client.recv(1024).decode("utf-8")

# intro
print("|------------------------------------------------------------------------------|")
print("|------------------------- ROCKET TRANSFER 1.0 --------------------------------|")
print("|------------------------------------------------------------------------------|")
print("\n")


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
print("\n|------------------CREATED BY BAMILOSIN DANIEL - 9TH MARCH 2024---------------|\n")

client.close()


