__author__ = 'Giovanni'

import unittest
from restomat import RestoMat

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.resto = RestoMat([5, 5, 5, 5, 5])
        self.restoInattivo = RestoMat([2,3,1])
    def test_attivazione_ok(self):
        self.assertTrue(self.resto.attivo)
    def test_attivazione_fail(self):
        self.assertFalse(self.restoInattivo.attivo)
    def test_slotesaurito_ok(self):
        self.resto.capienze[2] = 0
        self.assertTrue(self.resto.slotEsaurito(.5))
    def test_slotesaurito_fail(self):
        self.assertFalse(self.resto.slotEsaurito(.5))
    def test_calcolaresto(self):
        self.assertEqual(self.resto.calcolaResto(2.10, 5), 2.90)

if __name__ == '__main__':
    unittest.main()
