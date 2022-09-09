class Schema:
    fields = []
    def create(self, table_name, grammar):
        for i in grammar:
            self.fields.append(str(i))
        
        print("CREATE TABLE {} ({})".format(table_name, ", ".join(self.fields)))


class Blueprint:
    query = ""

    def id(self):
        self.query = "id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY"
        return self

    def string(self, name, length=255):
        self.query = "{} VARCHAR({})".format(name, length)
        return self

    def integer(self, name, length=5):
        self.query = "{} INT({})".format(name, length)
        return self

    def not_null(self):
        self.query = "{} NOT NULL".format(self.query)
        return self

    def __str__(self):
        return self.query


class Test:
    def up(self, column = Blueprint()):
        Schema().create("users", [
            column.string("username").not_null(),
            column.string("password"),
        ])

t = Test()
t.up()