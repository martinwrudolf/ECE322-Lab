import unittest
from modules.ModuleE import ModuleE

class TestModuleE(unittest.TestCase):
    def testModuleE(self):
        assert isinstance(ModuleE(), ModuleE)


    def testExitProgram(self):
        module_e = ModuleE()
        with self.assertRaises(SystemExit):
            module_e.exitProgram()

if __name__ == '__main__':
    unittest.main()
