# main.py

from storage import lade_notizen, speichere_notizen
from logic import validiere_notiz, formatiere_ausgabe, notiz_loeschen, notiz_suchen, notiz_bearbeiten

def hauptmenue():
    notizen = lade_notizen()
    print("👋 Willkommen zu Notizen-CLI!")

    while True:
        command = input("Neue Notiz (oder 'exit', 'delete', 'search', 'edit'): ")
        
        if command.lower() == "exit":
            break
        elif command.lower() == "delete":
            notizen = notiz_loeschen(notizen)
            speichere_notizen(notizen)
        elif command.lower() == "search":
            notiz_suchen(notizen)
        elif command.lower() == "edit":
            notizen = notiz_bearbeiten(notizen)
            speichere_notizen(notizen)
        elif validiere_notiz(command):
            notizen.append(command)
            speichere_notizen(notizen)
        else:
            print("❓ Unbekannter Befehl. Erlaubt sind: exit, delete, edit, search oder direkt eine Notiz.")

    formatiere_ausgabe(notizen)

if __name__ == "__main__":
    hauptmenue()
