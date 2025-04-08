# storage.py

NOTIZDATEI = "notes.txt"

def lade_notizen():
    try:
        with open(NOTIZDATEI, "r") as datei:
            return [zeile.strip() for zeile in datei.readlines()]
    except FileNotFoundError:
        return []

def speichere_notizen(notizen):
    with open(NOTIZDATEI, "w") as datei:
        for note in notizen:
            datei.write(note + "\n")
