from socket import *

serverPort = 12000  # Cổng mà server sẽ lắng nghe
serverSocket = socket(AF_INET, SOCK_STREAM)  # Tạo socket TCP
serverSocket.bind(('', serverPort))  # Gán socket với cổng 12000
serverSocket.listen(1)  # Cho phép tối đa 1 kết nối đồng thời

print("The server is ready to receive...")

while True:
    connectionSocket, addr = serverSocket.accept()  # Chấp nhận kết nối từ Client
    print(f"Connected by {addr}")  # Hiển thị thông tin máy Client

    sentence = connectionSocket.recv(1024).decode()  # Nhận dữ liệu từ Client
    capitalizedSentence = sentence.upper()  # Chuyển thành chữ hoa

    connectionSocket.send(capitalizedSentence.encode())  # Gửi lại Client
    connectionSocket.close()  # Đóng kết nối với Client
