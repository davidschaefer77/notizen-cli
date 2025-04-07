# main.py

notes = []

while True:
    command = input("Neue Notiz (oder 'exit' zum Beenden): ")
    if command == "exit":
        break
    notes.append(command)

print("\nDeine Notizen:")
for note in notes:
    print("-", note)
