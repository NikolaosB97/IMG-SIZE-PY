from PIL import Image
import os

def resize_images(folder, new_size):
    files = sorted(os.listdir(folder))  # Ordina i file per nome
    for filename in files:
        file_path = os.path.join(folder, filename)
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            print(f"Trovato file: {filename}")  # Messaggio di debug
            with Image.open(file_path) as img:
                img = img.resize(new_size, Image.LANCZOS)
                img.save(file_path)
                print(f"Immagine {filename} ridimensionata e salvata in {folder}.")


folder = 'NICOLA' 
new_size = (1500, 1500)  

resize_images(folder, new_size)