import psutil
import json
import time

def get_metrics():
    return {
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "cpu": {
            "percent": psutil.cpu_percent(interval=1),
            "count": psutil.cpu_count()
        },
        "memory": {
            "total_mb": round(psutil.virtual_memory().total / 1024**2),
            "used_mb": round(psutil.virtual_memory().used / 1024**2),
            "percent": psutil.virtual_memory().percent
        },
        "disk": {
            "total_gb": round(psutil.disk_usage('/').total / 1024**3, 1),
            "used_gb": round(psutil.disk_usage('/').used / 1024**3, 1),
            "percent": psutil.disk_usage('/').percent
        }
    }

if __name__ == "__main__":
    metrics = get_metrics()
    print(json.dumps(metrics, indent=2))
