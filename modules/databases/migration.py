class Schema:
    query = ""

    
    def create(self, grammar):
        print("CREATE TABLE users ({})".format(grammar))

class Blueprint(Schema):
    def id(self):
        self.query += "id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY"
        return self

    def string(self, name, length=255):
        self.query += "{} VARCHAR({})".format(name, length)
        return self

    def integer(self, name, length=5):
        self.query += "{} INT({})".format(name, length)
        return self

    def not_null(self):
        self.query += "{} NOT NULL".format(self.query)
        return self

class Test(Blueprint):
    def up(self):
        Schema().create([
            self.string("username").not_null(),
            self.string("password").not_null(),
        ])

t = Test()
t.up()
