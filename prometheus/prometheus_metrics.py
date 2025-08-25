from prometheus_client import Counter, Gauge, Histogram

REQUEST_COUNTER = Counter(
    name="app_requests_total",
    documentation="Total number of requests to the app",
    labelnames=["endpoint", "method"]
)

RANDOM_NUMBER_GAUGE = Gauge(
    name="app_random_number",
    documentation="Current value of the random number."
)
REQUEST_STATUS_COUNTER = Counter(
    name="request_status_counter",
    documentation="Total number of responses by status code",
    labelnames=['endpoint', 'status_code']
)

REQUEST_LATENCY_HISTOGRAM = Histogram(
    name="request_latency_histogram",
    documentation="The latency of requests in seconds",
    labelnames=['endpoint', 'method']

)

