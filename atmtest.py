import unittest
from atm import *


class Test_atm(unittest.TestCase):

    def test_atm_balance(self):
        self.assertEqual(Atm.atm_balance, 10000)

    def test_atm_balance_2(self):
        self.assertEqual(Atm.atm_balance, 10001)

    def test_atm_balance_3(self):
        self.assertEqual(Atm.atm_balance, 9999)

    def test_atm_attempts(self):
        self.assertEqual(Atm.attempts, 2)

    def test_rise_money(self):
        self.assertEqual(Atm.rise_money(100), 10100)
