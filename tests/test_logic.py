import unittest
from logic import validiere_notiz

class TestValidierung(unittest.TestCase):
    def test_notiz_mit_text(self):
        """Notiz mit Inhalt soll gültig sein."""
        self.assertTrue(validiere_notiz("Einkaufen"))

    def test_leere_notiz(self):
        """Leere oder nur Leerzeichen sollen ungültig sein."""
        self.assertFalse(validiere_notiz(""))
        self.assertFalse(validiere_notiz("    "))

# Hier kannst du weitere Test-Klassen später hinzufügen,
# z. B. TestLoeschen, TestBearbeiten usw.

if __name__ == "__main__":
    unittest.main()
