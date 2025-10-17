# streamlit_app/pages/8_📊_Dashboard_Local.py
import streamlit as st

st.set_page_config(page_title="Dashboard Local", layout="wide")

# =======================
# Estilos
# =======================
st.markdown("""
<style>
.stApp { background:#FF8C00; }
.dashboard-panel {
    background:#f79b2f; 
    border-radius:12px; 
    padding:20px; 
    margin-bottom:20px;
    box-shadow:0 8px 18px rgba(0,0,0,.18);
}
.metric-card {
    background:#fff5e6;
    border-radius:10px;
    padding:15px;
    text-align:center;
    box-shadow:0 2px 8px rgba(0,0,0,.12);
}
.section-title {
    color:#1f2e5e;
    font-weight:800;
    margin:20px 0 10px 0;
    border-bottom:2px solid #0b3a91;
    padding-bottom:5px;
}
</style>
""", unsafe_allow_html=True)

# =======================
# Encabezado
# =======================
st.markdown('<div class="dashboard-panel">', unsafe_allow_html=True)
st.markdown("## 📊 DASHBOARD LOCAL")
st.markdown("**Panel de control y métricas de tu actividad**")
st.markdown('</div>', unsafe_allow_html=True)

# =======================
# Selector de Vista
# =======================
st.markdown('<div class="dashboard-panel">', unsafe_allow_html=True)
view_mode = st.radio(
    "**👤 VER COMO:**",
    ["Vendedor", "Comprador"],
    horizontal=True,
    key="view_mode"
)
st.markdown('</div>', unsafe_allow_html=True)

# =======================
# KPIs Principales
# =======================
st.markdown('<div class="dashboard-panel">', unsafe_allow_html=True)
st.markdown("### 📈 MÉTRICAS PRINCIPALES")

