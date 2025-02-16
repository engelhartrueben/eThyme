# db.py # change this name -.-

import psycopg
from dotenv import dotenv_values

config = dotenv_values(".env")


class DB:
    def __init__(self, dbname, user):
        self.conn = psycopg.connect(f"dbname={config.DB_NAME} user={config.USER}")
        self.cur  = conn.cursor()
    
    # Creates User table if one does not exist
    def createUserTable(self):
        com = '''CREATE TABLE User (
           id serial NOT NULL PRIMARY KEY, 
           first_name NOT NULL varchar(255),
           last_name NOT NULL varchar(255),
           organization NOT NULL varchar(255),
           rate_of_pay NOT NULL float(4,2),
           date_created NOT NULL date);
        )''' 
        pass
    
    # Creates clock table if one does not exist
    def createClockTable(self):
        com = '''CREATE TABLE Clock_In (
           id serial NOT NULL PRIMARY KEY,
           user_id int FOREIGN KEY REFERENCES User(id),
           clock_in DATETIME(), 
           clock_out DATETIME(), 
           total TIME(),
           description TEXT(400));
        '''
        pass

    def clockIn(self,user_id,clock_in):
        com =  'INSERT INTO Clock_In(user_id,clock_in)'+
              f' VALUES({user_id},{clock_in});'
        pass

    def clockOut(self,id,user_id,clock_out,description):
        # Checks that both user_id and id match 
        com = 'UPDATE Clock_in ' +
              f'SET clock_out={clock_out}, ' +
              f'description={description} ' +
              f'WHERE user_id={user_id} AND ' +
              f'WHERE id={id};'
        pass

    def getCurrentDaysHours(self):
        pass

    def getWeeklyHours(self):
        pass

    def getMonthlyHours(self):
        pass

    def getYearlyHours(self):
        pass

    def getAllTimeHours(self):
        pass
