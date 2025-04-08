# storage.py

NOTIZDATEI = "notes.txt"

def lade_notizen():
    try:
        with open(NOTIZDATEI, "r") as f:
            return [zeile.strip() for zeile in f.readlines()]
    except FileNotFoundError:
        return []

def speichere_notizen(notizen):
    with open(NOTIZDATEI, "w") as f:
        for note in notizen:
            f.write(note + "\n")
