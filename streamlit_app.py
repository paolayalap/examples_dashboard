#Librerías
import streamlit as st
import pandas as pd #para implementar tablas

st.write('Hi everyone!')


st.title("Tabla editable (data_editor)")
df = pd.DataFrame({
    "Punto": ["A", "B", "C", "D"],
    "Temp (°C)": [24.3, 25.1, 23.8, 24.9],
    "pH": [7.1, 7.4, 7.0, 7.3],
    "Conductividad (µS/cm)": [420, 510, 385, 460]
})

editado = st.data_editor(
    df,
    use_container_width=True,
    column_config={
        "Temp (°C)": st.column_config.NumberColumn(format="%.1f"),
        "pH": st.column_config.NumberColumn(min_value=0.0, max_value=14.0, step=0.1),
        "Conductividad (µS/cm)": st.column_config.NumberColumn(step=1, help="MicroSiemens por centímetro")
    },
    hide_index=True
)

st.subheader("Datos finales")
st.write(editado)




"""st.title("Tabla interactiva")
df = pd.DataFrame({
    "Fecha": pd.date_range("2025-10-01", periods=6, freq="D"),
    "Chl-a (µg/L)": [12.1, 18.7, 33.2, 41.8, 22.0, 15.4],
    "Ficocianina (µg/L)": [3.2, 4.0, 5.1, 7.3, 4.2, 3.8]
})

st.dataframe(
    df,
    use_container_width=True,   # ocupa todo el ancho
    height=320,                 # alto del contenedor con scroll
)"""



""""st.title("Tabla estática")
data = {
    "Sensor": ["pH", "Turbidez", "DO", "Conductividad", "Temperatura"],
    "Valor": [7.2, 12.5, 6.8, 420.0, 24.3],
    "Unidad": ["pH", "NTU", "mg/L", "µS/cm", "°C"]
}
df = pd.DataFrame(data)

st.table(df)  # Render plano (no scroll, no ordenar)"""

