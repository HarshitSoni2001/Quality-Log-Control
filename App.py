from flask import Flask, request, render_template, abort
import json
import re
from datetime import datetime

app = Flask(__name__)
logs = [
    {"api_name": "api1", "log_level": "info", "log_message": "API call successful", "timestamp": "2024-04-15", "metadata": {"source": "log1.log"}},
    {"api_name": "api2", "log_level": "error", "log_message": "Error in search API", "timestamp": "2024-04-16", "metadata": {"source": "log2.log"}},
    {"api_name": "api2", "log_level": "error", "log_message": "User logged in", "timestamp": "2024-04-12", "metadata": {"source": "log3.log"}},
    {"api_name": "api2", "log_level": "error", "log_message": "Payment processed", "timestamp": "2024-04-18", "metadata": {"source": "log4.log"}}
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET'])
def search_logs():
    query = request.args.get('query')
    start_date = request.args.get('start_date') 
    end_date = request.args.get('end_date')
    filtered_logs = filter_logs(query, start_date, end_date)
    return render_template('search_results.html', logs=filtered_logs)

def filter_logs(query, start_date=None, end_date=None):
    filtered_logs = []
    for log in logs:
        if re.search(query, json.dumps(log)):
            if start_date and end_date:
                log_timestamp = datetime.strptime(log['timestamp'], '%Y-%m-%dT%H:%M:%SZ')
                start_datetime = datetime.strptime(start_date, '%Y-%m-%d')
                end_datetime = datetime.strptime(end_date, '%Y-%m-%d')
                if start_datetime <= log_timestamp <= end_datetime:
                    filtered_logs.append(log)
            else:
                filtered_logs.append(log)
    return filtered_logs

if __name__ == '__main__':
    app.run(debug=True)
