import dht
from machine import Pin
import network
import socket
import ujson
from time import sleep
import urequests

# connect to wifi
ssid = "DELSA517024"
password = "30004000"
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(ssid, password)
while not wifi.isconnected():
    print(".", end="")
    sleep(1)
print("\nconnected")
# sensor
sensor = dht.DHT11(Pin(12))
url = "http://192.168.1.36:8000/update"  # ifconfig | grep inet


while True:
    sensor.measure()
    t = sensor.temperature()
    h = sensor.humidity()
    data = {'temp': t, "hum": h}
    # print(data)
    try:
        res = urequests.post(url, json=data)
        res.close()
    except  Exception as e:
        print(e)
    sleep(5)


