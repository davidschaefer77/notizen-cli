import json
import csv


NOTIZDATEI = "notes.txt"

def lade_notizen() -> list[str]:
    """Lädt die gespeicherten Notizen aus der Datei."""
    try:
        with open(NOTIZDATEI, "r") as f:
            return [zeile.strip() for zeile in f.readlines()]
    except FileNotFoundError:
        print("⚠️ Noch keine Notizdatei vorhanden – starte neu.")
        return []
    except IOError:
        print("❌ Fehler beim Lesen der Datei.")
        return []

def speichere_notizen(notizen: list[str]) -> None:
    """Speichert alle Notizen in die Datei."""
    try:
        with open(NOTIZDATEI, "w") as f:
            for note in notizen:
                f.write(note + "\n")
    except IOError:
        print("❌ Fehler beim Schreiben in die Datei.")

def exportiere_notizen_als_json(notizen: list[str], dateiname: str = "notizen.json") -> None:
    """Speichert die Notizen als JSON-Datei."""
    try:
        with open(dateiname, "w", encoding="utf-8") as f:
            json.dump({"notizen": notizen}, f, indent=2, ensure_ascii=False)
        print(f"✅ Notizen erfolgreich in {dateiname} exportiert.")
    except IOError:
        print("❌ Fehler beim Exportieren der JSON-Datei.")

def exportiere_notizen_als_csv(notizen: list[str], dateiname: str = "notizen.csv") -> None:
    """Exportiert Notizen als CSV-Datei mit Nummerierung."""
    try:
        with open(dateiname, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Nr", "Notiz"])  # Kopfzeile

            for i, note in enumerate(notizen, start=1):
                writer.writerow([i, note])

        print(f"✅ Notizen erfolgreich in {dateiname} exportiert.")
    except IOError:
        print("❌ Fehler beim Exportieren der CSV-Datei.")

