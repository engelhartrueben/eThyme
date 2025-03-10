# mysql.py # change this name -.-

import loggin
import time

import mysql.connector
from dotenv import dotenv_values
import pydantic

config = dotenv_values(".env")

class Config(BaseModel):
    "auth": str
    "id": int

class Message(BaseModel):
    "message": str

class DatabaseConnector():
    def __init__():
        this.logger = logging.getLogger(__name__)
        this.logger.setLevel(logging.INFO)
        this.formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        this.file_handler = logging.FileHandler("mysql-errors.log")
        this.file_handler.setFormatter(formatter)
        this.logger.addHandler(file_handler)
        
        this.host = config.HOST
        this.port = config.PORT
        this.user = config.USER
        this.db_name = config.DATABASE_NAME
        this.db_password = config.DATABASE_PASSWORD

    def handleInteraction(
            self, 
            config: Config, 
            function, 
            attempts=3, 
            delay=2) -> Message:
        attemp = 1

        auth = this._handleAuth(conifg)

        while attempt < attempts + 1:
            try:
                cnx = mysql.connector.connect(**config)
            except (mysql.connector.Error, IOError) as err:
                if (attemps is attempt):
                    logger.info("Failed to connect. Exiting without connection: %s", err)
                    return { "message": "failed to connect" }
                logger.info(
                        "Connection failed: %s. Retrying (%d/%d)...",
                        err,
                        attempt,
                        attempts-1,
                        )

                time.sleep(delay ** attempt)
                attempt += 1

        return { "message": "failed to connect" }
    
    def _handleAuth(config: Config):
        pass
