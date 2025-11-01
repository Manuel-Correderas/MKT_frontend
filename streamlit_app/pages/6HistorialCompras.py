# streamlit_app/pages/6_🧾_Historial_Compras.py
import streamlit as st

st.set_page_config(page_title="Historial de Compras (Cliente)", layout="centered")

# ================== Estilos ==================
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
.badge { 
    display:inline-block; 
    background:#d6d6d6; 
    color:#000; 
    font-weight:900;
    border-radius:8px; 
    padding:6px 10px; 
    margin:4px 0;
}
.list { 
    background:#ffa84d; 
    border-radius:10px; 
    padding:10px; 
    margin-top:8px;
    max-height:460px; 
    overflow-y:auto; 
    box-shadow: inset 0 1px 4px rgba(0,0,0,.12); 
}
.card { 
    background:#fff5e6; 
    border-radius:10px; 
    padding:12px;
    box-shadow:0 2px 8px rgba(0,0,0,.12); 
    margin-bottom:10px; 
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
.client-header {
    background:#ff9b2f;
    padding:12px;
    border-radius:8px;
    margin-bottom:15px;
    text-align:center;
}
</style>
""", unsafe_allow_html=True)

# ================== Encabezado ==================
st.markdown('<div class="hdr"><h3>🧾 HISTORIAL DE COMPRAS</h3></div>', unsafe_allow_html=True)
st.markdown('<div class="panel">', unsafe_allow_html=True)

# Información del cliente
st.markdown("<div class='client-header'>", unsafe_allow_html=True)
st.markdown("### 👤 CLIENTE A")
st.markdown("**📊 RESUMEN:** 15 COMPRAS • ⭐ 9.2/10 VALORACIÓN PROMEDIO • $248,950 TOTAL GASTADO")
st.markdown("</div>", unsafe_allow_html=True)

# Búsqueda y filtros
st.markdown("### 🔍 BUSCAR EN MIS COMPRAS")
col_search, col_filter = st.columns([3, 1])
with col_search:
    search_query = st.text_input("", placeholder="Buscar por producto, empresa, factura...")
with col_filter:
    filter_status = st.selectbox("Estado", ["Todas", "Entregadas", "En camino", "Pendientes"])

# ================== Lista de Compras ==================
st.markdown('<div class="list">', unsafe_allow_html=True)

# Compras de ejemplo
purchases = [
    {
        "id": "ORD-001",
        "product_name": "Jean Slim Azul",
        "category": "Indumentaria",
        "subcategory": "Pantalones",
        "date": "15/03/2024",
        "time": "14:30",
        "seller": "H&M",
        "company": "H&M Argentina",
        "quantity": 1,
        "unit_price": 25999,
        "total": 25999,
        "status": "Entregado",
        "rating": 9.5,
        "invoice": "FAC-2024-001"
    },
    {
        "id": "ORD-002",
        "product_name": "Remera Básica Negra",
        "category": "Indumentaria", 
        "subcategory": "Remeras",
        "date": "12/03/2024",
        "time": "10:15",
        "seller": "H&M",
        "company": "H&M Argentina",
        "quantity": 2,
        "unit_price": 8999,
        "total": 17998,
        "status": "Entregado",
        "rating": 9.0,
        "invoice": "FAC-2024-002"
    },
    {
        "id": "ORD-003", 
        "product_name": "Zapatillas Urbanas",
        "category": "Calzado",
        "subcategory": "Urbano",
        "date": "08/03/2024",
        "time": "16:45",
        "seller": "SportShop",
        "company": "Deportes S.A.",
        "quantity": 1,
        "unit_price": 45999,
        "total": 45999,
        "status": "En camino",
        "rating": "-",
        "invoice": "FAC-2024-003"
    }
]

# Aplicar filtros
filtered_purchases = [
    p for p in purchases 
    if (search_query.lower() in p["product_name"].lower() or 
        search_query.lower() in p["seller"].lower() or
        search_query.lower() in p["invoice"].lower()) and
       (filter_status == "Todas" or p["status"] == filter_status)
]

if not filtered_purchases:
    st.info("No se encontraron compras que coincidan con los filtros.")
else:
    for purchase in filtered_purchases:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        
        # Header de la compra
        col_header1, col_header2 = st.columns([3, 1])
        with col_header1:
            st.markdown(f"**🛍️ {purchase['product_name']}**")
            st.caption(f"📂 {purchase['category']} • 🔍 {purchase['subcategory']}")
        with col_header2:
            status_color = "🟢" if purchase["status"] == "Entregado" else "🟡" if purchase["status"] == "En camino" else "🔴"
            st.markdown(f"**{status_color} {purchase['status']}**")
        
        # Detalles de la compra
        col_details1, col_details2 = st.columns(2)
        with col_details1:
            st.markdown(f"""
            **📅 Fecha:** {purchase['date']} {purchase['time']}  
            **🏪 Vendedor:** {purchase['seller']}  
            **🏢 Empresa:** {purchase['company']}  
            **📦 Cantidad:** {purchase['quantity']}
            """)
        with col_details2:
            st.markdown(f"""
            **💰 Precio Unitario:** ${purchase['unit_price']:,}  
            **🧾 Factura:** {purchase['invoice']}  
            **⭐ Valoración:** {purchase['rating']}/10  
            **🎯 Estado:** {purchase['status']}
            """.replace(",", "."))
        
        # Total y acciones
        st.markdown(f"<span class='badge'>💵 TOTAL: ${purchase['total']:,}</span>".replace(",", "."), unsafe_allow_html=True)
        
        # Botones de acción
        col_btn1, col_btn2, col_btn3 = st.columns(3)
        with col_btn1:
            st.button("📄 Ver Factura", key=f"invoice_{purchase['id']}")
        with col_btn2:
            st.button("📦 Seguir Envío", key=f"track_{purchase['id']}")
        with col_btn3:
            st.button("⭐ Valorar", key=f"rate_{purchase['id']}")
        
        st.markdown("</div>", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)  # /list

# ================== Pie ==================
st.write("")
col_back = st.columns([1])[0]
with col_back:
    st.button("⬅️ VOLVER AL PANEL", key="btn_back", use_container_width=True)

st.markdown('</div>', unsafe_allow_html=True)  # /panel

# Resumen estadístico
with st.expander("📊 ESTADÍSTICAS DETALLADAS"):
    col_stat1, col_stat2, col_stat3 = st.columns(3)
    with col_stat1:
        st.metric("Total de Compras", "15")
    with col_stat2:
        st.metric("Gasto Total", "$248,950")
    with col_stat3:
        st.metric("Valoración Promedio", "9.2/10")
    
    st.markdown("**📈 Distribución por Categoría:**")
    st.markdown("- 🧥 Indumentaria: 10 compras")
    st.markdown("- 👟 Calzado: 3 compras") 
    st.markdown("- 📱 Electrónicos: 2 compras")