import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta, date

# =======================
# Configuración y encabezado
# =======================
st.set_page_config(page_title="Dashboard Global - MKT", layout="wide")
st.title("Dashboard Global")
st.caption("Resumen general de actividad, ventas y rendimiento.")

# =======================
# Datos de ejemplo (solo front-end)
# =======================
np.random.seed(42)
hoy = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
fechas = pd.date_range(hoy - timedelta(days=30), hoy, freq="D")

orders = pd.DataFrame({
    "order_date": np.random.choice(fechas, 200),
    "seller": np.random.choice(["Juan", "Ana", "Carlos", "Sofía", "Lucía"], 200),
    "product_name": np.random.choice(["Remera", "Jean", "Auriculares", "Zapatillas", "Taladro"], 200),
    "qty": np.random.randint(1, 6, 200),
    "total_paid": np.random.randint(10_000, 200_000, 200),
    "payment_method": np.random.choice(["Tarjeta", "Transferencia", "QR", "Efectivo"], 200),
    "order_status": np.random.choice(["Paid", "Failed", "Pending"], 200)
})

# =======================
# Filtros laterales
# =======================
st.sidebar.header("Filtros")
desde = st.sidebar.date_input("Desde", (hoy - timedelta(days=30)).date())
hasta = st.sidebar.date_input("Hasta", hoy.date())

# Normalización segura de fechas (incluye 'hasta' completo)
desde_dt = pd.to_datetime(desde)
hasta_dt = pd.to_datetime(hasta) + pd.Timedelta(days=1) - pd.Timedelta(seconds=1)

mask = (orders["order_date"] >= desde_dt) & (orders["order_date"] <= hasta_dt)
orders = orders.loc[mask].copy()

# =======================
# KPIs
# =======================
total_users = 1200
total_products = 340
gmv = float(orders["total_paid"].sum())
orders_count = int(len(orders))
aov = gmv / orders_count if orders_count else 0.0

c1, c2, c3, c4 = st.columns(4)
c1.metric("Usuarios totales", f"{total_users:,}".replace(",", "."))
c2.metric("Productos publicados", f"{total_products:,}".replace(",", "."))
c3.metric("GMV (ventas cobradas)", f"$ {int(gmv):,}".replace(",", "."))
c4.metric("Ticket medio (AOV)", f"$ {int(aov):,}".replace(",", "."))

st.divider()

# =======================
# Evolución de ventas (robusto a nombres/índices)
# =======================
st.subheader("Evolución de ventas")
if not orders.empty:
    orders["day"] = orders["order_date"].dt.floor("D")
    by_day = (
        orders.groupby("day", as_index=False)
              .agg(gmv=("total_paid", "sum"), orders=("order_date", "count"))
              .sort_values("day")
    )
    by_day = by_day.rename(columns={"day": "fecha"})
    chart_df = by_day.set_index("fecha")[["gmv", "orders"]]
    st.line_chart(chart_df, height=260)
else:
    st.info("Sin datos en el rango seleccionado.")

# =======================
# Rankings
# =======================
col1, col2 = st.columns(2)

with col1:
    st.subheader("Top vendedores por GMV")
    if not orders.empty:
        top_sellers = (
            orders.groupby("seller", as_index=False)["total_paid"]
                  .sum()
                  .sort_values("total_paid", ascending=False)
                  .head(10)
        )
        st.bar_chart(top_sellers.set_index("seller")["total_paid"], height=260)
    else:
        st.info("Sin datos de órdenes.")

with col2:
    st.subheader("Top productos por unidades")
    if not orders.empty:
        top_products = (
            orders.groupby("product_name", as_index=False)["qty"]
                  .sum()
                  .sort_values("qty", ascending=False)
                  .head(10)
        )
        st.bar_chart(top_products.set_index("product_name")["qty"], height=260)
    else:
        st.info("Sin datos de órdenes.")

st.divider()

# =======================
# Catálogo y pagos (maqueta)
# =======================
cA, cB, cC = st.columns(3)

with cA:
    st.subheader("Catálogo")
    st.write("• Sin stock: **12**")
    st.write("• Con imagen: **285**")
    st.write("• Top categorías:")
    st.write(pd.Series(["Indumentaria", "Electrónica", "Herramientas", "Calzado"]))

with cB:
    st.subheader("Métodos de pago")
    if not orders.empty:
        st.bar_chart(orders["payment_method"].value_counts(), height=260)
    else:
        st.info("Sin datos de método de pago.")

with cC:
    st.subheader("Calidad de órdenes")
    if not orders.empty:
        fail_rate = (orders["order_status"].str.lower().eq("failed").mean() * 100)
        st.metric("Tasa de fallos de pago", f"{fail_rate:.1f}%")
    else:
        st.info("Sin estados de orden.")

st.divider()

# =======================
# Monetización
# =======================
st.subheader("Monetización & Premium")
m1, m2 = st.columns([2, 1])
with m1:
    st.write("Accedé a planes Premium para mejorar la visibilidad y reducir comisiones.")
with m2:
    st.button("Ver planes Premium", type="primary")

st.caption("Panel demostrativo — solo front-end para vista de vendedores.")
