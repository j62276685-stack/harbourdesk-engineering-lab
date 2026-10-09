import os
import time
from datetime import datetime, timezone, timedelta

DEFAULT_NOW = "2026-10-06T09:00:00Z"
_STARTED = time.monotonic()

def parse(value):
    return datetime.fromisoformat(value.replace("Z", "+00:00"))

def now():
    result = parse(os.environ.get("LAB_NOW", DEFAULT_NOW)).astimezone(timezone.utc)
    if os.environ.get("LAB_TICK") == "1":
        result += timedelta(seconds=time.monotonic()-_STARTED)
    return result
