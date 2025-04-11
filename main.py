from storage import (
    lade_notizen,
    speichere_notizen,
    exportiere_notizen_als_json,
    exportiere_notizen_als_csv
)

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
    print("  • exit   → Beenden")
    print("  • export to .json → Exportieren als JSON-Datei")
    print("  • export to .csv  → Export als CSV-Datei\n")



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
        elif command == "export to .json":
            exportiere_notizen_als_json(notizen)
        elif command == "export to .csv":
            exportiere_notizen_als_csv(notizen)
        elif validiere_notiz(command):
            notizen.append(command)
            speichere_notizen(notizen)
        else:
            print("❓ Ungültiger Befehl oder leere Notiz.")

    print("👋 Bis bald!")

if __name__ == "__main__":
    menue_loop()
