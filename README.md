ipconfig
📌 Cách hoạt động của Server:
1️⃣ Khởi động Server → Server chờ Client kết nối.
2️⃣ Khi Client gửi dữ liệu → Server xử lý và gửi lại dữ liệu đã viết hoa.
3️⃣ Server tiếp tục lắng nghe Client mới.
📌 Cách hoạt động của Client:
1️⃣ Nhập một chuỗi chữ thường (ví dụ "hello").
2️⃣ Gửi chuỗi đến Server qua kết nối TCP.
3️⃣ Nhận chuỗi đã viết hoa từ Server (ví dụ "HELLO").
4️⃣ Hiển thị kết quả rồi đóng kết nối.
```bash
python TCPServer.py
```
```bash
python TCPClient.py
```
📌 Quá trình giao tiếp TCP
💻 Client → Gửi "hello" → 🌍 Internet → 📡 Server
📡 Server → Chuyển "hello" → "HELLO" → 🌍 Internet → 💻 Client

📌 Giao tiếp TCP vs UDP
TCP (Dùng trong bài này)	    UDP
Đảm bảo dữ liệu không mất	    Không đảm bảo dữ liệu đến đích
Dữ liệu đến đúng thứ tự	        Có thể bị trễ hoặc sai thứ tự
Có kiểm tra lỗi	                Không kiểm tra lỗi






```bash
python UDPServer.py
```
```bash
python UDPClient.py
```