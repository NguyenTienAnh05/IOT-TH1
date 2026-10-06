# IOT-TH1: Lập trình Python với giao thức MQTT

## 1. Yêu cầu môi trường
- Python 3.x
- Cài đặt thư viện: `pip install paho-mqtt`

## 2. Cấu hình MQTT Broker
- Sử dụng MQTT Broker công cộng: `broker.hivemq.com`
- Port: `1883`

## 3. Cách chạy các chương trình
- Hướng dẫn chạy: Cần mở 2 cửa sổ TERMINAL
### Bài 1 (Gửi và nhận thông điệp)
- Mở Terminal và chạy Subscriber: `python subscriber_bai1.py`
- Mở 1 Terminal khác và chạy Publisher: `python publisher_bai1.py`
- Gõ MSV + Họ tên xong nhấn Enter
- Nhấn Ctrl+C để dừng

### Bài 2 (Mô phỏng cảm biến nhiệt độ, độ ẩm)
- Mở Terminal và chạy Monitoring Subscriber: `python monitor_subscriber_bai2.py`
- Mở 1 Terminal khác và chạy Sensor Publisher: `python sensor_publisher_bai2.py`
- Nhấn Ctrl+C để dừng

### Bài 3 (Hệ thống điều khiển đèn thông minh)
- Mở Terminal và chạy Device: `python device_bai3.py`
- Mở 1 Terminaal khác và hạy Controller: `python controller_bai3.py` *(nhập lệnh ON hoặc OFF từ bàn phím để điều khiển đèn, nhập EXIT để thoát)*
## 4. Kết quả
### Bài 1 (Gửi và nhận thông điệp)
Test case 1:
Bên publisher:
client = mqtt.Client()
Đang kết nối tới broker broker.hivemq.com...
Bắt đầu gửi thông điệp lên topic 'iot/lab/message' (Nhấn Ctrl+C để dừng)...
Đã gửi thành công: Xin chao tu client Python MQTT - B23DCCN037 - Nguyen Tien Anh
Đã gửi thành công: Xin chao tu client Python MQTT - B23DCCN037 - Nguyen Tien Anh

Đã dừng chương trình Publisher.

Bên subscriber:
client = mqtt.Client()
Đang kết nối tới broker broker.hivemq.com...
Kết nối thành công tới Broker! Đang lắng nghe topic: iot/lab/message

Nhan duoc message:
Topic: iot/lab/message
Payload: Xin chao tu client Python MQTT - B23DCCN037 - Nguyen Tien Anh
Time: 09:30:44

Nhan duoc message:
Topic: iot/lab/message
Payload: Xin chao tu client Python MQTT - B23DCCN037 - Nguyen Tien Anh
Time: 09:30:46

Test case 2:
Bên publisher:
client = mqtt.client()
Dang kết nối tới broker broker.hivemq.com...
Bắt đầu gửi thông điệp lên topic 'iot/lab/message' (Nhấn Ctrl+C để dừng)...
Đã gửi thành công: Xin chao tu client Python MQTT - B23DCCN690 - Nguyen Van Quang
Đã dừng chương trình Publisher.

Bên subscriber:
client = mqtt.client()
Dang kết nối tới broker broker.hivemq.com...
Kết nối thành công tới Broker! Đang lắng nghe topic: iot/lab/message

Nhan duoc message:
Topic: iot/lab/message
Payload: Xin chao tu client Python MQTT - B23DCCN690 - Nguyen Van Quang
Time: 10:14:11

### Bài 2 (Mô phỏng cảm biến nhiệt độ, độ ẩm)
Bên sensor_publisher:
    client = mqtt.Client()
Đã gửi: {"device_id": "sensor01", "temperature": 29.8, "humidity": 50.8}
Đã gửi: {"device_id": "sensor01", "temperature": 26.7, "humidity": 39.1}
Đã gửi: {"device_id": "sensor01", "temperature": 29.5, "humidity": 54.9}

Đã dừng chương trình Sensor Publisher.

Bên monitor_subscriber:
client = mqtt.Client()
Đã kết nối Broker và lắng nghe topic: iot/lab/sensor01/data

Device: sensor01
Temperature: 29.8 C
Humidity: 50.8 %

Device: sensor01
Temperature: 26.7 C
Humidity: 39.1 %
CANH BAO: Do am thap

Device: sensor01
Temperature: 29.5 C
Humidity: 54.9 %

### Bài 3 (Hệ thống điều khiển đèn thông minh)
Bên controller:
Trang thai nhan duoc:
{"device_id": "light01", "status": "ON"}
Nhap lenh (ON/OFF/EXIT): OFF
Da gui lenh OFF toi light01
Nhap lenh:
Trang thai nhan duoc:
{"device_id": "light01", "status": "OFF"}
Nhap lenh (ON/OFF/EXIT): EXIT
Dang thoat ung dung dieu khien...

Bên device:
client = mqtt.Client()
Đã kết nối Broker! Đang lắng nghe lệnh tại: iot/lab/light01/cmd
Đã cập nhật trạng thái lên iot/lab/light01/status: {"device_id": "light01", "status": "OFF"}
Nhận được lệnh: ON
Đã cập nhật trạng thái lên iot/lab/light01/status: {"device_id": "light01", "status": "ON"}
Nhận được lệnh: OFF
Đã cập nhật trạng thái lên iot/lab/light01/status: {"device id": "light01", "status": "OFF"}
