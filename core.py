from PIL import Image
import os

# Defina a pasta de entrada e saída
input_folder = "/home/diego/Desktop/webp_to_jpeg/input_folder"
output_folder = "/home/diego/Desktop/webp_to_jpeg/output_folder"

def convert_webp_to_jpg(input_folder, output_folder):
    # Verifica se a pasta de saída existe, se não, cria
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Loop sobre os arquivos na pasta de entrada
    for filename in os.listdir(input_folder):
        if filename.endswith(".webp"):
            # Abre a imagem WebP
            img = Image.open(os.path.join(input_folder, filename))
            # Remove a extensão .webp do nome do arquivo
            filename_without_extension = os.path.splitext(filename)[0]
            # Salva a imagem como JPEG na pasta de saída
            img.save(os.path.join(output_folder, f"{filename_without_extension}.jpg"), "JPEG")
            print(f"Converted {filename} to JPEG.")


# Chama a função de conversão
convert_webp_to_jpg(input_folder, output_folder)
