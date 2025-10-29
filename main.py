import dht
from machine import Pin
import network
import urequests
from time import sleep
from config import SSID, PASSWORD, SERVERURL

# connect to wifi
ssid = "<SSID>"
password = "<PASSWORD>"
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(ssid, password)
while not wifi.isconnected():
    print(".", end="")
    sleep(1)
print("\nconnected")
# sensor
sensor = dht.DHT11(Pin(12))

# to find the right IP: ifconfig | grep inet
url = "http://<IP>:8000/update"
print(url)

while True:
    sensor.measure()
    t = sensor.temperature()
    h = sensor.humidity()
    data = {'temp': t, "hum": h}
    print(data)
    try:
        res = urequests.post(url, json=data)
        res.close()
    except Exception as e:
        print(e)
    sleep(5)
