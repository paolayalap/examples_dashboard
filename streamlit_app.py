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




