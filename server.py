from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()
latest_data = {"temperature": None, "humidity": None}

# Allow Streamlit to read this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/update")
async def update_data(data: dict):
    global latest_data
    latest_data = data
    return {"status": "ok"}

@app.get("/latest")
async def get_latest():
    return latest_data

if __name__ == "__main__":
    uvicorn.run(app, host="192.168.1.36", port=8000)
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()
latest_data = {"temperature": None, "humidity": None}

# Allow Streamlit to access the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/update")
async def update_data(data: dict):
    global latest_data
    latest_data = data
    return {"status": "ok"}

@app.get("/latest")
async def get_latest():
    return latest_data

if __name__ == "__main__":
    uvicorn.run(app, host="192.168.1.36", port=8000)
