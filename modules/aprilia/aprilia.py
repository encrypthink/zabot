"""
Aprilia ORM

Start Development   : 13 September 2022
Author              : Tri Wijayanto
Github              : https://github.com/encrypthink
Description         : Aprilia is an SQL Query Builder.
"""


from abc import ABC, abstractmethod
from dataclasses import field


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

    def all(self):
        return "SELECT {} FROM {}".format(", ".join(self.fields), self.table)

    def count(self, column):
        self.syntax = "SELECT COUNT({}) FROM {}".format(column, self.table)
        return self

    def min(self, column):
        self.syntax = "SELECT MIN({}) FROM {}".format(column, self.table)
        return self

    def max(self, column):
        self.syntax = "SELECT MAX({}) FROM {}".format(column, self.table)
        return self

    def find(self, vals):
        self.syntax = "SELECT * FROM {} WHERE {} = {}".format(self.table, self.primary_key, vals)
        return self

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


        
