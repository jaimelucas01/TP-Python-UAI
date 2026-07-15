import streamlit as st
import pandas as pd

from utils.pandas_tools import mostrar_analisis
from utils.ml_tools import mostrar_machine_learning

st.set_page_config(

    page_title="Smart Data Analyzer",

    page_icon="📊",

    layout="wide"

)

# Título de la aplicación
st.title("📊 Smart Data Analyzer")

st.caption("Proyecto Final - Python para Inteligencia Artificial | UAI 2026")

st.divider()
with st.sidebar:

    st.header("📂 Menú")

    st.info(

        """

Este sistema permite:

✅ Cargar archivos CSV

✅ Analizar datos con Pandas

✅ Visualizar gráficos

✅ Aplicar Machine Learning

"""

    )
# Descripción
st.write("Subí un archivo CSV para comenzar el análisis.")

# Botón para subir un archivo
archivo = st.file_uploader(
    "Seleccioná un archivo CSV",
    type=["csv"]
)

# Si el usuario subió un archivo
if archivo is not None:

    try:
        # Leer el CSV
        df = pd.read_csv(archivo)

        st.success("✅ Archivo cargado correctamente")

        st.subheader("Vista previa de los datos")

        st.dataframe(df)

        # Llamar al módulo de análisis
        mostrar_analisis(df)
        mostrar_machine_learning(df)

    except Exception as e:

        st.error(f"Ocurrió un error al leer el archivo: {e}")