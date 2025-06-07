import socket

# Step 1: Client ka socket (phone) banaya
client = socket.socket()

# Step 2: Server se connect kiya
client.connect(("127.0.0.1", 12345))
print("📲 Server se connection ho gaya. 'exit' likh ke chat band kar sakte ho.")

# Step 3: Message exchange start
while True:
    # Client ka message bhejna
    msg_to_server = input("Client ➡ ")
    client.send(msg_to_server.encode())
    if msg_to_server.lower() == "exit":
        print("👋 Client ne chat band kar diya.")
        break

    # Server ka reply sunna
    msg_from_server = client.recv(1024).decode()
    if msg_from_server.lower() == "exit":
        print("👋 Server ne chat band kar diya.")
        break
    print("Server ➡", msg_from_server)

# Step 4: Socket band
client.close()
