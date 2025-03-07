from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

# Directorios para guardar imágenes
SCREENSHOT_FOLDER = r"C:\Users\sxc_x\OneDrive\Escritorio\rpa_becas_estudiantiles\rpa_becas_estudiantiles\screenshots"
os.makedirs(SCREENSHOT_FOLDER, exist_ok=True)

# URLs a visitar
URLS = [
    "https://fulbright.edu.co/beca-fulbright-para-comunidades-afrodescendientes/",
    "https://fulbright.edu.co/beca-fulbright-minciencias/",
    "https://fulbright.edu.co/beca-j-william-fulbright/",
]

# Configurar Selenium WebDriver
def get_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Ejecutar en segundo plano
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    service = Service(ChromeDriverManager().install())
    return webdriver.Chrome(service=service, options=chrome_options)

# Función para visitar la página y tomar una captura de pantalla
def scrape_and_capture(url):
    driver = get_driver()
    try:
        driver.get(url)
        time.sleep(3)  # Esperar a que la página cargue completamente
        filename = url.split("/")[-2] + ".png"  # Nombre basado en la URL
        screenshot_path = os.path.join(SCREENSHOT_FOLDER, filename)
        driver.save_screenshot(screenshot_path)
        print(f"Captura guardada en: {screenshot_path}")
    finally:
        driver.quit()
        print(f"Navegador cerrado para {url}")

# Ejecutar el scraping en todas las URLs
def scrap():
    for url in URLS:
        scrape_and_capture(url)


