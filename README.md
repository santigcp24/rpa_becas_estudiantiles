Este proyecto es un prototipo de RPA (Robotic Process Automation) diseñado para automatizar la extracción,
procesamiento y almacenamiento de información sobre becas estudiantiles. Utiliza Web Scraping con Selenium, OCR con Tesseract, y almacenamiento en SQLite,
permitiendo a los usuarios acceder a información consolidada y actualizada sobre oportunidades académicas. Para el tema visual se opta por el uso de Streamlit.

Scraping Web Automatizado: Extrae información de páginas de becas con Selenium.
Captura de Pantallas: Guarda imágenes de las páginas procesadas para auditoría.
Extracción de Texto con OCR: Utiliza Tesseract para procesar imágenes y extraer texto relevante.
Almacenamiento en Base de Datos: Guarda la información estructurada en SQLite.
Estructura Modular: Separación del scraping, OCR y carga en BD para mayor flexibilidad.
Generación de Archivos TXT: Guarda los datos en text_data/ para versionado y auditoría.

rpa_becas_estudiantiles/
├── 📂 .venv/ - Entorno virtual de Python
├── 📂 data_extraction/ - Módulo de scraping
│ ├── scraping_becas.py - Extrae datos de las páginas web
│ └── screenshots/ - Capturas de pantalla de las páginas procesadas
├── 📂 text_processing/ - Módulo de OCR
│ ├── ocr_extraccion.py - Extrae texto de las imágenes
│ └── text_data/ - Almacena los archivos de texto generados
├── 📂 database/ - Módulo de almacenamiento en SQLite
│ ├── becas.db - Base de datos SQLite
│ ├── load_text.py - Carga los datos procesados en la BD
├── 📂 scripts/ - Archivos adicionales de soporte
├── .gitignore - Exclusiones para el control de versiones
├── requirements.txt - Dependencias del proyecto
└── main.py - Punto de entrada principal

Explicación de los Módulos
🔹 1. Web Scraping (scraping_becas.py)
Se conecta a páginas de becas usando Selenium.
Extrae nombre, descripción y enlace de cada beca.
Genera capturas de pantalla en screenshots/.
Guarda los datos en archivos TXT en text_data/.
🔹 2. Extracción de Texto (ocr_extraccion.py)
Usa Tesseract OCR para convertir imágenes en texto.
Almacena el texto en text_data/ para auditoría.
🔹 3. Carga en Base de Datos (load_text.py)
Toma los archivos TXT generados.
Carga la información en SQLite (becas.db).
Permite consultas rápidas y análisis de datos.
🔹 4. visualización con streamlit
Consulta la base de datos generada y muestra la tabla 
con la información haciendo uso de dataframe. 
Se tiene diversos filtros para el tema de la interacción.
