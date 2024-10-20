# db.py # change this name -.-

import psycopg
from dotenv import dotenv_values

config = dotenv_values(".env")


class DB:
    def __init__(self, dbname, user):
        self.conn = psycopg.connect(f"dbname={dbname} user={user}")
        self.cur  = conn.cursor()
    
    # Creates User table if one does not exist
    def createUserTable(self):
        pass
    
    # Creates clock table if one does not exist
    def createClockTable(self):
        pass

    def clockInOrOut(self):
        pass

    def getCurrentDaysHours(self):
        pass

    def getWeeklyHours(self):
        pass

    def getMonthlyHours(self):
        pass

    def getYearlyHours(self):
        pass