if view_mode == "Vendedor":
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("💰 VENTAS TOTALES", "$248,950", "+12% vs mes anterior")
        st.markdown('</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("📦 PEDIDOS", "156", "+8% vs mes anterior")
        st.markdown('</div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("⭐ VALORACIÓN", "9.2/10", "+0.3 puntos")
        st.markdown('</div>', unsafe_allow_html=True)
    with col4:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("🔄 DEVOLUCIONES", "4", "-2% vs mes anterior")
        st.markdown('</div>', unsafe_allow_html=True)
else:
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("🛍️ COMPRAS TOTALES", "$45,850", "+15% vs mes anterior")
        st.markdown('</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("📦 PEDIDOS", "12", "+2 vs mes anterior")
        st.markdown('</div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("⭐ VALORACIÓN PROMEDIO", "9.5/10", "+0.2 puntos")
        st.markdown('</div>', unsafe_allow_html=True)
    with col4:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("🎯 PRODUCTOS FAVORITOS", "8", "+3 vs mes anterior")
        st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# =======================
# Gráficos y Evolución
# =======================
st.markdown('<div class="dashboard-panel">', unsafe_allow_html=True)
st.markdown("### 📊 EVOLUCIÓN TEMPORAL")

if view_mode == "Vendedor":
    col_chart1, col_chart2 = st.columns(2)
    with col_chart1:
        st.markdown("**📈 Ventas Mensuales**")
        # Simulación de datos para gráfico
        st.markdown(
            '<div style="background:#fff5e6; border-radius:8px; padding:80px 20px; text-align:center; border:1px solid #ddd;">'
            '<span style="color:#666;">Gráfico de Ventas Mensuales</span>'
            '</div>', 
            unsafe_allow_html=True
        )
    with col_chart2:
        st.markdown("**📦 Pedidos por Categoría**")
        st.markdown(
            '<div style="background:#fff5e6; border-radius:8px; padding:80px 20px; text-align:center; border:1px solid #ddd;">'
            '<span style="color:#666;">Gráfico de Pedidos por Categoría</span>'
            '</div>', 
            unsafe_allow_html=True
        )
else:
    col_chart1, col_chart2 = st.columns(2)
    with col_chart1:
        st.markdown("**🛍️ Compras Mensuales**")
        st.markdown(
            '<div style="background:#fff5e6; border-radius:8px; padding:80px 20px; text-align:center; border:1px solid #ddd;">'
            '<span style="color:#666;">Gráfico de Compras Mensuales</span>'
            '</div>', 
            unsafe_allow_html=True
        )
    with col_chart2:
        st.markdown("**⭐ Valoraciones por Producto**")
        st.markdown(
            '<div style="background:#fff5e6; border-radius:8px; padding:80px 20px; text-align:center; border:1px solid #ddd;">'
            '<span style="color:#666;">Gráfico de Valoraciones</span>'
            '</div>', 
            unsafe_allow_html=True
        )

st.markdown('</div>', unsafe_allow_html=True)

# =======================
# Top Productos/Categorías
# =======================
st.markdown('<div class="dashboard-panel">', unsafe_allow_html=True)

if view_mode == "Vendedor":
    st.markdown("### 🏆 TOP PRODUCTOS MÁS VENDIDOS")
    col_top1, col_top2, col_top3 = st.columns(3)
    
    with col_top1:
        st.markdown("**🥇 Jean Slim Azul**")
        st.markdown("💰 $25,999 c/u")
        st.markdown("📦 45 vendidos")
        st.markdown("⭐ 9.2/10")
    
    with col_top2:
        st.markdown("**🥈 Remera Básica Negra**")
        st.markdown("💰 $8,999 c/u")
        st.markdown("📦 32 vendidos") 
        st.markdown("⭐ 8.7/10")
    
    with col_top3:
        st.markdown("**🥉 Zapatillas Urbanas**")
        st.markdown("💰 $45,999 c/u")
        st.markdown("📦 18 vendidos")
        st.markdown("⭐ 9.5/10")
else:
    st.markdown("### 🏆 TUS MARCAS FAVORITAS")
    col_top1, col_top2, col_top3 = st.columns(3)
    
    with col_top1:
        st.markdown("**🥇 H&M**")
        st.markdown("🛍️ 8 compras")
        st.markdown("💰 $28,950 gastado")
        st.markdown("⭐ 9.2/10")
    
    with col_top2:
        st.markdown("**🥈 SportShop**")
        st.markdown("🛍️ 3 compras")
        st.markdown("💰 $12,500 gastado")
        st.markdown("⭐ 9.5/10")
    
    with col_top3:
        st.markdown("**🥉 TechStore**")
        st.markdown("🛍️ 1 compra")
        st.markdown("💰 $4,400 gastado")
        st.markdown("⭐ 9.0/10")

st.markdown('</div>', unsafe_allow_html=True)

# =======================
# Actividad Reciente
# =======================
st.markdown('<div class="dashboard-panel">', unsafe_allow_html=True)
st.markdown("### 📋 ACTIVIDAD RECIENTE")

if view_mode == "Vendedor":
    st.markdown("**Últimos Pedidos:**")
    st.markdown("- 🟢 **Pedido #001** - Jean Slim Azul - $25,999 - Cliente: María G.")
    st.markdown("- 🟢 **Pedido #002** - Remera Negra (x2) - $17,998 - Cliente: Carlos R.")
    st.markdown("- 🟡 **Pedido #003** - Zapatillas Urbanas - $45,999 - Cliente: Laura M. (En camino)")
    st.markdown("- 🔴 **Pedido #004** - Auriculares - $14,999 - Cliente: Ana L. (Pendiente)")
else:
    st.markdown("**Tus Últimas Compras:**")
    st.markdown("- 🟢 **Compra #001** - Jean Slim Azul - $25,999 - Entregado")
    st.markdown("- 🟢 **Compra #002** - Remera Negra (x2) - $17,998 - Entregado")
    st.markdown("- 🟡 **Compra #003** - Zapatillas Urbanas - $45,999 - En camino")
    st.markdown("- ⭐ **Valoración:** Dejaste 5 estrellas para Jean Slim Azul")

st.markdown('</div>', unsafe_allow_html=True)

# =======================
# Acciones Rápidas
# =======================
st.markdown('<div class="dashboard-panel">', unsafe_allow_html=True)
st.markdown("### ⚡ ACCIONES RÁPIDAS")

if view_mode == "Vendedor":
    col_action1, col_action2, col_action3 = st.columns(3)
    with col_action1:
        st.button("📦 GESTIONAR PEDIDOS", use_container_width=True)
    with col_action2:
        st.button("📊 VER REPORTES", use_container_width=True)
    with col_action3:
        st.button("🔄 ACTUALIZAR STOCK", use_container_width=True)
else:
    col_action1, col_action2, col_action3 = st.columns(3)
    with col_action1:
        st.button("🛍️ SEGUIR COMPRANDO", use_container_width=True)
    with col_action2:
        st.button("⭐ DEJAR VALORACIONES", use_container_width=True)
    with col_action3:
        st.button("📋 VER HISTORIAL", use_container_width=True)

st.markdown('</div>', unsafe_allow_html=True)