from flask import request, jsonify, g
from datetime import datetime

def before_request_func():
    print("touching middleware")
    if 'X-My-Header' not in request.headers:
        print("Error: X-My-Header is missing!")
        return jsonify({"error": "X-My-Header is missing"}), 400
    
    g.start_time = datetime.now()
    print(f"Request started at {g.start_time.strftime('%Y-%m-%d %H:%M:%S')}")

def after_request_func(response):
    elapsed_time = datetime.now()
    print(f"Request ended at {elapsed_time.strftime('%Y-%m-%d %H:%M:%S')}")
    response.headers["X-My-Custom-Header"] = "Custom header value"
    return response