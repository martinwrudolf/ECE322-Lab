import unittest
from unittest.mock import Mock
from data.Entry import Entry
from modules.ModuleB import ModuleB

### change code
class TestModuleB(unittest.TestCase):

    def testModuleB(self):
        assert isinstance(ModuleB(Mock()), ModuleB)


    def testLoadFile(self):
        B = ModuleB(Mock())
        assert B.loadFile("../data.txt") == [Entry("Jeremy", "1234"),
                                             Entry("Morris", "0623"),
                                             Entry("Quinn", "3847"),
                                             Entry("JJJ", "1234"),
                                             Entry("Thomas", "777222"),
                                             Entry("Frank", "123456789789"),
                                            ]


if __name__ == '__main__':
    unittest.main()
