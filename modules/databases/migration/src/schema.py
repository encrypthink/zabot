from modules.databases.database import Database


class Schema(Database):
    def create(self, table_name, grammar):
        syntax = "CREATE TABLE {} ({})".format(table_name, grammar[0])
        return Database().execution(syntax)

    def modify(self, table_name, grammar):
        grammar_str = str(grammar[0])
        grammar_to_list = list(grammar_str.split(", "))
        extend_add = [("ADD " if "DROP" not in x else "") + x for x in grammar_to_list]
        column = ", ".join(extend_add)
        syntax = "ALTER TABLE {} {}".format(table_name, column)
        return Database().execution(syntax)
        