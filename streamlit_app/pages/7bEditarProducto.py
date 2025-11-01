# streamlit_app/pages/7b_✏️_Editar_Producto.py
import streamlit as st

st.set_page_config(page_title="Editar Producto (Vendedor)", layout="centered")

# ===== Estilos =====
st.markdown("""
<style>
.stApp { background:#FF8C00; }
.panel{
  background:#f79b2f; border-radius:14px; padding:18px;
  box-shadow:0 8px 18px rgba(0,0,0,.18);
}
.hdr{ 
    text-align:center; 
    font-weight:900; 
    letter-spacing:.6px; 
    color:#10203a; 
    margin-bottom:10px; 
}
.btn-primary { 
    background:#0b3a91 !important; 
    color:#fff !important; 
    border:none !important; 
    border-radius:8px !important; 
    padding:10px 18px !important; 
    font-weight:900 !important;
}
.btn-secondary { 
    background:#936037 !important; 
    color:#fff !important; 
    border:none !important; 
    border-radius:8px !important; 
    padding:10px 18px !important; 
    font-weight:900 !important;
}
.product-header {
    background:#ff9b2f;
    padding:12px;
    border-radius:8px;
    margin-bottom:15px;
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

# ===== Encabezado =====
st.markdown('<div class="hdr"><h3>✏️ EDITAR PRODUCTO</h3></div>', unsafe_allow_html=True)
st.markdown('<div class="panel">', unsafe_allow_html=True)

# Información del producto
st.markdown("<div class='product-header'>", unsafe_allow_html=True)
col_info1, col_info2 = st.columns([1, 3])
with col_info1:
    st.markdown(
        '<div style="background:#f8f9fa; border-radius:8px; padding:40px 20px; text-align:center; border:1px solid #ddd;">'
        '<span style="color:#666;">📸</span>'
        '</div>', 
        unsafe_allow_html=True
    )
with col_info2:
    st.markdown("### Jean Slim Azul")
    st.markdown("**🏪 Vendedor:** H&M • **⭐ Valoración:** 9.2/10 • **🎯 Ventas:** 45 unidades")
    st.markdown("**📂 Categoría:** Indumentaria • **🔍 Subcategoría:** Pantalones")
st.markdown("</div>", unsafe_allow_html=True)

# ===== Información Básica =====
st.markdown('<div class="section-title">📝 INFORMACIÓN BÁSICA</div>', unsafe_allow_html=True)

col_basic1, col_basic2 = st.columns(2)
with col_basic1:
    product_name = st.text_input("Nombre del producto", value="Jean Slim Azul")
    product_category = st.text_input("Categoría", value="Indumentaria")
    product_subcategory = st.text_input("Subcategoría", value="Pantalones")
with col_basic2:
    product_stock = st.number_input("Stock disponible", min_value=0, value=15, step=1)
    product_price = st.number_input("Precio unitario ($)", min_value=0, value=25999, step=100)
    product_image = st.text_input("URL de imagen", value="https://ejemplo.com/jean-azul.jpg")

# ===== Descripción y Características =====
st.markdown('<div class="section-title">📋 DESCRIPCIÓN Y CARACTERÍSTICAS</div>', unsafe_allow_html=True)

product_description = st.text_area(
    "Descripción breve del producto", 
    value="Jean slim fit color azul, corte moderno y cómodo. Ideal para uso diario y ocasiones especiales.",
    height=100
)

product_features = st.text_area(
    "Características técnicas", 
    value="• 98% Algodón, 2% Elastano\n• Tallas disponibles: 28 al 44\n• Color: Azul Denim\n• Cuidados: Lavar a máquina 30°",
    height=120
)

# ===== Configuración de Pagos =====
st.markdown('<div class="section-title">💳 CONFIGURACIÓN DE PAGOS</div>', unsafe_allow_html=True)

col_payment1, col_payment2 = st.columns(2)
with col_payment1:
    payment_method = st.selectbox(
        "Método de pago principal", 
        ["Transferencia Bancaria", "Mercado Pago", "Tarjeta de Crédito", "Criptomonedas"],
        index=0
    )
    payment_alias = st.text_input("Alias/CBU", value="H&M.VENTAS")
with col_payment2:
    crypto_network = st.selectbox(
        "Red para criptomonedas", 
        ["BEP-20", "ERC-20", "TRC-20", "Polygon"],
        index=0
    )
    crypto_wallet = st.text_input("Wallet address", value="0x742...d35")

# ===== Información Adicional =====
st.markdown('<div class="section-title">📊 INFORMACIÓN ADICIONAL</div>', unsafe_allow_html=True)

col_extra1, col_extra2 = st.columns(2)
with col_extra1:
    product_condition = st.selectbox(
        "Condición del producto",
        ["Nuevo", "Como nuevo", "Usado - Excelente", "Usado - Bueno"],
        index=0
    )
    product_weight = st.number_input("Peso (kg)", min_value=0.0, value=0.5, step=0.1)
with col_extra2:
    product_dimensions = st.text_input("Dimensiones (LxAxA cm)", value="30x20x5")
    shipping_time = st.number_input("Tiempo de envío (días)", min_value=1, value=3, step=1)

# ===== Botones de Acción =====
st.markdown("---")
col_btn1, col_btn2, col_btn3 = st.columns(3)

with col_btn1:
    st.button("💾 GUARDAR CAMBIOS", key="btn_save", type="primary", use_container_width=True)

with col_btn2:
    st.button("🔄 RESTABLECER", key="btn_reset", use_container_width=True)

with col_btn3:
    st.button("⬅️ VOLVER A MIS PRODUCTOS", key="btn_back", use_container_width=True)

# ===== Vista Previa =====
with st.expander("👁️ VISTA PREVIA DEL PRODUCTO"):
    st.markdown("### Jean Slim Azul")
    col_preview1, col_preview2 = st.columns([1, 2])
    with col_preview1:
        st.markdown(
            '<div style="background:#f8f9fa; border-radius:8px; padding:60px 30px; text-align:center; border:1px solid #ddd;">'
            '<span style="color:#666;">Imagen del Producto</span>'
            '</div>', 
            unsafe_allow_html=True
        )
    with col_preview2:
        st.markdown("**Precio:** $25.999")
        st.markdown("**Stock:** 15 unidades")
        st.markdown("**⭐ 9.2/10** (45 valoraciones)")
        st.markdown("**Envío:** 3-5 días hábiles")
    
    st.markdown("**Descripción:**")
    st.write("Jean slim fit color azul, corte moderno y cómodo. Ideal para uso diario y ocasiones especiales.")
    
    st.markdown("**Características:**")
    st.write("• 98% Algodón, 2% Elastano")
    st.write("• Tallas disponibles: 28 al 44") 
    st.write("• Color: Azul Denim")
    st.write("• Cuidados: Lavar a máquina 30°")

st.markdown('</div>', unsafe_allow_html=True)  # /panel