from django.test import TestCase
from app.calc import add

class CalcTests(TestCase):
    """Test that two numbers are added together"""


    def test_add_numbers(self):
        """Test that two numbers are added together"""
        self.assertEqual(add(3,8),11)