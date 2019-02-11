import unittest
from boxers import *

class TestBoxers(unittest.TestCase):

    def test_boxer1_age(self):
        self.assertEqual(first_boxer.age, 33)

    def test_boxer2_age(self):
        self.assertEqual(second_boxer.age, 28)

    def test_boxer3_age(self):
        self.assertEqual(third_boxer.age, 35)

    def test_boxer1_weight(self):
        self.assertEqual(first_boxer.weight, 78)

    def test_boxer2_weight(self):
        self.assertEqual(second_boxer.weight, 72)

    def test_boxer3_weight(self):
        self.assertEqual(third_boxer.weight, 69)

    def test_boxer1_height(self):
        self.assertEqual(first_boxer.height, 180)

    def test_boxer2_height(self):
        self.assertEqual(second_boxer.height, 185)

    def test_boxer3_height(self):
        self.assertEqual(third_boxer.height, 182)
