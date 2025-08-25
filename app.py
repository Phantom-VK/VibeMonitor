from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import random
from prometheus_client import  make_asgi_app
from config.prometheus_metrics import RANDOM_NUMBER_GAUGE, REQUEST_COUNTER

app = FastAPI()
metrics_app = make_asgi_app()
app.mount("/metrics", app = metrics_app)

@app.get("/", response_class=JSONResponse)
def get_homepage():
    # Increment request counter
    REQUEST_COUNTER.labels(endpoint="/").inc()

    random_num = random.randint(1, 10)

    # Set random number gauge
    RANDOM_NUMBER_GAUGE.set(random_num)
    return {
        "status":"OK",
        "random_number":random_num
    }

