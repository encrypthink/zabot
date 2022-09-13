"""
Aprilia ORM

Start Development   : 13 September 2022
Author              : Tri Wijayanto
Github              : https://github.com/encrypthink
Description         : Aprilia is an object relational mapper (ORM).
"""


from abc import ABC, abstractmethod


class Aprilia(ABC):

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
        return self

    @abstractmethod
    def count(self):
        return self

    @abstractmethod
    def find(self, vals):
        return self

    @abstractmethod
    def get(self):
        return self
    
    @abstractmethod
    def select(self, columns="*"):
        return self

    @abstractmethod
    def where(self, column:str, operator, comps: str):
        return self


a = Aprilia().select().get()