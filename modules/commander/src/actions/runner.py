from asyncore import read
from cgi import print_directory
from modules.databases.database import Database
from modules.helpers.finder import Finder
import importlib.util


class Runner:
    def __init__(self, args1):
        if args1 == "migration":
            return self.__run_migration()

    def __run_migration(self, connection = Database()):
        exist_table = connection.fetch_all("SHOW TABLES")
        migration_directory = "database/migrations/"
        all_migrations = Finder(migration_directory).get_directory_list()

        if len(exist_table) < 1:
            
            for migration in all_migrations:
                if "create_migrations_table" in all_migrations[migration]["filename"]:
                    self.__execute_migration(all_migrations[migration]["filename"], all_migrations[migration]["fullpath"])
                    new_migration_list = dict(all_migrations)
                    del new_migration_list[migration]
                    all_migrations = new_migration_list

            for migration in all_migrations:
                self.__execute_migration(all_migrations[migration]["filename"], all_migrations[migration]["fullpath"])
                connection.syntax_execution("INSERT INTO migrations(migration, steps) VALUES ('{}', {})".format(all_migrations[migration]["filename"], 1))

        else:
            already_migrate = connection.fetch_all("SELECT migration FROM migrations")
            steps = connection.fetch_one("SELECT max(steps) from migrations")[0] + 1
            migration_in_directory = []
            migrated_list = []
            ready_to_migrated = []
        
            for i in already_migrate: migrated_list.append(i[0])
            
            i = 0
            for migration in all_migrations:
                if "create_migrations_table" not in all_migrations[i]["filename"]:
                    migration_in_directory.append(all_migrations[i]["filename"])
                i = i+1

            for i in migration_in_directory:
                if i not in migrated_list:
                    ready_to_migrated.append(i)

            if len(ready_to_migrated) > 0:            
                i = 0
                for migration in all_migrations:
                    if all_migrations[i]["filename"] in ready_to_migrated:
                        self.__execute_migration(all_migrations[i]["filename"], all_migrations[i]["fullpath"])
                        connection.syntax_execution("INSERT INTO migrations(migration, steps) VALUES ('{}', {})".format(all_migrations[i]["filename"], steps))
                    i = i+1
            else:
                print("Nothing migrated")

                
    def __execute_migration(self, filename, filepath):
        spec = importlib.util.spec_from_file_location(filename, filepath)
        module = spec.loader.load_module()
        module.up_migration
            
        print("\tSuccess migrated {}".format(filename))