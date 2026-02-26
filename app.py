"""Example of flask main file."""
from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics
from prometheus_client import Gauge
import os
import psutil

app = Flask(__name__)

# Expose metrics at custom endpoint
metrics = PrometheusMetrics(app, path="/actuator/prometheus")

# ----------------------------------------
# Custom Metric with required naming
# ----------------------------------------

app_memory_usage_74cudwfj = Gauge(
    "app_memory_usage_74cudwfj",
    "Current memory usage of the application in bytes"
)

@app.before_request
def track_memory_usage():
    process = psutil.Process(os.getpid())
    memory_usage = process.memory_info().rss
    app_memory_usage_74cudwfj.set(memory_usage)

@app.route('/api/hello')
def hello_world():
    """Returns Hello, EDP!"""
    return 'Hello, EDP!'


if __name__ == '__main__':
    app.run()
