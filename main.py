import os
import shutil

# Estensioni e categorie
EXT_CATEGORIES = {
    "Immagini": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documenti": [".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".txt"],
    "Video": [".mp4", ".mov", ".avi", ".mkv"],
    "Audio": [".mp3", ".wav", ".ogg"],
    "Archivi": [".zip", ".rar", ".7z", ".tar", ".gz"]
}

def get_category(extension):
    for category, extensions in EXT_CATEGORIES.items():
        if extension.lower() in extensions:
            return category
    return "Altro"

def organizza_cartella(percorso):
    for filename in os.listdir(percorso):
        file_path = os.path.join(percorso, filename)

        if os.path.isfile(file_path):
            _, ext = os.path.splitext(filename)
            categoria = get_category(ext)

            nuova_cartella = os.path.join(percorso, categoria)
            os.makedirs(nuova_cartella, exist_ok=True)

            nuovo_percorso = os.path.join(nuova_cartella, filename)
            shutil.move(file_path, nuovo_percorso)
            print(f"Spostato: {filename} → {categoria}/")

if __name__ == "__main__":
    cartella = input("Inserisci il percorso della cartella da organizzare: ").strip()
    if os.path.exists(cartella):
        organizza_cartella(cartella)
        print("Fatto! Cartella organizzata.")
    else:
        print("Percorso non valido.")
