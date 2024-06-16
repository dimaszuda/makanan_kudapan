import uvicorn
from fastapi import FastAPI
from routes import kue_kudapan

app = FastAPI()
app.include_router(kue_kudapan.router)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port="8000")

# TODO: add logging to perform debugging