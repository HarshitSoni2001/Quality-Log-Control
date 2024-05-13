import logging
import json
from datetime import datetime

logging.basicConfig(filename='logs.log', level=logging.INFO, format='%(levelname)s - %(asctime)s - %(message)s')

def log_data(api_name, log_level, log_message, metadata=None):
    log_entry = {
        "api_name": api_name,
        "log_level": log_level,
        "log_message": log_message,
        "timestamp": datetime.utcnow().isoformat(),
        "metadata": metadata
    }
    logging.log(getattr(logging, log_level.upper()), json.dumps(log_entry))

def calling_api(api_name, log_level, log_message, metadata=None):
    log_data(api_name, log_level, log_message, metadata)

if __name__ == "__main__":
    calling_api("example_api", "info", "API call successful", {"source": "log1.log"})
    calling_api("search_api", "error", "Error in search API", {"source": "log2.log"})
    calling_api("user_api", "info", "User logged in", {"source": "log3.log"})
    calling_api("payment_api", "info", "Payment processed", {"source": "log4.log"})
