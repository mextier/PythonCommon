#https://www.youtube.com/watch?v=1Lfv5tUGsn8
#https://docs.python.org/3/library/unittest.html
#https://pythonworld.ru/moduli/modul-unittest.html


import unittest
import Utest_


class UnitTestConcrete(unittest.TestCase):
    def testgreaterthan(self):
        self.assertTrue(Utest_.isgreaterthan(2,1))
        self.assertFalse(Utest_.isgreaterthan(1,2))
        self.assertFalse(Utest_.isgreaterthan(1,1))
    def testlessthan(self):
        self.assertTrue(Utest_.islessthan(1,2))
        self.assertFalse(Utest_.islessthan(2,1))
        self.assertFalse(Utest_.islessthan(2,2))

if __name__ == '__main__':
    unittest.main()
