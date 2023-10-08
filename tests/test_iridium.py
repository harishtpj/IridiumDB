import pytest
from db.iridium import Iridium, IrDbError, IrKeyError, IrCommitError

# Test the Iridium class
class TestIridium:
    # Setup method to create an instance of Iridium for testing
    def setup_method(self):
        self.db = Iridium()
        self.perdb = Iridium("samples/testdb")

    # Test if reading a nonexistent db raises Error
    def test_read_nonexistent_db(self):
        with pytest.raises(IrDbError):
            Iridium("nonexistent")

    # Test the set() and get() methods
    def test_set_and_get(self):
        self.db.set("key1", "value1")
        assert self.db.get("key1") == "value1"

    # Test the delete() method
    def test_delete(self):
        self.db.set("key2", "value2")
        self.db.delete("key2")
        assert self.db.get("key2") == None

    # Test the commit() method
    def test_commit(self):
        with pytest.raises(IrCommitError):
            self.db.commit()

    # Test the __getitem__() and __setitem__() methods
    def test_getitem_and_setitem(self):
        self.perdb["key3"] = "value3"
        assert self.perdb["key3"] == "value3"

    # Test the __delitem__() method
    def test_delitem(self):
        self.perdb["key4"] = "value4"
        del self.perdb["key4"]
        with pytest.raises(IrKeyError):
            self.perdb["key4"]

    # Test the __repr__() method
    def test_repr(self):
        self.db.set("key1", "value1")
        assert repr(self.db) == "{'key1': 'value1'}"

    # Test the __str__() method
    def test_str(self):
        dbid = id(self.db)
        assert str(self.db) == f"IridiumDB instance <Temp> at 0x{dbid:x}"

# Run the tests
if __name__ == "__main__":
    pytest.main()