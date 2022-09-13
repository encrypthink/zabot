"""
Aprilia ORM

Start Development   : 13 September 2022
Author              : Tri Wijayanto
Github              : https://github.com/encrypthink
Description         : Aprilia is an SQL Query Builder.
"""


from abc import ABC, abstractmethod


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

    @abstractmethod
    def all(self):
        self.syntax = "SELECT * FROM {}".format(self.table)
        return self

    @abstractmethod
    def count(self, column):
        self.syntax = "SELECT COUNT({}) FROM {}".format(column, self.table)
        return self

    @abstractmethod
    def min(self, column):
        self.syntax = "SELECT MIN({}) FROM {}".format(column, self.table)
        return self

    @abstractmethod
    def max(self, column):
        self.syntax = "SELECT MAX({}) FROM {}".format(column, self.table)
        return self

    @abstractmethod
    def find(self, vals):
        self.syntax = "SELECT * FROM {} WHERE {} = {}".format(self.table, self.primary_key, vals)
        return self

    @abstractmethod
    def get(self):
        return self
    
    @abstractmethod
    def select(self, columns: list):
        self.syntax = "SELECT {} ".format(", ".join(columns))
        return self

    @abstractmethod
    def where(self, column:str, operator:str, comparasion: str):
        self.syntax = "WHERE {} {} {} ".format(column, operator, comparasion)
        return self