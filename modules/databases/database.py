import json
import mysql.connector
from pathlib import Path


class Database:
    
    config_file = "db.config.json"

    def read_config(self):
        find_db_config = Path(self.config_file)

        if find_db_config.is_file():
            db_config = open(self.config_file, "r")
            return json.load(db_config)
        else:
            print("Database config not found")    
            exit()
    
    def connection(self):
        db_config = self.read_config()
        
        try:
            connect = mysql.connector.connect(
                host = db_config["host"],
                port = db_config["port"],
                username = db_config["username"],
                password = db_config["password"],
                database = db_config["database"]
            )
            return connect
        except mysql.connector.Error as e:
            print(e)
            exit()