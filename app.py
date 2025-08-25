from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import random

app = FastAPI()

@app.get("/", response_class=JSONResponse)
def get_homepage():
    random_num = random.randint(1, 10)
    return {
        "status":"OK",
        "random_number":random_num
    }

