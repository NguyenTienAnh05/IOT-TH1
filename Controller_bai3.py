import paho.mqtt.client as mqtt

BROKER = "broker.hivemq.com"
PORT = 1883
CMD_TOPIC = "iot/lab/light01/cmd"
STATUS_TOPIC = "iot/lab/light01/status"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        client.subscribe(STATUS_TOPIC)
    else:
        print(f"Kết nối thất bại, mã lỗi: {rc}")

def on_message(client, userdata, msg):
    print("\nTrang thai nhan duoc:")
    print(msg.payload.decode('utf-8'))
    print("Nhap lenh (ON/OFF/EXIT): ", end="", flush=True)

def main():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    try:
        client.connect(BROKER, PORT, 60)
        client.loop_start()
        
        print("--- ỨNG DỤNG ĐIỀU KHIỂN ĐÈN ---")
        print("Các lệnh hợp lệ: ON, OFF | Gõ EXIT để thoát.")
        
        while True:
            cmd = input("Nhap lenh: ").strip().upper()
            
            if cmd == "EXIT":
                print("Đang thoát ứng dụng điều khiển...")
                break
            elif cmd in ["ON", "OFF"]:
                client.publish(CMD_TOPIC, cmd)
                print(f"Da gui lenh {cmd} toi light01")
            else:
                print("Lỗi: Lệnh không hợp lệ! Vui lòng chỉ nhập ON, OFF hoặc EXIT.")
                
    except KeyboardInterrupt:
        print("\nĐã dừng ứng dụng Controller.")
    finally:
        client.loop_stop()
        client.disconnect()

if __name__ == "__main__":
    main()
