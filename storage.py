NOTIZDATEI = "notes.txt"

def lade_notizen():
    try:
        with open(NOTIZDATEI, "r") as f:
            return [zeile.strip() for zeile in f.readlines()]
    except FileNotFoundError:
        print("⚠️ Hinweis: Noch keine Notizdatei vorhanden.")
        return []
    except IOError:
        print("❌ Fehler beim Lesen der Datei.")
        return []

def speichere_notizen(notizen):
    try:
        with open(NOTIZDATEI, "w") as f:
            for note in notizen:
                f.write(note + "\n")
    except IOError:
        print("❌ Fehler beim Schreiben in die Datei.")
