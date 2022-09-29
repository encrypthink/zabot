"""
Aprilia Query Builder

Start Development   : 13 September 2022
Author              : Tri Wijayanto
Github              : https://github.com/encrypthink
Description         : Aprilia is an SQL Query Builder.
"""


from abc import ABC, abstractmethod
from modules.databases.database import Database


class Aprilia(ABC):

    syntax = ""

    @property
    @abstractmethod
    def table(self) -> str:
        """
        Get table name from child of models class
        return String
        """
        
    @property
    @abstractmethod
    def fields(self) -> list:
        """
        Get fields from child of models class
        return List
        """

    @property
    @abstractmethod
    def primary_key(self) -> str:
        """
        Get table primary key from child of models class
        return String
        """

    def all(self) -> list:
        query = "SELECT * FROM {}".format(self.table)
        return Database().fetch_all(query)

    def count(self, column) -> int:
        query = "SELECT COUNT({}) FROM {}".format(column, self.table)
        return Database().fetch_one(query)

    def sum(self, column) -> int:
        query = "SELECT SUM({}) FROM {}".format(column, self.table)
        return Database().fetch_one(query)

    def min(self, column):
        self.syntax = "SELECT MIN({}) FROM {}".format(column, self.table)
        return self

    def max(self, column):
        self.syntax = "SELECT MAX({}) FROM {}".format(column, self.table)
        return self

    def find(self, vals) -> dict:
        query = "SELECT * FROM {} WHERE {} = {}".format(self.table, self.primary_key, vals)
        return Database().fetch_one(query)

    def get(self):
        return self
    
    def select(self, columns: list):
        self.syntax = "SELECT {} ".format(", ".join(columns))
        return self

    def where(self, column:str, operator:str, comparasion: str):
        self.syntax = "WHERE {} {} {} ".format(column, operator, comparasion)
        return self

    def add(self, insert: dict):
        fields: tuple = []
        values: tuple = []

        for i in insert: fields.append(i)
        for i in insert: 
            if isinstance(insert[i], str):
                values.append(f'"{insert[i]}"')
            else:
                values.append(insert[i])

        return "INSERT INTO {} ({}) VALUES ({})".format(self.table, ", ".join(fields), ", ".join(map(str, values)))

    def insert(self, insert: dict):
        fields: tuple = []
        values: tuple = []

        for i in insert: fields.append(i)
        for i in insert: 
            if isinstance(insert[i], str):
                values.append(f'"{insert[i]}"')
            else:
                values.append(insert[i])

        return "INSERT INTO {} ({}) VALUES ({})".format(self.table, ", ".join(fields), ", ".join(map(str, values)))
        
        
