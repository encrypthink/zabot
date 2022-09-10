from ast import arg
from datetime import datetime
from importlib import import_module
import importlib.util
from pathlib import Path
from modules.databases.database import Database
from modules.helpers.finder import Finder
from modules.helpers.strings import String
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
        elif command[0] in ["create", "testing", "run"]:
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
            elif command[0] == "run":
                Runner(args1=arguments[0])
        else:
            print("Incomplete command, please recheck your '{}' command must have arguments after it.".format(command[0]))

class Creator:
    def __init__(self, args1, args2):
        if args1 == "db":
            return self.__db_creator(args=args2)
        elif args1 == "controller":
            return self.__controller_creator(args=args2)
        elif args1 == "model":
            return
        elif args1 == "migration":
            return self.__migration_creator(args=args2)

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

    def __controller_creator(self, args):
        create_controller_file = open("app/controllers/" + args + ".py", "w")
        create_controller_file.write("ini controller")
        create_controller_file.close()
        print("finish create controller")

    def __migration_creator(self, args):
        date_now = datetime.now().strftime("%Y_%m_%m_%H_%M_%S")
        filename = args + "_" + date_now + ".py"
        class_name = String().snake_to_camel(args)
        create_migration_file = open("database/migrations/" + filename, "w")
        create_migration_file.write("from modules.databases.migration.migration import Migration")
        create_migration_file.write("\nfrom modules.databases.migration.src.schema import Schema")
        create_migration_file.write("\n\nclass {}({}):".format(class_name, "Migration"))
        create_migration_file.write("\n\tdef up(self):")
        create_migration_file.write("\n\t\tSchema().create({}, [".format(f'"{String().string_to_list(args)[1]}"'))
        create_migration_file.write("\n\t\t\tself.id(),")
        create_migration_file.write("\n\t\t\tself.timestamps()")
        create_migration_file.write("\n\t\t])")
        create_migration_file.write("\n\n\n\n\nup_migration = {}().up()".format(class_name))
        create_migration_file.close()
        print("finish create {} migration.".format(args))



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

class Runner:
    def __init__(self, args1):
        if args1 == "migration":
            return self.__run_migration()

    def __run_migration(self, connection = Database()):
        exist_table = connection.fetch_all("SHOW TABLES")
        migration_directory = "database/migrations/"
        all_migrations = Finder(migration_directory).get_directory_list()

        if len(exist_table) < 1:
            i = 0
            
            for migration in all_migrations:
                if "create_migrations_table" in all_migrations[i]["filename"]:
                    self.__execute_migration(all_migrations[i]["filename"], all_migrations[i]["fullpath"])
                    new_migration_list = dict(all_migrations)
                    del new_migration_list[i]
                    all_migrations = new_migration_list
                i = i+1

            i = 1
            for migration in all_migrations:
                self.__execute_migration(all_migrations[i]["filename"], all_migrations[i]["fullpath"])
                connection.syntax_execution("INSERT INTO migrations(migration, steps) VALUES ('{}', {})".format(all_migrations[i]["filename"], 1))

                i = i+1
        else:
            already_migrated = connection.fetch_all("SELECT migration FROM migrations")
            migrated = []
            
            for i in already_migrated:
                migrated.append(i[0])
            
            for migration in all_migrations:
                if all_migrations in "create_migrations_table" and all_migrations not in migrated:
                    self.__execute_migration(all_migrations[i]["filename"], all_migrations[i]["fullpath"])
                    connection.syntax_execution("INSERT INTO migrations(migration, steps) VALUES ('{}', {})".format(all_migrations[i]["filename"], 1))


    def __execute_migration(self, filename, filepath):
        spec = importlib.util.spec_from_file_location(filename, filepath)
        module = spec.loader.load_module()
        module.up_migration
            
        print("\tSuccess migrated {}".format(filename))