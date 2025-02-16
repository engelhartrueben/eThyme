# main.py

from fastapi import FastAPI, Request
from datetime import datetime

app = FastAPI()

# Connect to existing database

# Auto commit
conn.set_session(autocommit=True)

# Open a cursor to perform database operations
curr = conn.cursor()

def id_gen():
    num = 1
    yield num
    num += 1

@app.get("/")
def default_response():
    pass

@app.get("/timesheet/{user_id}")
def get_total_time(user_id: str):
    pass

@app.get("/timesheet/clock/{start_day}/{end_day}")
def get_time_in_range(range: str):
    pass

@app.get("/timesheet/clock/last/{user_id}")
def return_last_clock_in(user_id: str):
    pass

@app.put("/timesheet/clock/in/{time}")
def clock_in(time: str):
    pass

@app.put("/timesheet/clock/out/{time}")
def clock_out(time: str):
    pass
