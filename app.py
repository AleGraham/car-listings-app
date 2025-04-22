import pandas as pd
import plotly.express as px
import streamlit as st

# Encabezado de la app
st.header("🚗 Análisis de anuncios de coches en venta")

# Leer el dataset
car_data = pd.read_csv('vehicles_us.csv')

# Casilla para histograma
show_hist = st.checkbox('Mostrar histograma de odómetro')

if show_hist:
    st.write("🔍 Distribución del kilometraje (odómetro)")
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Casilla para gráfico de dispersión
show_scatter = st.checkbox('Mostrar dispersión de precio vs. año')

if show_scatter:
    st.write("📊 Relación entre precio y año del coche")
    fig2 = px.scatter(car_data, x="model_year", y="price", color="condition")
    st.plotly_chart(fig2, use_container_width=True)
