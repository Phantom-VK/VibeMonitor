import time

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import random
from prometheus_client import  make_asgi_app
from prometheus.prometheus_metrics import RANDOM_NUMBER_GAUGE, REQUEST_COUNTER, REQUEST_STATUS_COUNTER, \
    REQUEST_LATENCY_HISTOGRAM

app = FastAPI()
metrics_app = make_asgi_app()
app.mount("/metrics", app = metrics_app)

@app.middleware("http")
async def metrics_middleware(request:Request, call_next):
    start_time = time.time()

    response = await call_next(request)
    process_time = time.time() - start_time
    endpoint = request.url.path
    status_code = str(response.status_code)
    method = request.method

    REQUEST_COUNTER.labels(endpoint = endpoint).inc()
    REQUEST_STATUS_COUNTER.labels(endpoint = endpoint, status_code = status_code).inc()
    REQUEST_LATENCY_HISTOGRAM.labels(endpoint = endpoint, method = method).observe(process_time)
    return response

@app.get("/", response_class=JSONResponse)
def get_homepage():
    random_num = random.randint(1, 20)

    RANDOM_NUMBER_GAUGE.set(random_num)

    if random_num % 2 == 0:
        return {
        "status":"OK",
        "random_number":random_num
    }
    return {
        "status":"ERROR",
        "random_number":random_num
    }

