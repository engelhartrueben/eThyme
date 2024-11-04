# main.py

from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

global id
id = 1

@app.get("/")
def default_response():
    # Eventually want response ID to be tracked in DB
    response = {
        "head": "Default Response. Cute.",
        "body": {
            "date": datetime.today(),
            "response_id": id
        }
    }
    id += 1
    return response

@app.get("/timesheet/")
def get_total_time():
    pass

@app.get("/timesheet/clock/{range}")
def get_time_in_range(range: str):
    pass

@app.get("/timesheet/clock/last/")
def return_last_clock_in():
    pass

@app.put("/timesheet/clock/in/{time}")
def clock_in(time: str):
    pass

@app.put("/timesheet/clock/out/{time}")
def clock_out(time: str):
    pass