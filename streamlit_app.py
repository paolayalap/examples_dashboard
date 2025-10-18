#Librerías
import streamlit as st
import pandas as pd #para implementar tablas

st.write('Hi everyone!')

# ------ Subir un CSV y mostrarlo como tabla -------
#st.title("Cargar CSV y mostrar tabla")
#archivo = st.file_uploader("Sube tu archivo .csv", type=["csv"])
#if archivo is not None:
#    df = pd.read_csv(archivo)
#    st.success(f"Filas: {df.shape[0]} | Columnas: {df.shape[1]}")
#    st.dataframe(df, use_container_width=True)

# ------- Botón con color personalizado --------
#st.markdown("""
#<style>
#div.stButton > button {
#    background-color: #ff4b4b;   /* rojo personalizado */
#    color: white;
#    border-radius: 12px;
#    padding: 0.6em 1.2em;
#    font-weight: bold;
#    border: none;
#}
#div.stButton > button:hover {
#    background-color: #ff7878;   /* color al pasar el mouse 
#    transform: scale(1.03);
#}
#</style>
#""", unsafe_allow_html=True)
#st.button("Botón rojo personalizado")

# ------- Botón simple --------
def correr_modelo(k):
    st.write(f"Entrenando modelo con k={k}...")

st.button(
    "Entrenar",
    type="primary",
    help="Ejecuta el pipeline completo",
    on_click=correr_modelo,
    kwargs={"k": 5},
)

if st.button("Procesar datos"):
    st.success("¡Listo!")

