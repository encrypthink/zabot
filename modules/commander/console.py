from pathlib import Path
from modules.databases.database import Database
import json


class Console(Database):

    version = "0.1 beta"

    def __init__(self, command):
        super().__init__()
        self.router(command)

    def router(self, command):
        if command[0] in ["-help", "--h"]:
            return self.helps()
        elif command[0] in ["-version", "--v"]:
            return self.__version()
        elif command[0] in ["create", "testing"]:
            return self.__command_check(command)

    def helps(self):
        file_help = Path("modules/commander/help.txt")
        if file_help.is_file():
            open_help_file = open(file_help, "r")
            print(open_help_file.read())
        else:
            print("file not found")

    def __version(self):
        print("ZaBot version {}".format(self.version))

    def __command_check(self, command):
        if len(command) > 1:
            arguments = command[1].split(":")
            if command[0] == "create":
                Creator(args1=arguments[0], args2=arguments[1])
            elif command[0] == "testing":
                Tester(args1=arguments[0], args2=arguments[1])
        else:
            print("Incomplete command, please recheck your '{}' command must have arguments after it.".format(command[0]))

class Creator:
    def __init__(self, args1, args2):
        if args1 == "db":
            return self.__db_creator(args=args2)
        elif args1 == "controller":
            return
        elif args1 == "model":
            return

    def __db_creator(self, args):
        if args == "config":
            return self.__db_config_creator()

    def __db_config_creator(self):
        check_config_file = Path(Database().config_file)

        if check_config_file.is_file():
            print("Your database configuration already exist.")
        else:
            host = input("host: ")
            port = input("port ('default: 3306'): ")
            username = input("username: ")
            password = input("password: ")
            database = input("database: ")
            
            config = {
                "host": host,
                "port": int(port),
                "username": username,
                "password": password,
                "database": database
            }

            config_to_json = json.dumps(config)
            
            create_config_file = open("db.config.json", "w")
            create_config_file.write(config_to_json)
            create_config_file.close()

            print("database configuration successfully created, please run 'commander.py testing db:config' to make sure you are connected to your database")


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