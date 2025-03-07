import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import sqlite3

# Carpeta donde se almacenarán los archivos de texto extraídos
TEXT_FOLDER = r"C:\Users\sxc_x\OneDrive\Escritorio\rpa_becas_estudiantiles\text_processing\text_data"
os.makedirs(TEXT_FOLDER, exist_ok=True)

# Diccionario que asocia URLs con selectores específicos de scraping
URL_FUNCTIONS = {
    "https://web.icetex.gov.co/es/-/2024-maestrias-en-diferentes-areas-en-whitecliffe-college": ("scrape_whitecliffe", "fragment-0-ckxq", "fragment-0-ckxq", "#content"),
    "https://web.icetex.gov.co/es/-/2025-maestrias-en-diferentes-areas-en-unir": ("scrape_unir", "fragment-0-ckxq", "fragment-0-ckxq", "#content"),
    "https://fulbright.edu.co/beca-j-william-fulbright/": ("scrape_lideres", "d65629b", "bdt-tab-2-tabpanel-0", ".jwilliam-item"),
}

# Función genérica para ejecutar el scraping según la URL
def scrape_url(url):
    if url in URL_FUNCTIONS:
        function_name, title_id, desc_id, selector = URL_FUNCTIONS[url]
        run_scraping(url, title_id, desc_id, selector)
    else:
        print(f"⚠ No hay función definida para la URL: {url}")

# Función generalizada para hacer scraping y guardar datos en TXT
def run_scraping(url, title_id, desc_id, selector):
    driver = webdriver.Chrome()
    data = []

    try:
        driver.get(url)
        print(f"🌐 Conectado a {url}")

        becas = driver.find_elements(By.CSS_SELECTOR, selector)  
        for beca in becas:
            try:
                titulo = beca.find_element(By.ID, title_id).text
                descripcion = beca.find_element(By.ID, desc_id).text
                data.append((titulo, descripcion, url))
            except Exception as e:
                print(f"⚠ Error extrayendo datos de {url}: {e}")

        # Guardar datos en un archivo TXT
        save_to_txt(url, data)

    except Exception as e:
        print(f"❌ Error al acceder a {url}: {e}")
    finally:
        driver.quit()
        print("🛑 Navegador cerrado")
    
    # Guardar en base de datos
    save_to_db(data)

# Función para guardar en archivos de texto
def save_to_txt(url, data):
    file_name = os.path.join(TEXT_FOLDER, f"{url.split('/')[-2]}.txt")
    with open(file_name, "w", encoding="utf-8") as file:
        for titulo, descripcion, enlace in data:
            file.write(f"Nombre de la beca: {titulo}\n")
            file.write(f"Descripción: {descripcion}\n")
            file.write(f"URL: {enlace}\n")
            file.write("="*50 + "\n")
    print(f"📄 Datos guardados en {file_name}")

# Función para guardar en la base de datos
def save_to_db(data):
    conn = sqlite3.connect("database/becas.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS becas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre_beca TEXT NOT NULL,
            enfoque_beca TEXT NOT NULL,
            poblacion_aspirante TEXT NOT NULL,
            fecha_beca DATETIME,
            url_beca TEXT NOT NULL
        )
    """)
    cursor.executemany("INSERT INTO becas (nombre_beca, enfoque_beca, poblacion_aspirante, url_beca) VALUES (?, ?, ?, ?)", data)
    conn.commit()
    conn.close()
    print(f"✅ {len(data)} becas guardadas en la base de datos.")

# Script principal para recorrer todas las URLs
def ejecutar_scraping():
    for url in URL_FUNCTIONS.keys():
        scrape_url(url)
