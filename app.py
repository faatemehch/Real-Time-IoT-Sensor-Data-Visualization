import streamlit as st
import requests
import time

st.title("DHT11 Live Data via FastAPI")

temp_display = st.empty()
hum_display = st.empty()
url = "http://192.168.1.36:8000/latest"

while True:
    try:
        r = requests.get(url)
        data = r.json()
        temp_display.write(f"🌡 Temperature: {data['temp']}°C")
        hum_display.write(f"💧 Humidity: {data['hum']}%")
    except:
        st.write("Error fetching data")
        
    time.sleep(5)
