# main.py

from storage import lade_notizen, speichere_notizen

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
