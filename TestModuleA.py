import unittest
from unittest.mock import Mock

from modules.ModuleA import ModuleA

"""
1. How should we be using Mocks? 
"""


### change code
class TestModuleA(unittest.TestCase):

    def testModuleA(self):
        assert isinstance(ModuleA(Mock(), Mock(), Mock(), Mock()), ModuleA)

    def testParseDelete(self):
        D = Mock()
        D.deleteData.return_value = "John,123"
        A = ModuleA(Mock(), Mock(), D, Mock())
        assert A.parseDelete(1) == True

        D.deleteData.return_value = None
        A = ModuleA(Mock(), Mock(), D, Mock())
        assert A.parseDelete(1) == False

    def testDisplayHelp(self):
        A = ModuleA(Mock(), Mock(), Mock(), Mock())
        assert A.displayHelp() == True

    def testParseLoad(self):
        B = Mock()
        B.loadFile.return_value = "John,123"
        A = ModuleA(B, Mock(), Mock(), Mock())
        assert A.parseLoad(1) == True

        B.loadFile.return_value = None
        A = ModuleA(B, Mock(), Mock(), Mock())
        assert A.parseLoad(1) == False

    def testParseAdd(self):
        D = Mock()
        D.insertData.return_value = "John,123"
        A = ModuleA(Mock(), Mock(), D, Mock())
        assert A.parseAdd("John", "123") == True

        D.insertData.return_value = None
        A = ModuleA(Mock(), Mock(), D, Mock())
        assert A.parseAdd("John", "123") == False

    def testRunSort(self):
        C = Mock()
        C.sortData.return_value = "John,123"
        A = ModuleA(Mock(), C, Mock(), Mock())
        assert A.runSort() == True

        C.sortData.return_value = None
        A = ModuleA(Mock(), C, Mock(), Mock())
        assert A.runSort() == False

    def testParseUpdate(self):
        D = Mock()
        D.updateData.return_value = "John,123"
        A = ModuleA(Mock(), Mock(), D, Mock())
        assert A.parseUpdate(1, "John", "123") == True

        D.updateData.return_value = None
        A = ModuleA(Mock(), Mock(), D, Mock())
        assert A.parseUpdate(1, "John", "123") == False


    def testRunExit(self):
        A = ModuleA(Mock(), Mock(), Mock(), Mock())
        with self.assertRaises(SystemExit):
            A.runExit()

    def testRunNoArgs(self):
        A = ModuleA(Mock(), Mock(), Mock(), Mock())
        A.run()
        return;

    def testRunHelp(self):
        A = ModuleA(Mock(), Mock(), Mock(), Mock())
        A.run("help")
        return;

    def testRunExitCLI(self):
        A = ModuleA(Mock(), Mock(), Mock(), Mock())
        with self.assertRaises(SystemExit):
            A.run("exit")



if __name__ == '__main__':
    unittest.main()
