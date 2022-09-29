from datetime import date, datetime, timedelta
import json
from time import strftime
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
            cols_name = [i[0] for i in cursor.description]
            raw_result = cursor.fetchall()
            result: list() = []

            i = 0
            for row in raw_result:
                in_row: dict() = {}
                j = 0
                for val in row:
                    if type(val) == datetime:
                        in_row[cols_name[j]] = val.strftime("%Y-%m-%d %H:%M:%S")
                    elif type(val) == date:
                        in_row[cols_name[j]] = val.strftime("%Y-%m-%d")
                    elif type(val) == timedelta:
                        in_row[cols_name[j]] = str(val)
                    else:
                        in_row[cols_name[j]] = val
                    j = j+1

                result.append(in_row)
                i = i+1

            return result

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
            result = cursor.fetchone()
            return result[0]
        except mysql.connector.Error as e:
            print(e)
            exit()