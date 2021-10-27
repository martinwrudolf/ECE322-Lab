import unittest
import mybisect

class MyTestCase(unittest.TestCase):

    """
    Constructors can be tested on either the (tolerance and maxiterations), the printed output (using assertEquals) and
    or assertIsInstance.
    """
    def test3args(self):
        f = mybisect.Polynomial(1, -1)
        b = mybisect.MyBisect(0.00001, 50, f)
        root = b.run(-1, 1)
        self.assertEqual(b._tolerance, 0.00001)
        self.assertEqual(b._maxIterations, 50)
        self.assertEqual(b._func, f)
        self.assertAlmostEqual(root, 1, 4)



    def test2argsFloat(self):
        f = mybisect.Polynomial(1, -1)
        b = mybisect.MyBisect(0.0001, f)
        root = b.run(-1, 1)
        # self.assertAlmostEqual(root, 1, 4)
        self.assertEqual(b._tolerance, 0.0001)
        self.assertEqual(b._maxIterations, 50)
        self.assertEqual(b._func, f)


    def test2argsInt(self):
        f = mybisect.Polynomial(1, -1)
        b = mybisect.MyBisect(50, f)
        root = b.run(-1, 1)
        self.assertAlmostEqual(root, 1 - b._tolerance, 5)
        self.assertEqual(b._tolerance, 0.000001)
        self.assertEqual(b._maxIterations, 50)
        self.assertEqual(b._func, f)

    def test1arg(self):
        f = mybisect.Polynomial(1, -1)
        b = mybisect.MyBisect(f)
        root = b.run(-1, 1)
        self.assertAlmostEqual(root, 1 - 0.000001, 5)
        self.assertEqual(b._tolerance, 0.000001)
        self.assertEqual(b._maxIterations, 50)
        self.assertEqual(b._func, f)

    def testOtherConstructor(self):
        f = mybisect.Polynomial(1, -1)
        b = mybisect.MyBisect(1, 1, 1, f)
        # root = b.run(-1, 1)
        self.assertRaises(TypeError, lambda: b.run(-1,1))
        # self.assertEqual(root, 1)
        self.assertEqual(b._tolerance, 0.000001)
        self.assertEqual(b._maxIterations, 50)
        self.assertEqual(b._func, None)


    def testToleranceGetter(self):
        f = mybisect.Polynomial(1, -1)
        b = mybisect.MyBisect(f)
        self.assertEqual(b.tolerance, 0.000001)

    # def testToleranceSetter(self):
    #     f = mybisect.Polynomial(1, -1)
    #     b = mybisect.MyBisect(f)
    #     b.tolerance(1)
    #     self.assertEqual(b.tolerance(1), 1)

    def testMaxIterationsGetter(self):
        f = mybisect.Polynomial(1, -1)
        b = mybisect.MyBisect(f)
        self.assertEqual(b.maxIterations, 50)

    # def testMaxIterationsSetter(self):
    #     f = mybisect.Polynomial(1, -1)
    #     b = mybisect.MyBisect(f)
    #     b.maxIterations(10)
    #     self.assertEqual(b._maxIterations, 10)

    def testRootNotFound(self):
        f = mybisect.Polynomial(1, 1, 1)
        b = mybisect.MyBisect(f)
        self.assertRaises(ValueError, lambda: b.run(-1, 1))
        f = mybisect.Polynomial(1, -1)
        b = mybisect.MyBisect(1, f)
        self.assertRaises(ValueError, lambda: b.run(-100, 100))

if __name__ == '__main__':
    unittest.main()
