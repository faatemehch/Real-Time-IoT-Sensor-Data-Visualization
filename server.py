from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from decouple import config

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
    uvicorn.run(app, host=config("IP"), port=8000)

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
    uvicorn.run(app, host=config("IP"), port=8000)
