from datetime import datetime 
import json
from pathlib import Path
from modules.databases.database import Database
from modules.helpers.strings import String


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
        if "create" in args:
            self.__migration_generate_create_file(args)
        elif "modify" in args:
            self.__migration_generate_modify_file(args)
        else:
            print("Illegal command, please use 'create TABLE_NAME table' if you want to create table, and use 'modify_TABLE_NAME_table' to modify your own table.")


    def __migration_generate_create_file(self, args):
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


    def __migration_generate_modify_file(self, args):
        date_now = datetime.now().strftime("%Y_%m_%m_%H_%M_%S")
        filename = args + "_" + date_now + ".py"
        class_name = String().snake_to_camel(args)
        create_migration_file = open("database/migrations/" + filename, "w")
        create_migration_file.write("from modules.databases.migration.migration import Migration")
        create_migration_file.write("\nfrom modules.databases.migration.src.schema import Schema")
        create_migration_file.write("\n\nclass {}({}):".format(class_name, "Migration"))
        create_migration_file.write("\n\tdef up(self):")
        create_migration_file.write("\n\t\tSchema().modify({}, [".format(f'"{String().string_to_list(args)[1]}"'))
        create_migration_file.write("\n\t\t])")
        create_migration_file.write("\n\n\n\n\nup_migration = {}().up()".format(class_name))
        create_migration_file.close()
        print("finish create {} migration.".format(args))