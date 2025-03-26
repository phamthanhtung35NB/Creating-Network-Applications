from socket import *  # Import thư viện socket để làm việc với mạng

serverPort = 12000  # Cổng server lắng nghe (UDP sử dụng số cổng bất kỳ, miễn là trùng với client)
serverSocket = socket(AF_INET, SOCK_DGRAM)  # Tạo socket UDP (AF_INET = IPv4, SOCK_DGRAM = UDP)
serverSocket.bind(('', serverPort))  # Gán socket vào cổng 12000, chấp nhận kết nối từ tất cả IP

print("The server is ready to receive...")  # Thông báo server đã khởi động và đang chờ dữ liệu

while True:  # Vòng lặp vô hạn để server chạy liên tục
    message, clientAddress = serverSocket.recvfrom(2048)  # Nhận dữ liệu từ client (2048 byte tối đa)
    modifiedMessage = message.decode().upper()  # Chuyển nội dung nhận được thành chữ in hoa
    print(f"Received from {clientAddress}: {message.decode()}")  # In ra màn hình nội dung nhận được
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)  # Gửi lại dữ liệu đã chuyển đổi cho client
