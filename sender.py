import network
import espnow
from machine import Pin
p0 = Pin(0, Pin.IN, Pin.PULL_UP)


# A WLAN interface must be active to send()/recv()
sta = network.WLAN(network.WLAN.IF_STA)  # Or network.WLAN.IF_AP
sta.active(True)
sta.disconnect()      # For ESP8266

e = espnow.ESPNow()
e.active(True)
peer = b'\x80e\x99\xfa\x86<'   # MAC address of peer's wifi interface
e.add_peer(peer)      # Must add_peer() before send()

e.send(peer, "Starting...")
x = 0
y = 0
while True:
    if p0.value() == 0:
        x+=5
        y+=5
        string = str(x)+","+str(y)
        e.send(peer,string,True)
e.send(peer, b'end')