import time
from datetime import date
from flask import Response, request, g

def run_before_request():
    g.start_time = time.time()

def run_after_request(response: Response):
    if response and response.status_code == 200:
        if request.url_rule:
            print(request.url_rule.rule)
        else:
            print(request.path)
        exec_start_time = g.start_time
        t = time.time() - exec_start_time
        print("time: " + str(t))
    return response
