import os
import sys
import redis

try:
    host = os.getenv("REDIS_HOST", "localhost")
    port = int(os.getenv("REDIS_PORT", 6379))
    r = redis.Redis(host=host, port=port, decode_responses=True)
    r.ping()
    sys.exit(0)
except Exception:
    sys.exit(1)