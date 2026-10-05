import json
import paho.mqtt.client as mqtt

BROKER = "broker.hivemq.com"
PORT = 1883
TOPIC = "iot/lab/sensor01/data"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        client.subscribe(TOPIC)
        print(f"Đã kết nối Broker và lắng nghe topic: {TOPIC}")
    else:
        print(f"Kết nối thất bại, mã lỗi: {rc}")

def on_message(client, userdata, msg):
    try:
        data = json.loads(msg.payload.decode('utf-8'))
        device_id = data.get("device_id")
        temperature = data.get("temperature")
        humidity = data.get("humidity")
        
        print(f"\nDevice: {device_id}")
        print(f"Temperature: {temperature} C")
        print(f"Humidity: {humidity} %")
        
        if temperature > 35:
            print("CANH BAO: Nhiet do cao")
        if humidity < 40:
            print("CANH BAO: Do am thap")
            
    except json.JSONDecodeError:
        print("Lỗi: Không thể phân tích dữ liệu JSON.")

def main():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    try:
        client.connect(BROKER, PORT, 60)
        client.loop_forever()
    except KeyboardInterrupt:
        print("\nĐã dừng chương trình Monitoring Subscriber.")
        client.disconnect()

if __name__ == "__main__":
    main()
