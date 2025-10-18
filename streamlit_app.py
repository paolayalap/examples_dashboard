#Librerías
import streamlit as st
import pandas as pd #para implementar tablas

st.write('Hi everyone!')


st.title("Tabla interactiva")
df = pd.DataFrame({
    "Fecha": pd.date_range("2025-10-01", periods=6, freq="D"),
    "Chl-a (µg/L)": [12.1, 18.7, 33.2, 41.8, 22.0, 15.4],
    "Ficocianina (µg/L)": [3.2, 4.0, 5.1, 7.3, 4.2, 3.8]
})

st.dataframe(
    df,
    use_container_width=True,   # ocupa todo el ancho
    height=320,                 # alto del contenedor con scroll
)


""""st.title("Tabla estática")
data = {
    "Sensor": ["pH", "Turbidez", "DO", "Conductividad", "Temperatura"],
    "Valor": [7.2, 12.5, 6.8, 420.0, 24.3],
    "Unidad": ["pH", "NTU", "mg/L", "µS/cm", "°C"]
}
df = pd.DataFrame(data)

st.table(df)  # Render plano (no scroll, no ordenar)"""

