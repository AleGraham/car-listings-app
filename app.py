import pandas as pd
import plotly.express as px
import streamlit as st

# Encabezado de la app
st.header("🚗 Análisis de anuncios de coches en venta")

# Leer el dataset
car_data = pd.read_csv('vehicles_us.csv')

# Botón para construir histograma
hist_button = st.button('Mostrar histograma')

if hist_button:
    st.write("Distribución de kilometraje (odómetro)")
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Botón para construir gráfico de dispersión
scatter_button = st.button('Mostrar gráfico de dispersión')

if scatter_button:
    st.write("Relación entre precio y año del coche")
    fig2 = px.scatter(car_data, x="model_year", y="price", color="condition")
    st.plotly_chart(fig2, use_container_width=True)
