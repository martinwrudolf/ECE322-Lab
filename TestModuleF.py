import unittest
from modules.ModuleF import ModuleF
### change code
class MyTestCase(unittest.TestCase):

    def testModuleF(self):
        assert isinstance(ModuleF(), ModuleF)


if __name__ == '__main__':
    unittest.main()
