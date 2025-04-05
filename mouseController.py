import serial
import mouse
import json
import time

port = "COM7"  # Replace with your port
baud_rate = 115200      # Replace with your baud rate
while True:
    try:
        ser = serial.Serial(port, baud_rate)
        print(f"Connected to {port} at {baud_rate} baud")
    except serial.SerialException as e:
        time.sleep(1)
        continue
    try:
        while True:
            data = ser.readline()
            if data:
                coordinates = data.decode().strip().split(",")
                try:
                    x = coordinates[0]
                    y = coordinates[1]
                    mouse.move(x,y)
                except:
                    print(data)

    except:
        time.sleep(1)
        ser.close()
