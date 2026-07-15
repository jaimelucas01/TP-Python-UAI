import streamlit as st
from sklearn.cluster import KMeans
import plotly.express as px


def mostrar_machine_learning(df):

    st.divider()
    st.header("🤖 Machine Learning - K-Means")

    columnas = df.select_dtypes(include="number")

    if len(columnas.columns) < 2:
        st.warning(
            "Se necesitan al menos dos columnas numéricas para ejecutar K-Means."
        )
        return

    st.write("Seleccioná las variables para el análisis:")

    x = st.selectbox(
        "Variable X",
        columnas.columns,
        index=0
    )

    y = st.selectbox(
        "Variable Y",
        columnas.columns,
        index=1
    )

    cantidad_grupos = st.slider(
        "Cantidad de grupos",
        2,
        5,
        3
    )

    modelo = KMeans(
        n_clusters=cantidad_grupos,
        random_state=42,
        n_init=10
    )

    datos = df[[x, y]]

    df_ml = df.copy()

    df_ml["Grupo"] = modelo.fit_predict(datos)

    st.success("Modelo ejecutado correctamente.")

    st.dataframe(df_ml)

    fig = px.scatter(
        df_ml,
        x=x,
        y=y,
        color=df_ml["Grupo"].astype(str),
        title="Agrupamiento con K-Means"
    )

    st.plotly_chart(fig)