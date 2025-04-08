# main.py

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

def hauptmenue():
    notizen = lade_notizen()
    print("👋 Willkommen zu Notizen-CLI!")
    
    while True:
        command = input("Neue Notiz (oder 'exit'): ")
        if command.lower() == "exit":
            break
        notizen.append(command)
        speichere_notizen(notizen)

    print("\n📝 Deine gespeicherten Notizen:")
    for note in notizen:
        print("-", note)

if __name__ == "__main__":
    hauptmenue()
