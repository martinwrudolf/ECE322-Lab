import unittest
from unittest.mock import Mock
from data.Entry import Entry
from modules.ModuleG import ModuleG

class TestModuleG(unittest.TestCase):
    def testModuleG(self):
        assert isinstance(ModuleG(), ModuleG)

    def testUpdateData(self):
        G = ModuleG()
        data = [Entry("John", "123")]
        G.updateData("dataTest.txt", data)
        with open("dataTest.txt", "r") as f:
            someEntry = f.read()
        assert someEntry ==  "John,123\n"

if __name__ == '__main__':
    unittest.main()
