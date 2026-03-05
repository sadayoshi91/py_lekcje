# Stwórz prostą aplikację do zarządzania listą zadań. Program
# powinien:
# Przy starcie próbować wczytać zadania z pliku zadania.json .
# Pozwalać użytkownikowi dodać nowe zadanie.
# Pozwalać wyświetlić wszystkie zadania.
# Przy zamknięciu (lub na polecenie) zapisywać aktualną listę zadań do pliku
# zadania.json .

import json
tasks = []
try:
    with open("lekcja_9/zadania.json", "r", encoding="utf-8") as file:
        tasks = json.load(file)
except FileNotFoundError:
    tasks = []
while True:
    print("1. Dodaj nowe zadanie")
    print("2. Wyświetl wszystkie zadania")
    print("3. Zakończ program")
    choice = input("Wybierz opcję: ")

    if choice == "1":
        new_task = input("Podaj nowe zadanie: ")
        tasks.append(new_task)
    elif choice == "2":
        print("Lista zadań:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")
    elif choice == "3":
        with open("lekcja_9/zadania.json", "w", encoding="utf-8") as file:
            json.dump(tasks, file, indent=4)
        print("Zadania zostały zapisane. Do widzenia!")
        break
    else:
        print("Nieprawidłowy wybór. Spróbuj ponownie.")
        input("Naciśnij Enter, aby kontynuować...")
        continue
    