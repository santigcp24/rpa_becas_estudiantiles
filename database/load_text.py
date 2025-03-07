import sqlite3
import os

# Ruta de la base de datos y directorio de archivos de texto
DB_PATH = r"C:\Users\sxc_x\OneDrive\Escritorio\rpa_becas_estudiantiles\rpa_becas_estudiantiles\database\becas.db"
TEXT_FOLDER = r"C:\Users\sxc_x\OneDrive\Escritorio\rpa_becas_estudiantiles\rpa_becas_estudiantiles\text_processing\text_data"

# Crear y conectar a la base de datos
def create_db():
    try:
        
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS becas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT,
                nombre_beca TEXT NOT NULL,
                enfoque_beca TEXT NOT NULL,
                poblacion_aspirante TEXT NOT NULL,
                fecha_beca DATETIME,
                url_beca TEXT NOT NULL
            )
        """)
        conn.commit()
        conn.close()

    except Exception as e:
        raise (e)
        
# Cargar datos de archivos .txt a la base de datos
def load_texts_to_db():
    try: 
        
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        for filename in os.listdir(TEXT_FOLDER):
            if filename.endswith(".txt"):
                file_path = os.path.join(TEXT_FOLDER, filename)
                with open(file_path, "r", encoding="utf-8") as file:
                    text = file.read()

                    cursor.execute("INSERT INTO becas (titulo, descripcion) VALUES (?, ?)", 
                                (filename.replace(".txt", ""), text))

        conn.commit()
        conn.close()
        print("Datos almacenados en la base de datos.")
    
    except Exception as e:
        raise (e)    


