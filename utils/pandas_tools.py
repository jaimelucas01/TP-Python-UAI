import streamlit as st
import plotly.express as px


def mostrar_analisis(df):

    st.subheader("📈 Información del dataset")

    st.write("Cantidad de filas:", df.shape[0])

    st.write("Cantidad de columnas:", df.shape[1])

    st.subheader("📋 Tipos de datos")

    st.write(df.dtypes)

    st.subheader("❌ Valores nulos")

    st.write(df.isnull().sum())

    st.subheader("📊 Estadísticas")

    st.write(df.describe())

    st.subheader("📈 Gráfico")

    columnas_numericas = df.select_dtypes(include="number").columns

    if len(columnas_numericas) > 0:

        columna = st.selectbox(

            "Elegí una columna",

            columnas_numericas

        )

        fig = px.histogram(

            df,

            x=columna,

            title=f"Distribución de {columna}"

        )

        st.plotly_chart(fig)

    st.divider()

    st.header("📌 Resumen")

    st.success(

        f"El archivo tiene {df.shape[0]} filas y {df.shape[1]} columnas."

    )

    if df.isnull().sum().sum() == 0:

        st.success("No se encontraron valores nulos.")

    else:

        st.warning("Se encontraron valores nulos.")