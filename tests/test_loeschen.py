import unittest
from unittest.mock import patch
from logic import notiz_loeschen

class TestNotizLoeschen(unittest.TestCase):
    def test_gueltige_nummer(self):
        notizen = ["Eins", "Zwei", "Drei"]

        with patch("builtins.input", return_value="2"):
            neue_liste = notiz_loeschen(notizen)

        self.assertEqual(neue_liste, ["Eins", "Drei"])

    def test_ungueltige_nummer(self):
        notizen = ["Nur eine"]
        
        with patch("builtins.input", return_value="5"):
            neue_liste = notiz_loeschen(notizen)

        self.assertEqual(neue_liste, ["Nur eine"])

    def test_text_statt_zahl(self):
        notizen = ["A", "B"]

        with patch("builtins.input", return_value="abc"):
            neue_liste = notiz_loeschen(notizen)

        self.assertEqual(neue_liste, ["A", "B"])

if __name__ == "__main__":
    unittest.main()
