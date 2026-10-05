import time
import paho.mqtt.client as mqtt

BROKER = "broker.hivemq.com"
PORT = 1883
TOPIC = "iot/lab/message"

WELCOME_MSG = "Xin chao tu client Python MQTT"

def main():
    print("--- Nhập thông tin sinh viên ---")
    student_id = input("Nhập mã sinh viên: ").strip()
    name = input("Nhập họ và tên: ").strip()
    print("-" * 35)

    client = mqtt.Client()
    
    try:
        print(f"Đang kết nối tới broker {BROKER}...")
        client.connect(BROKER, PORT, 60)
        client.loop_start()
        
        payload = f"{WELCOME_MSG} - {student_id} - {name}"
        
        print(f"Bắt đầu gửi thông điệp lên topic '{TOPIC}' (Nhấn Ctrl+C để dừng)...")
        while True:
            client.publish(TOPIC, payload)
            print(f"Đã gửi thành công: {payload}")
            time.sleep(3)
            
    except KeyboardInterrupt:
        print("\nĐã dừng chương trình Publisher.")
    finally:
        client.loop_stop()
        client.disconnect()

if __name__ == "__main__":
    main()
