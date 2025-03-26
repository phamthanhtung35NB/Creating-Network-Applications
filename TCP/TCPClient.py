from socket import *

serverName = '192.168.1.100'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)  # Tạo socket TCP
clientSocket.connect((serverName, serverPort))  # Kết nối tới Server

sentence = input("Input lowercase sentence: ")  # Nhập dữ liệu từ bàn phím
clientSocket.send(sentence.encode())  # Gửi dữ liệu tới Server

modifiedSentence = clientSocket.recv(1024)  # Nhận dữ liệu từ Server
print("From Server:", modifiedSentence.decode())  # Hiển thị kết quả

clientSocket.close()  # Đóng kết nối
