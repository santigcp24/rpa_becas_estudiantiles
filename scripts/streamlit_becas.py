import sqlite3
import pandas as pd
import streamlit as st

db_path = r"C:\Users\46229090\Desktop\automatismos bkcp\rpa_becas_estudiantiles\files\becas.db"

# Configurar el título de la aplicación
st.title("Becas Disponibles")

# Conectar a la base de datos SQLite
def get_data_from_db():
    conn = sqlite3.connect(db_path)
    query = "SELECT * FROM becas"
    df = pd.read_sql_query(query, conn)
    conn.close()
    # Eliminar duplicados basados en nombre_beca, enfoque_beca y poblacion_aspirante
    # 🔹 Normalizar la columna 'poblacion_aspirante' para evitar inconsistencias
    df['poblacion_aspirante'] = df['poblacion_aspirante'].str.strip().str.lower()
    return df

data = get_data_from_db()

# Filtros
st.sidebar.header("Sección de filtros")

# Obtener valores únicos normalizados
enfoques = sorted(data['enfoque_beca'].drop_duplicates())
poblaciones = sorted(data['poblacion_aspirante'].drop_duplicates())

# Agregar opción "Población General"
if "población general" in poblaciones:
    poblaciones.insert(0, "Población General")  # La agregamos al inicio de la lista

# Filtros en la barra lateral
enfoque_filter = st.sidebar.multiselect("🎯 Filtrar por enfoque de beca:", options=enfoques, default=enfoques, key="enfoque")
poblacion_filter = st.sidebar.multiselect("👥 Filtrar por población aspirante:", options=poblaciones, default=poblaciones, key="poblacion")

# ✅ Nuevo Filtro: Becas Vigentes / Becas Vencidas
estado_beca_filter = st.sidebar.radio(
    "📅 Filtrar por estado de la beca:",
    options=["Todas", "Becas Vigentes", "Becas Vencidas"],  # Opciones del filtro
    index=0,  # Por defecto, muestra todas las becas
    key="estado_beca"
)

# 📌 **Aplicar filtros**
filtered_data = data[data['enfoque_beca'].isin(enfoque_filter)]

# Aplicar filtro de población aspirante
if "Población General" in poblacion_filter:
    # Si "Población General" está seleccionado, se muestran todas las becas
    pass  
else:
    # Si no está seleccionado, se filtran las becas específicas
    filtered_data = filtered_data[filtered_data['poblacion_aspirante'].isin(poblacion_filter)]


# Mostrar los datos filtrados
st.dataframe(filtered_data.style.hide(axis="index"))

# Enlaces a las becas
st.write("### Enlaces para ver la información más detallada")
for index, row in filtered_data.iterrows():
    st.write(f"[{row['nombre_beca']}]({row['url_beca']})")

    
