import os
from data_extraction.scraping_becas import scrap as ejecutar_scraping
from data_extraction.scraping_becas_2 import ejecutar_scraping as scraping_becas
from text_processing.ocr_extraccion import extract_text_from_images
from database.load_text import load_texts_to_db
from database.load_text import create_db


def main():
    try:
        print("\n🚀 Iniciando proceso de extracción de becas...\n")
        
        # ✅ 1. Realizar Web Scraping y tomar capturas de pantalla
        print("\n🔍 Ejecutando Web Scraping y capturando pantallas...\n")
        scraping_becas()
        ejecutar_scraping()
        
        
        # ✅ 2. Extraer texto de las capturas de pantalla
        print("\n📄 Extrayendo texto de las imágenes capturadas...\n")
        extract_text_from_images()

        # ✅ 3. Almacenar el texto extraído en la base de datos
        print("\n📂 Cargando información extraída a la base de datos...\n")
        create_db()
        load_texts_to_db()
        
        print("\n🎉 Proceso completado con éxito. Los datos están almacenados en la base de datos.\n")

    except Exception as e:
        raise (e)
if __name__ == "__main__":
    main()
