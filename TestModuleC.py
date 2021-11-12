import unittest
from unittest.mock import Mock
from data.Entry import Entry
from modules.ModuleC import ModuleC


class TestModuleC(unittest.TestCase):
    def testModuleC(self):
        assert isinstance(ModuleC(Mock()), ModuleC)


    def testSortData(self):
        F = Mock()
        C = ModuleC(F)
        assert C.sortData([Entry("A", "1"), Entry("B", "2")]) == [Entry("A", "1"), Entry("B", "2")]

if __name__ == '__main__':
    unittest.main()
