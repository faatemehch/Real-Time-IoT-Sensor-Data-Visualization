import streamlit as st
import requests
import time
from decouple import config

st.title("DHT11 Live Data via FastAPI")

temp_display = st.empty()
hum_display = st.empty()
url = config("SERVER_URL")+"latest"

while True:
    try:
        r = requests.get(url)
        data = r.json()
        temp_display.write(f"🌡 Temperature: {data['temp']}°C")
        hum_display.write(f"💧 Humidity: {data['hum']}%")
    except:
        st.write("Error fetching data")

    time.sleep(5)
