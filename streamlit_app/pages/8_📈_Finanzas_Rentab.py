import streamlit as st
import pandas as pd
import numpy as np
from datetime import date, timedelta

st.set_page_config(page_title="Finanzas y Rentabilidad", page_icon="💰", layout="wide")

# =======================
# Encabezado
# =======================
st.title("Finanzas y Rentabilidad")
st.caption("KPIs y dashboard financiero del vendedor")

# =======================
# Filtros
# =======================
st.sidebar.header("Filtros")
hoy = date.today()
inicio = hoy - timedelta(days=30)
rango = st.sidebar.date_input("Rango de fechas", (inicio, hoy), format="DD/MM/YYYY")
moneda = st.sidebar.selectbox("Moneda", ["ARS", "USD"], index=0)
canales = st.sidebar.multiselect("Canales", ["Tienda", "Marketplace", "Instagram", "WhatsApp"], default=["Tienda"])
mostrar_iva = st.sidebar.toggle("Mostrar IVA (21%)", value=False)
top_n = st.sidebar.slider("Top productos", 3, 15, 8)

# =======================
# Datos de ejemplo
# =======================
fechas = pd.date_range(inicio, hoy, freq="D")
np.random.seed(42)
categorias = ["Indumentaria", "Calzado", "Electrónica", "Accesorios"]
df = pd.DataFrame({
    "fecha": np.random.choice(fechas, 100),
    "categoria": np.random.choice(categorias, 100),
    "producto": np.random.choice(["Remera", "Jean", "Zapatillas", "Auriculares", "Mochila"], 100),
    "importe": np.random.randint(8000, 120000, 100),
    "margen": np.random.randint(2000, 60000, 100)
})

# =======================
# KPIs
# =======================
ventas = df["importe"].sum()
margen = df["margen"].sum()
ticket = ventas / len(df)
devoluciones = np.random.randint(0, 15)

c1, c2, c3, c4 = st.columns(4)
c1.metric("Ventas", f"$ {ventas:,.0f}".replace(",", "."))
c2.metric("Margen", f"$ {margen:,.0f}".replace(",", "."), delta=f"{(margen/ventas)*100:.1f}%")
c3.metric("Ticket Promedio", f"$ {ticket:,.0f}".replace(",", "."))
c4.metric("Devoluciones", devoluciones)

st.divider()

# =======================
# Gráficos
# =======================
st.subheader("Evolución diaria de ventas")
ventas_dia = df.groupby("fecha", as_index=False)["importe"].sum()
st.line_chart(ventas_dia, x="fecha", y="importe", height=250)

col1, col2 = st.columns(2)
with col1:
    st.subheader("Margen por categoría")
    margen_cat = df.groupby("categoria", as_index=False)["margen"].sum()
    st.bar_chart(margen_cat, x="categoria", y="margen", height=260)
with col2:
    st.subheader("Top productos por ventas")
    top_prod = df.groupby("producto", as_index=False)["importe"].sum().sort_values("importe", ascending=False).head(top_n)
    st.bar_chart(top_prod, x="producto", y="importe", height=260)

st.divider()

# =======================
# Detalle
# =======================
st.subheader("Detalle de operaciones")
st.dataframe(df.sort_values("fecha", ascending=False), use_container_width=True)
