# main.py

from fastapi import FastAPI
from datetime import datetime
import psycopg2

app = FastAPI()

# Connect to existing database
conn = psycopg2.connect("dbname=eThyme user=eThyme_user password=eThyme_test port=9001")

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
    response = {
        "head": "Default Response. Cute.",
        "body": {
            "date": datetime.today(),
            "response_id": id_gen() 
        }
    }
    return response

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
