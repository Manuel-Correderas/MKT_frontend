# streamlit_app/pages/9_📈_Historial_Ventas.py
import streamlit as st

st.set_page_config(page_title="Historial de Ventas (Vendedor)", layout="centered")

# =============== Estilos ===============
st.markdown("""
<style>
.stApp { background:#FF8C00; }
.panel { 
    background:#f79b2f; 
    border-radius:14px; 
    padding:16px 18px;
    box-shadow:0 8px 18px rgba(0,0,0,.18); 
}
.hdr { 
    text-align:center; 
    font-weight:900; 
    letter-spacing:.6px;
    color:#10203a; 
    margin-bottom:12px; 
}
.sub { 
    color:#162c56; 
    font-size:.92rem; 
}
.list { 
    background:#ffa84d; 
    border-radius:10px; 
    padding:10px; 
    margin-top:8px;
    max-height: 460px; 
    overflow-y: auto; 
    box-shadow: inset 0 1px 4px rgba(0,0,0,.12); 
}
.card { 
    background:#fff5e6; 
    border-radius:10px; 
    padding:12px;
    box-shadow:0 2px 8px rgba(0,0,0,.12); 
    margin-bottom:10px; 
}
.badge { 
    display:inline-block; 
    background:#d6d6d6; 
    color:#000; 
    font-weight:900;
    border-radius:8px; 
    padding:6px 10px; 
    margin:6px 0; 
}
.small { 
    font-size:.86rem; 
    color:#333; 
}
.btn-primary { 
    background:#0b3a91 !important; 
    color:#fff !important; 
    border:none !important; 
    border-radius:8px !important;
    padding:8px 14px !important; 
    font-weight:900 !important;
}
.btn-secondary { 
    background:#936037 !important; 
    color:#fff !important; 
    border:none !important; 
    border-radius:8px !important;
    padding:8px 14px !important; 
    font-weight:900 !important;
}
.seller-header {
    background:#ff9b2f;
    padding:12px;
    border-radius:8px;
    margin-bottom:15px;
    text-align:center;
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

# =============== Encabezado ===============
st.markdown('<div class="hdr"><h3>📈 HISTORIAL DE VENTAS</h3></div>', unsafe_allow_html=True)
st.markdown('<div class="panel">', unsafe_allow_html=True)

# Información del vendedor
st.markdown("<div class='seller-header'>", unsafe_allow_html=True)
st.markdown("### 🏪 H&M - VENDEDOR")
st.markdown("**📊 RESUMEN:** 156 VENTAS • ⭐ 9.2 VALORACIÓN PROMEDIO • $1,248,950 INGRESOS TOTALES")
st.markdown("</div>", unsafe_allow_html=True)

# Búsqueda y filtros
st.markdown("### 🔍 BUSCAR VENTAS")
col_search, col_filter1, col_filter2 = st.columns([2, 1, 1])
with col_search:
    search_query = st.text_input("", placeholder="Buscar por producto, cliente, factura...")
with col_filter1:
    date_filter = st.selectbox("Fecha", ["Últimos 7 días", "Este mes", "Últimos 3 meses", "Todo"])
with col_filter2:
    status_filter = st.selectbox("Estado", ["Todos", "Entregados", "En camino", "Pendientes"])

# =============== Lista de Ventas ===============
st.markdown('<div class="list">', unsafe_allow_html=True)

# Ventas de ejemplo
sales = [
    {
        "id": "V-001",
        "product_name": "Jean Slim Azul",
        "category": "Indumentaria",
        "subcategory": "Pantalones",
        "date": "15/03/2024",
        "time": "14:30",
        "client_name": "María González",
        "client_address": "Av. Siempre Viva 123, CABA",
        "quantity": 1,
        "unit_price": 25999,
        "total": 25999,
        "invoice": "FAC-2024-001",
        "status": "Entregado",
        "product_rating": 9.5,
        "client_rating": 10,
        "stock_at_sale": 15
    },
    {
        "id": "V-002",
        "product_name": "Remera Básica Negra",
        "category": "Indumentaria",
        "subcategory": "Remeras",
        "date": "12/03/2024", 
        "time": "10:15",
        "client_name": "Carlos Rodríguez",
        "client_address": "Calle Falsa 456, CABA",
        "quantity": 2,
        "unit_price": 8999,
        "total": 17998,
        "invoice": "FAC-2024-002",
        "status": "Entregado",
        "product_rating": 9.0,
        "client_rating": 9,
        "stock_at_sale": 20
    },
    {
        "id": "V-003",
        "product_name": "Zapatillas Urbanas",
        "category": "Calzado",
        "subcategory": "Urbano", 
        "date": "08/03/2024",
        "time": "16:45",
        "client_name": "Laura Martínez",
        "client_address": "Av. Corrientes 789, CABA",
        "quantity": 1,
        "unit_price": 45999,
        "total": 45999,
        "invoice": "FAC-2024-003",
        "status": "En camino",
        "product_rating": "-",
        "client_rating": "-",
        "stock_at_sale": 8
    }
]

# Aplicar filtros
filtered_sales = [
    s for s in sales 
    if (search_query.lower() in s["product_name"].lower() or 
        search_query.lower() in s["client_name"].lower() or
        search_query.lower() in s["invoice"].lower()) and
       (status_filter == "Todos" or s["status"] == status_filter)
]

if not filtered_sales:
    st.info("No se encontraron ventas que coincidan con los filtros.")
else:
    for sale in filtered_sales:
        st.markdown('<div class="card">', unsafe_allow_html=True)

        # Header de la venta
        col_header1, col_header2 = st.columns([4, 1])
        with col_header1:
            st.markdown(f"**🛍️ {sale['product_name']}**")
            st.caption(f"📂 {sale['category']} • 🔍 {sale['subcategory']}")
        with col_header2:
            status_color = "🟢" if sale["status"] == "Entregado" else "🟡" if sale["status"] == "En camino" else "🔴"
            st.markdown(f"**{status_color} {sale['status']}**")

        # Detalles de la venta
        col_details1, col_details2 = st.columns(2)
        with col_details1:
            st.markdown(f"""
            **📅 Fecha:** {sale['date']} {sale['time']}  
            **👤 Cliente:** {sale['client_name']}  
            **🏠 Dirección:** {sale['client_address']}  
            **📦 Cantidad:** {sale['quantity']}  
            **💰 Precio Unitario:** ${sale['unit_price']:,}
            """.replace(",", "."))
        with col_details2:
            st.markdown(f"""
            **🧾 Factura:** {sale['invoice']}  
            **📊 Stock al momento:** {sale['stock_at_sale']}  
            **⭐ Valoración Producto:** {sale['product_rating']}/10  
            **😊 Valoración Cliente:** {sale['client_rating']}/10  
            **🎯 Estado:** {sale['status']}
            """)

        # Total y acciones
        st.markdown(f"<span class='badge'>💵 TOTAL VENTA: ${sale['total']:,}</span>".replace(",", "."), unsafe_allow_html=True)

        # Sección de gestión
        st.markdown("### 🛠️ GESTIÓN DE VENTA")
        col_manage1, col_manage2, col_manage3 = st.columns(3)
        
        with col_manage1:
            st.markdown("**📊 Valorar Cliente**")
            client_rating = st.slider("Puntuación del cliente", 1, 10, value=sale["client_rating"] if sale["client_rating"] != "-" else 5, key=f"rate_{sale['id']}")
        
        with col_manage2:
            st.markdown("**📎 Comprobante**")
            st.file_uploader("Subir archivo", type=["pdf", "png", "jpg"], key=f"file_{sale['id']}", label_visibility="collapsed")
        
        with col_manage3:
            st.markdown("**⚡ Acciones**")
            col_btn1, col_btn2 = st.columns(2)
            with col_btn1:
                st.button("💾 GUARDAR", key=f"save_{sale['id']}", use_container_width=True)
            with col_btn2:
                st.button("📧 CONTACTAR", key=f"contact_{sale['id']}", use_container_width=True)

        st.markdown("</div>", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)  # /list

# =============== Pie ===============
st.write("")
col_back = st.columns([1])[0]
with col_back:
    st.button("⬅️ VOLVER AL PANEL", key="btn_back", use_container_width=True)

st.markdown('</div>', unsafe_allow_html=True)  # /panel

# Resumen estadístico
with st.expander("📊 ESTADÍSTICAS DETALLADAS"):
    col_stat1, col_stat2, col_stat3, col_stat4 = st.columns(4)
    with col_stat1:
        st.metric("Ventas Totales", "156")
    with col_stat2:
        st.metric("Ingresos Totales", "$1,248,950")
    with col_stat3:
        st.metric("Valoración Promedio", "9.2/10")
    with col_stat4:
        st.metric("Clientes Satisfechos", "98%")
    
    st.markdown("**📈 Distribución por Categoría:**")
    st.markdown("- 🧥 Indumentaria: 112 ventas ($896,450)")
    st.markdown("- 👟 Calzado: 32 ventas ($287,600)") 
    st.markdown("- 📱 Electrónicos: 12 ventas ($64,900)")