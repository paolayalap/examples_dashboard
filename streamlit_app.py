#Librerías
import streamlit as st
import pandas as pd #para implementar tablas

st.title('Examples')
st.write('Hi everyone!')

st.title("Tabla estática")
data = {
    "Sensor": ["pH", "Turbidez", "DO", "Conductividad", "Temperatura"],
    "Valor": [7.2, 12.5, 6.8, 420.0, 24.3],
    "Unidad": ["pH", "NTU", "mg/L", "µS/cm", "°C"]
}
df = pd.DataFrame(data)

st.table(df)  # Render plano (no scroll, no ordenar)

