import json
import mysql.connector
from pathlib import Path

from modules.aprilia.result import Result


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

    def execution(self, syntax):
        connection = self.connection()
        cursor = connection.cursor()

        try:
            return cursor.execute(syntax)
        except mysql.connector.Error as e:
            print(e)
            exit()

    def fetch_all(self, syntax):
        connection = self.connection()
        cursor = connection.cursor()

        try:
            cursor.execute(syntax)
            raw_columns = [i[0] for i in cursor.description]
            raw_result = cursor.fetchall()
            return Result().result_all(raw_columns, raw_result)
        except mysql.connector.Error as e:
            print(e)
            exit()

    def syntax_execution(self, syntax):
        connection = self.connection()
        cursor = connection.cursor()

        try:
            cursor.execute(syntax)
            connection.commit()
            return cursor.rowcount
        except mysql.connector.Error as e:
            print(e)
            exit()

    def fetch_one(self, syntax):
        connection = self.connection()
        cursor = connection.cursor()

        try:
            cursor.execute(syntax)
            raw_columns = [i[0] for i in cursor.description]
            raw_result = cursor.fetchone()

            if len(raw_result) > 1:
                return Result().result_row(raw_columns, raw_result)
            else:
                return Result().result_one(raw_result)
        
        except mysql.connector.Error as e:
            print(e)
            exit()