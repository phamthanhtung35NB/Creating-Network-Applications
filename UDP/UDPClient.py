from socket import *  # Import thư viện socket để giao tiếp qua mạng

serverName = '192.168.1.100'  # Địa chỉ IP của Server (cần thay thế bằng địa chỉ thực tế của Server)
serverPort = 12000  # Cổng UDP của Server (phải trùng với cổng server đang lắng nghe)

clientSocket = socket(AF_INET, SOCK_DGRAM)  # Tạo socket UDP để gửi/nhận dữ liệu

message = input("Input lowercase sentence: ")  # Nhập chuỗi từ bàn phím
clientSocket.sendto(message.encode(), (serverName, serverPort))  # Gửi dữ liệu tới Server

modifiedMessage, serverAddress = clientSocket.recvfrom(2048)  # Nhận phản hồi từ Server
print("From Server:", modifiedMessage.decode())  # Hiển thị chuỗi đã được Server xử lý

clientSocket.close()  # Đóng kết nối socket
