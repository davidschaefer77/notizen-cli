import unittest
from logic import validiere_notiz

class TestLogic(unittest.TestCase):
    def test_valid_notiz(self):
        self.assertTrue(validiere_notiz("Einkaufen"))

    def test_leere_notiz(self):
        self.assertFalse(validiere_notiz("   "))
        self.assertFalse(validiere_notiz(""))

if __name__ == "__main__":
    unittest.main()
