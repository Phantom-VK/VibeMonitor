from prometheus_client import Counter,Gauge

REQUEST_COUNTER = Counter(
    name="app_requests_total",
    documentation="Total number of requests to the app",
    labelnames=["endpoint"]
)

RANDOM_NUMBER_GAUGE = Gauge(
    name="app_random_number",
    documentation="Current value of the random number."
)

