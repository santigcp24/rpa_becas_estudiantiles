import pytesseract
from PIL import Image
import os

# Ruta local de instalación de Tesseract (Ajusta según tu sistema)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Directorios de entrada y salida
SCREENSHOT_FOLDER = r"C:\Users\sxc_x\OneDrive\Escritorio\rpa_becas_estudiantiles\rpa_becas_estudiantiles\screenshots"
TEXT_FOLDER = r"C:\Users\sxc_x\OneDrive\Escritorio\rpa_becas_estudiantiles\rpa_becas_estudiantiles\text_processing\text_data"
os.makedirs(TEXT_FOLDER, exist_ok=True)

# Función para procesar cada imagen
def extract_text_from_images():
    for filename in os.listdir(SCREENSHOT_FOLDER):
        if filename.endswith(".png"):  # Procesar solo imágenes PNG
            image_path = os.path.join(SCREENSHOT_FOLDER, filename)
            text_filename = filename.replace(".png", ".txt")
            text_path = os.path.join(TEXT_FOLDER, text_filename)

            # Procesar la imagen con OCR
            image = Image.open(image_path)
            extracted_text = pytesseract.image_to_string(image, lang="spa")  # Extrae en español

            # Guardar el texto en un archivo de texto
            with open(text_path, "w", encoding="utf-8") as file:
                file.write(extracted_text)

            print(f"Texto extraído de {filename} y guardado en {text_path}")

# Ejecutar la extracción de OCR
if __name__ == "__main__":
    extract_text_from_images()
