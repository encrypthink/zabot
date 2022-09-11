from modules.databases.database import Database
from pathlib import Path

class Tester:
    def __init__(self, args1, args2):
        if args1 == "db":
            return self.__db_tester(args=args2)

    def __db_tester(self, args):
        if args == "config":
            self.__db_connection_tester()

    def __db_connection_tester(self):
        check_config_file = Path(Database().config_file)
        if check_config_file.is_file():
            if Database().connection().is_connected():
                print("Success to connect")
        else:
            print("Your config not found, please create your database configuration using 'command.py create db:config'.")