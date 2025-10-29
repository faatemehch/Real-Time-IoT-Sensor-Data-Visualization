# 🌡️ IoT Temperature & Humidity Monitor

A simple IoT system that reads temperature and humidity data from a **DHT11 sensor** using an **ESP8266 (NodeMCU)**, sends the data to a **FastAPI server**, and visualizes it in real-time with **Streamlit**.

DHT11 → ESP8266 (MicroPython) → FastAPI (Python) → Streamlit Dashboard

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository
    git clone https://github.com/faatemehch/Real-Time-IoT-Sensor-Data-Visualization
    cd <project_name>

### 2️⃣ Create and activate a virtual environment
    python -m venv venv
    source venv/bin/activate   # macOS/Linux
    venv\Scripts\activate      # Windows

### 3️⃣ Install dependencies
    pip install -r requirements.txt

## 🖥️ Run on Your Computer
### 1️⃣ Start the FastAPI server
    python server.py
### 2️⃣ Start the Streamlit dashboard
    streamlit run app.py
### 3️⃣ Run main.py

🧠 How It Works

The ESP8266 connects to Wi-Fi and reads DHT11 sensor data.

Every 5 seconds, it sends temperature and humidity to the FastAPI backend.

FastAPI stores the latest reading in memory.

Streamlit continuously fetches /latest and displays live updates.