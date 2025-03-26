from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))  # Lắng nghe trên tất cả các IP của máy

print("Máy chủ đã sẵn sàng để nhận...")

while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    modifiedMessage = message.decode().upper()
    print(f"Nhận được từ: {clientAddress}: {message.decode()}")
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)
