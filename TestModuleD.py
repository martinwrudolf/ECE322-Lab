import unittest
from unittest.mock import Mock
from data.Entry import Entry
from modules.ModuleD import ModuleD

class TestModuleD(unittest.TestCase):
    def testModuleD(self):
        assert isinstance(ModuleD(Mock(), Mock()), ModuleD)


    def testInsertData(self):
        D = ModuleD(Mock(), Mock())
        data = []
        filename = "dataTest.txt"
        assert D.insertData(data, "John", "123", filename) == [Entry("John", "123")]

    def testUpdateData(self):
        D = ModuleD(Mock(), Mock())
        data = [Entry("Jogn", "123")]
        filename = "dataTest.txt"
        assert D.updateData(data, 0, "John", "123", filename) == [Entry("John", "123")]

    def testDeleteData(self):
        D = ModuleD(Mock(), Mock())
        data = [Entry("John", "123")]
        filename = "dataTest.txt"
        assert D.deleteData(data, 0, filename) == []



if __name__ == '__main__':
    unittest.main()
