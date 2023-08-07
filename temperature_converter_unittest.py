import unittest
from temperature_converter import *

class TestConverter(unittest.TestCase):

    def test_fahrenheit_to_celsius(self):
        # Test freezing temperature
        self.assertEqual(f_to_c(32), 0)
        # Test boiling temperature
        self.assertEqual(f_to_c(212), 100)
        # Test float
        self.assertAlmostEqual(f_to_c(31.0), -0.5555555555)
        # Test errors
        self.assertRaises(TypeError, f_to_c, 'freezing')
    
    def test_celsius_to_farenheit(self):
        self.assertEqual
unittest.main()