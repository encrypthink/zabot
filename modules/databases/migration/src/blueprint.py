class Blueprint:
    def __init__(self):
        self.query = []

    def id(self):
        self.query.append("id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY")
        return self

    def string(self, name, length=255):
        self.query.append("{} VARCHAR({})".format(name, length))
        return self

    def text(self, name, length=10000):
        self.query.append("{} TEXT({})".format(name, length))
        return self

    def enum(self, name, options):
        index_options = ", ".join(f'"{option}"' for option in options)
        self.query.append("{} ENUM({})".format(name, index_options))
        return self

    def integer(self, name, length=5):
        self.query.append("{} INT({})".format(name, length))
        return self
    
    def double(self, name, length=5):
        self.query.append("{} DOUBLE({})".format(name, length))
        return self

    def not_null(self):
        count_field = len(self.query)
        index_numered = count_field - 1
        index_value = self.query[index_numered]
        self.query[index_numered] = "{} NOT NULL".format(index_value)
        return self

    def default(self, value):
        count_field = len(self.query)
        index_numered = count_field - 1
        index_value = self.query[index_numered]
        self.query[index_numered] = "{} DEFAULT '{}'".format(index_value, value)
        return self

    def timestamps(self):
        self.query.append("created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP")
        self.query.append("updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP")
        return self

    def drop_column(self, name):
        self.query.append("DROP {}".format(name))
        return self

    def after(self, name):
        count_field = len(self.query)
        index_numered = count_field - 1
        index_value = self.query[index_numered]
        self.query[index_numered] = "{} AFTER {}".format(index_value, name)
        return self

    def primary_key(self):
        count_field = len(self.query)
        index_numered = count_field - 1
        index_value = self.query[index_numered]
        self.query[index_numered] = "{} PRIMARY KEY".format(index_value)
        return self

    def set_primary_key(self, column):
        self.query.append("PRIMARY KEY({})".format(column))
        return self

    def __str__(self):
        return ", ".join(self.query)