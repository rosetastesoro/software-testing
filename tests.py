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
        
    def test_boxer1_age_1(self):
        self.assertEqual(first_boxer.age, 32)

    def test_boxer1_age_2(self):
        self.assertEqual(first_boxer.age, 34)

    def test_boxer1_age_3(self):
        self.assertEqual(first_boxer.age, -33)

    def test_boxer2_age_1(self):
        self.assertEqual(second_boxer.age, 29)

    def test_boxer2_age_2(self):
        self.assertEqual(second_boxer.age, 27)

    def test_boxer2_age_3(self):
        self.assertEqual(second_boxer.age, -28)

    def test_boxer3_age_1(self):
        self.assertEqual(third_boxer.age, 36)

    def test_boxer3_age_2(self):
        self.assertEqual(third_boxer.age, 34)

    def test_boxer3_age_3(self):
        self.assertEqual(third_boxer.age, -35)

    def test_boxer1_weight_1(self):
        self.assertEqual(first_boxer.weight, 79)

    def test_boxer1_weight_2(self):
        self.assertEqual(first_boxer.weight, 77)

    def test_boxer1_weight_3(self):
        self.assertEqual(first_boxer.weight, -78)

    def test_boxer2_weight_1(self):
        self.assertEqual(second_boxer.weight, 73)

    def test_boxer2_weight_2(self):
        self.assertEqual(second_boxer.weight, 71)

    def test_boxer2_weight_3(self):
        self.assertEqual(second_boxer.weight, -72)

    def test_boxer3_weight_1(self):
        self.assertEqual(third_boxer.weight, 70)

    def test_boxer3_weight_2(self):
        self.assertEqual(third_boxer.weight, 68)

    def test_boxer3_weight_3(self):
        self.assertEqual(third_boxer.weight, -69)

    def test_boxer1_height_1(self):
        self.assertEqual(first_boxer.height, 181)

    def test_boxer1_height_2(self):
        self.assertEqual(first_boxer.height, 179)

    def test_boxer1_height_3(self):
        self.assertEqual(first_boxer.height, -180)

    def test_boxer2_height_1(self):
        self.assertEqual(second_boxer.height, 186)

    def test_boxer2_height_2(self):
        self.assertEqual(second_boxer.height, 184)

    def test_boxer2_height_3(self):
        self.assertEqual(second_boxer.height, -185)

    def test_boxer3_height_1(self):
        self.assertEqual(third_boxer.height, 183)

    def test_boxer3_height_2(self):
        self.assertEqual(third_boxer.height, 181)

    def test_boxer3_height_3(self):
        self.assertEqual(third_boxer.height, -182)

   
