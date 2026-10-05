import json
import paho.mqtt.client as mqtt

BROKER = "broker.hivemq.com"
PORT = 1883
CMD_TOPIC = "iot/lab/light01/cmd"
STATUS_TOPIC = "iot/lab/light01/status"
DEVICE_ID = "light01"

# Trạng thái ban đầu của đèn
current_status = "OFF"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print(f"Đã kết nối Broker! Đang lắng nghe lệnh tại: {CMD_TOPIC}")
        client.subscribe(CMD_TOPIC)
        # Gửi trạng thái ban đầu khi vừa khởi động thiết bị
        publish_status(client)
    else:
        print(f"Kết nối thất bại, mã lỗi: {rc}")

def on_message(client, userdata, msg):
    global current_status
    command = msg.payload.decode('utf-8').strip().upper()
    
    print(f"Nhận được lệnh: {command}")
    
    if command == "ON":
        current_status = "ON"
        publish_status(client)
    elif command == "OFF":
        current_status = "OFF"
        publish_status(client)
    else:
        print(f"Lệnh không hợp lệ nhận được: {command}")

def publish_status(client):
    payload_data = {
        "device_id": DEVICE_ID,
        "status": current_status
    }
    payload = json.dumps(payload_data)
    client.publish(STATUS_TOPIC, payload)
    print(f"Đã cập nhật trạng thái lên {STATUS_TOPIC}: {payload}")

def main():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    try:
        client.connect(BROKER, PORT, 60)
        client.loop_forever()
    except KeyboardInterrupt:
        print("\nThiết bị Smart Light đã dừng hoạt động.")
        client.disconnect()

if __name__ == "__main__":
    main()
