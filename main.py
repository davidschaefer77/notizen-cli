from storage import lade_notizen, speichere_notizen
from logic import (
    validiere_notiz,
    formatiere_ausgabe,
    notiz_loeschen,
    notiz_suchen,
    notiz_bearbeiten,
)

def begruessung():
    print("👋 Willkommen zu Notizen-CLI!")
    print("Tippe eine Notiz, oder nutze:")
    print("  • delete → Notiz löschen")
    print("  • edit   → Notiz bearbeiten")
    print("  • search → Notiz suchen")
    print("  • exit   → Beenden\n")

def menue_loop():
    notizen = lade_notizen()
    begruessung()

    while True:
        command = input("📝 Neue Notiz oder Befehl: ").strip().lower()

        if command == "exit":
            break
        elif command == "delete":
            notizen = notiz_loeschen(notizen)
            speichere_notizen(notizen)
        elif command == "edit":
            notizen = notiz_bearbeiten(notizen)
            speichere_notizen(notizen)
        elif command == "search":
            notiz_suchen(notizen)
        elif validiere_notiz(command):
            notizen.append(command)
            speichere_notizen(notizen)
        else:
            print("❓ Ungültiger Befehl oder leere Notiz.")

    print("👋 Bis bald!")

if __name__ == "__main__":
    menue_loop()
