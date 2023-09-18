"""
Sample Test
"""
from django.test import SimpleTestCase

from app import calc

class CalcTests(SimpleTestCase):
    
    def test_add_nums(self):
        res = calc.add(6, 6)
        self.assertEqual(res, 12)
