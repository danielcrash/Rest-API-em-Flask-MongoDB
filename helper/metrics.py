from flask import request
from prometheus_client import Counter, Histogram
import time

REQUEST_COUNT = Counter(
    'request_count', 'App Request Count',
    ['app_name', 'method', 'endpoint', 'http_status']
)

REQUEST_LATENCY = Histogram('request_latency_seconds', 'Request latency',
                            ['app_name', 'endpoint', 'http_status']
                            )


def start_timer():
    request.start_time = time.time()


def stop_timer(response):
    resp_time = time.time() - request.start_time
    REQUEST_LATENCY.labels('webapp', request.path, response.status_code).observe(resp_time)
    return response


def record_request_data(response):
    REQUEST_COUNT.labels('webapp', request.method, request.path,
                         response.status_code).inc()
    return response


# Configurar metricas
def setup_metrics(app):
    app.before_request(start_timer)
    app.after_request(record_request_data)
    app.after_request(stop_timer)
