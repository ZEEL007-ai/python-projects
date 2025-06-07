import socket

# Step 1: Server ka socket (phone) banaya
server = socket.socket()

# Step 2: Apna IP aur port diya
server.bind(("127.0.0.1", 12345))

# Step 3: Sunne ke liye tayyar
server.listen(1)
print("📻 Server ready. Client ka intezar ho raha hai...")

# Step 4: Client se connection accept kiya
client, address = server.accept()
print("✅ Client connected:", address)

# Step 5: Message exchange start
while True:
    # Client ka message sunna
    msg_from_client = client.recv(1024).decode()
    if msg_from_client.lower() == "exit":
        print("👋 Client ne chat band kar diya.")
        break
    print("Client ➡", msg_from_client)

    # Server ka reply bhejna
    msg_to_client = input("Server ➡ ")
    client.send(msg_to_client.encode())
    if msg_to_client.lower() == "exit":
        print("👋 Server ne chat band kar diya.")
        break

# Step 6: Socket band
client.close()
server.close()
