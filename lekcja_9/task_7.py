# Użyj modułu pathlib , aby napisać skrypt, który tworzy
# strukturę folderów: Projekt/src , Projekt/data , Projekt/docs 

from pathlib import Path    

# Tworzenie struktury folderów
Path("Projekt/src").mkdir(parents=True, exist_ok=True)
Path("Projekt/data").mkdir(parents=True, exist_ok=True) 
Path("Projekt/docs").mkdir(parents=True, exist_ok=True)
print("Struktura folderów została utworzona.")
