from fastapi import APIRouter, HTTPException
from prometheus_client import Counter, Histogram

router = APIRouter()

# Metrics for tracking requests
REQUEST_COUNT = Counter('request_count', 'Total number of requests', ['endpoint'])
REQUEST_LATENCY = Histogram('request_latency_seconds', 'Request latency in seconds', ['endpoint'])

@router.get("/metrics")
async def get_metrics():
    """
    Endpoint to expose metrics for monitoring.
    """
    return {
        "request_count": REQUEST_COUNT.collect(),
        "request_latency": REQUEST_LATENCY.collect()
    }

@router.middleware("http")
async def track_requests(request, call_next):
    """
    Middleware to track request count and latency.
    """
    endpoint = request.url.path
    REQUEST_COUNT.labels(endpoint=endpoint).inc()
    
    # Start time
    start_time = time.time()
    
    response = await call_next(request)
    
    # Calculate latency
    latency = time.time() - start_time
    REQUEST_LATENCY.labels(endpoint=endpoint).observe(latency)
    
    return response