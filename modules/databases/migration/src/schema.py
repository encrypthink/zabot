from modules.databases.database import Database


class Schema(Database):
    def create(self, table_name, grammar):
        syntax = "CREATE TABLE {} ({})".format(table_name, grammar[0])
        return Database().execution(syntax)