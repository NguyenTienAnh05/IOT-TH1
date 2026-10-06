from datetime import datetime
import paho.mqtt.client as mqtt

BROKER = "broker.hivemq.com"
PORT = 1883
TOPIC = "iot/lab/message"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print(f"Kết nối thành công tới Broker! Đang lắng nghe topic: {TOPIC}")
        client.subscribe(TOPIC)
    else:
        print(f"Kết nối thất bại, mã lỗi: {rc}")

def on_message(client, userdata, msg):

    current_time = datetime.now().strftime("%H:%M:%S")
    
    print("\nNhan duoc message:")
    print(f"Topic: {msg.topic}")
    print(f"Payload: {msg.payload.decode('utf-8')}")
    print(f"Time: {current_time}")

def main():
    client = mqtt.Client()

    client.on_connect = on_connect
    client.on_message = on_message

    try:
        print(f"Đang kết nối tới broker {BROKER}...")
        client.connect(BROKER, PORT, 60)
        
        client.loop_forever()
        
    except KeyboardInterrupt:
        print("\nĐã dừng chương trình Subscriber.")
        client.disconnect()

if __name__ == "__main__":
    main()
