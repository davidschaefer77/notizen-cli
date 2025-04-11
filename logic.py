# logic.py

def validiere_notiz(notiz: str) -> bool:
    """Prüft, ob eine Notiz gültig ist (nicht leer oder nur Leerzeichen)."""
    return bool(notiz.strip())


def formatiere_ausgabe(notizen: list[str]) -> None:
    """Gibt alle Notizen formatiert mit Nummerierung aus."""
    print("\n📝 Deine gespeicherten Notizen:")
    for i, note in enumerate(notizen, start=1):
        print(f"{i}. {note}")


def notiz_suchen(notizen: list[str]) -> None:
    """Sucht nach Notizen, die ein bestimmtes Stichwort enthalten."""
    suchwort = input("🔎 Suchbegriff eingeben: ").strip().lower()
    treffer = [note for note in notizen if suchwort in note.lower()]

    if treffer:
        print("\n✅ Gefundene Notizen:")
        for i, note in enumerate(treffer, start=1):
            print(f"{i}. {note}")
    else:
        print("❌ Keine Notiz gefunden.")


def notiz_loeschen(notizen: list[str]) -> list[str]:
    """Löscht eine Notiz anhand der eingegebenen Nummer."""
    try:
        nummer = int(input("🗑️ Welche Notiznummer möchtest du löschen? "))
        if 1 <= nummer <= len(notizen):
            geloescht = notizen.pop(nummer - 1)
            print(f"✅ Notiz gelöscht: {geloescht}")
        else:
            print("❌ Ungültige Nummer.")
    except ValueError:
        print("⚠️ Bitte eine gültige Zahl eingeben.")
    except IndexError:
        print("❌ Diese Notiz existiert nicht.")
    return notizen


def notiz_bearbeiten(notizen: list[str]) -> list[str]:
    """Bearbeitet eine Notiz anhand der Nummer."""
    try:
        nummer = int(input("📝 Welche Notiz möchtest du bearbeiten? "))
        if 1 <= nummer <= len(notizen):
            print(f"Aktuelle Notiz: {notizen[nummer - 1]}")
            neuer_text = input("✏️ Neuer Text: ").strip()
            if neuer_text:
                notizen[nummer - 1] = neuer_text
                print("✅ Notiz aktualisiert.")
            else:
                print("⚠️ Kein Text eingegeben – nichts geändert.")
        else:
            print("❌ Ungültige Notiznummer.")
    except ValueError:
        print("⚠️ Bitte gib eine Zahl ein.")
    except IndexError:
        print("❌ Diese Notiz existiert nicht.")
    return notizen
