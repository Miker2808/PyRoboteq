import serial
import time

device = serial.Serial("COM9", 115200)
print(device.name)

device.close()
device.open()

if __name__ == "__main__":
    while True:
        time.sleep(0.1)
        message_raw = "!M 100 100\r"
        #message = message_raw.encode()
        device.write(message_raw.encode())

        