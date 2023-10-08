# The errors module - Contains error for IridiumDB

class IrKeyError(Exception):
    def __init__(self, key, db):
        super().__init__(f"Key '{key}' not found in <{db}> Database")

class IrCommitError(Exception):
    def __init__(self, msg=None):
        if msg == "tmp":
            super().__init__("Can't commit a temporary database")
        else:
            super().__init__(msg)

class IrDbError(Exception):
    def __init__(self, db):
        super().__init__(f"Database '{db}' not found")