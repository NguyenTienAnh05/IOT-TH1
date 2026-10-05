# IOT-TH1: Lập trình Python với giao thức MQTT

## 1. Yêu cầu môi trường
- Python 3.x
- Cài đặt thư viện: `pip install paho-mqtt`

## 2. Cấu hình MQTT Broker
- Sử dụng MQTT Broker công cộng: `broker.hivemq.com`
- Port: `1883`

## 3. Cách chạy các chương trình

### Bài 1 (Gửi và nhận thông điệp)
- Chạy Subscriber: `python subscriber_bai1.py`
- Chạy Publisher: `python publisher_bai1.py`

### Bài 2 (Mô phỏng cảm biến nhiệt độ, độ ẩm)
- Chạy Monitoring Subscriber: `python monitor_subscriber_bai2.py`
- Chạy Sensor Publisher: `python sensor_publisher_bai2.py`

### Bài 3 (Hệ thống điều khiển đèn thông minh)
- Chạy Smart Light Device: `python device_bai3.py`
- Chạy Controller App: `python controller_bai3.py` *(nhập lệnh ON hoặc OFF từ bàn phím để điều khiển đèn, nhập EXIT để thoát)*
