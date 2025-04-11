import unittest
from unittest.mock import patch
from logic import notiz_suchen

class TestNotizSuchen(unittest.TestCase):

    def test_suchbegriff_wird_gefunden(self):
        notizen = ["Python lernen", "Milch kaufen", "python üben"]

        with patch("builtins.input", return_value="python"), \
             patch("builtins.print") as mock_print:
            notiz_suchen(notizen)

        ausgaben = [call.args[0] for call in mock_print.call_args_list]
        treffer = [zeile for zeile in ausgaben if "python" in zeile.lower()]

        self.assertEqual(len(treffer), 2)

    def test_suchbegriff_nicht_vorhanden(self):
        notizen = ["Haus putzen", "Wäsche waschen"]

        with patch("builtins.input", return_value="urlaub"), \
             patch("builtins.print") as mock_print:
            notiz_suchen(notizen)

        ausgaben = [call.args[0] for call in mock_print.call_args_list]
        keine_treffer = any("Keine Notiz gefunden" in zeile for zeile in ausgaben)

        self.assertTrue(keine_treffer)

if __name__ == "__main__":
    unittest.main()
