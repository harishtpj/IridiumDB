# The IridiumDB class.
from .errors import *

import pprint
import yaml

try:
    from yaml import CSafeLoader as SafeLoader
    from yaml import CSafeDumper as SafeDumper
except ImportError:
    from yaml import SafeLoader
    from yaml import SafeDumper

DBEXT = '.yml'

class Iridium:
    def __init__(self, db_name=None):
        if db_name is not None:
            self.__dbname = db_name
            try:
                with open(db_name + DBEXT, "r") as stream:
                    self.__db = yaml.load(stream, Loader=SafeLoader)
            except FileNotFoundError:
                raise IrDbError(db_name) from None
        else:
            self.__dbname = "<Temp>"
            self.__db = {}

    def get(self, key):
        return self.__db.get(key)
    
    def set(self, key, value):
        self.__db[key] = value
    
    def delete(self, key):
        if key not in self.__db:
            raise IrKeyError(key, self.__dbname)
        del self.__db[key]
    
    def commit(self):
        if self.__dbname == "<Temp>":
            raise IrCommitError("tmp")
        with open(self.__dbname + DBEXT, "w") as stream:
            yaml.dump(self.__db, stream, Dumper=SafeDumper)
    
    def __getitem__(self, key):
        value = self.get(key)
        if value is None:
            raise IrKeyError(key, self.__dbname)
        return value
    
    def __setitem__(self, key, value):
        self.set(key, value)
        self.commit()
    
    def __delitem__(self, key):
        self.delete(key)
        self.commit()
    
    def __repr__(self):
        return pprint.pformat(self.__db)
    
    def __str__(self):
        return f"IridiumDB instance {self.__dbname} at 0x{id(self):x}"