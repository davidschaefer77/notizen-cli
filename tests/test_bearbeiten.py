import unittest
from unittest.mock import patch
from logic import notiz_bearbeiten

class TestNotizBearbeiten(unittest.TestCase):

    def test_gueltige_bearbeitung(self):
        notizen = ["A", "B", "C"]

        with patch("builtins.input", side_effect=["2", "Beta"]):
            neue_liste = notiz_bearbeiten(notizen)

        self.assertEqual(neue_liste, ["A", "Beta", "C"])

    def test_ungueltige_nummer(self):
        notizen = ["X", "Y"]

        with patch("builtins.input", side_effect=["5", "irrelevant"]):
            neue_liste = notiz_bearbeiten(notizen)

        self.assertEqual(neue_liste, ["X", "Y"])

    def test_text_ist_leer(self):
        notizen = ["Note"]

        with patch("builtins.input", side_effect=["1", "   "]):
            neue_liste = notiz_bearbeiten(notizen)

        self.assertEqual(neue_liste, ["Note"])

    def test_ungueltige_eingabe_zahl(self):
        notizen = ["Alpha", "Beta"]

        with patch("builtins.input", side_effect=["abc", "Gamma"]):
            neue_liste = notiz_bearbeiten(notizen)

        self.assertEqual(neue_liste, ["Alpha", "Beta"])

if __name__ == "__main__":
    unittest.main()
