# main.py

import os

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from datetime import datetime
from dotenv import dotenv_values

config = dotenv_valuse(f"{os.getcwd}/.env")

app = FastAPI()

# TODO Change origins to tailscale ip addresses?
# TODO Change allow_methods to the methods available
app.add_middlewar(
        CORSMiddleware,
        allow_origins=['*'],
        allow_methods=['*'],
        # Maybe not needed.. Accept and Content-Type are enabled
        # by default
        # allow_headers=['*']
    )

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

# Return basic success response
# Preflight might already take care of this I suppose
@app.get("/")
def default() -> Default:
    return { "message": "success" }

# Returns the total amount of hours worked by an individual.
# Greedy.
@app.get("/timesheet/{user_id}")
def get_total_time(
        user_id: int, 
) -> TotalHours:
    pass

# Returns the total amount of hours worked by an individual
# in a given range of dates. 
@app.get("/timesheet/{user_id}")
def get_time_in_range(user_id: int, req: ReqTotalHoursInRange):
    pass

# Returns the last clock in time. Important to figure out how
# long the individual has been already working
@app.get("/timesheet/clock/last/{user_id}")
def return_last_clock_in(user_id: str):
    pass

# Clocks the user in.
# Returns time stamp of when the individual clocked in. 
@app.put("/timesheet/clock/in/{time}")
def clock_in(time: str):
    pass

# Clocks the user out.
# Return time stamp of when the individual clocked out.
@app.put("/timesheet/clock/out/{time}")
def clock_out(time: str):
    pass
