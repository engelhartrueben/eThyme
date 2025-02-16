# main.py

from fastapi import FastAPI, Request
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()

# Yields unique id.
# probably not needed. like ever. but its a generator
# so oh well.
def id_gen():
    num = 1
    yield num
    num += 1

# Basic success message
class Default(BaseModel):
    "message": "success"

# Request total hours worked
class ReqTotalHours(BaseModel):
    "auth": str

# Return total hours worked. Greedy
class RetTotalHours(BaseModel):
    "user_id": int
    "total_hours_worked": float

# Request total hours worked between two days
class ReqTotalHoursInRange(BaseModel):
    "start_date": datetime
    "end_date": datetime
    "auth": str

# Returns the dates requested, and the total amount
# of time in integer minutes
class RetTotalHoursInrange(BaseModel):
    "start_date": datetime
    "end_date": datetime
    "total_minutes": int

@app.get("/")
def default() -> Default:
    return { "message": "success" }

@app.get("/timesheet/{user_id}")
def get_total_time(
        user_id: int, 
) -> TotalHours:
    pass

@app.get("/timesheet/{user_id}")
def get_time_in_range(user_id: int, req: ):
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
