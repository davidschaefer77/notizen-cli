# logic.py

def validiere_notiz(notiz: str) -> bool:
    """Leere Notizen oder nur Leerzeichen sind ungültig."""
    return bool(notiz.strip())

def formatiere_ausgabe(notizen: list[str]) -> None:
    """Gibt die Notizen hübsch aus."""
    print("\n📝 Deine gespeicherten Notizen:")
    for i, note in enumerate(notizen, start=1):
        print(f"{i}. {note}")

def notiz_loeschen(notizen: list[str]) -> list[str]:
    """Löscht eine Notiz basierend auf Nummerneingabe."""
    try:
        nummer = int(input("Welche Notiznummer möchtest du löschen? "))
        if 1 <= nummer <= len(notizen):
            geloescht = notizen.pop(nummer - 1)
            print(f"🗑️  Notiz gelöscht: {geloescht}")
        else:
            print("❌ Ungültige Nummer.")
    except ValueError:
        print("⚠️ Bitte eine gültige Zahl eingeben.")
    
    return notizen

