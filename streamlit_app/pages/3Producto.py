# streamlit_app/pages/3_🧥_Producto.py
import streamlit as st

st.set_page_config(page_title="Producto - Ecom MKT Lab", layout="centered")

st.markdown("""
<style>
.stApp { background:#FF8C00; }
.panel { 
    background:#ffffff; 
    padding:20px; 
    border-radius:12px; 
    box-shadow: 0 8px 20px rgba(0,0,0,0.15);
}
.product-header {
    background:#ff9b2f;
    padding:15px;
    border-radius:10px;
    margin-bottom:20px;
}
.box { 
    background:#f8f9fa; 
    padding:12px; 
    border-radius:8px; 
    margin-top:12px;
    border-left: 4px solid #0b3a83;
}
.btn-primary {
    background:#0b3a83 !important; 
    color:#fff !important; 
    border:none !important; 
    border-radius:8px !important; 
    padding:10px 16px !important; 
    font-weight:700 !important;
    width:100% !important;
}
.btn-secondary {
    background:#ff9b2f !important; 
    color:#1f2e5e !important; 
    border:none !important; 
    border-radius:8px !important; 
    padding:10px 16px !important; 
    font-weight:700 !important;
    width:100% !important;
}
.badge{ 
    background:#0b3a83; 
    color:#fff; 
    border-radius:8px; 
    padding:4px 10px; 
    font-weight:700; 
    font-size:0.9rem;
}
.price{ 
    color:#0b3a83; 
    font-weight:900; 
    font-size:1.5rem;
}
.rating {
    color:#ffc107;
    font-weight:bold;
}
.seller {
    color:#936037;
    font-weight:bold;
}
</style>
""", unsafe_allow_html=True)

# Header con navegación
top = st.columns([1, 6, 1])
with top[0]:
    st.button("⬅️", key="btn_back", help="Volver al Home")
with top[1]:
    st.markdown("### 🧥 Detalle del Producto")
with top[2]:
    st.markdown("<div class='badge'>Ecom MKT Lab</div>", unsafe_allow_html=True)

# Panel principal del producto
st.markdown("<div class='panel'>", unsafe_allow_html=True)

# Información del producto (simulada)
product_name = "Jean Slim Azul"
condition = "NUEVO"
sold_count = 45
stock_count = 15
rating = 9.2
seller = "H&M"
price = 25999
description = "Jean slim fit color azul, corte moderno y cómodo. Ideal para uso diario y ocasiones especiales."

# Layout de dos columnas
col_img, col_info = st.columns([1, 1])

with col_img:
    # Espacio para imagen del producto
    st.markdown("### 📸")
    st.markdown(
        '<div style="background:#f8f9fa; border-radius:10px; padding:60px; text-align:center; border:2px dashed #ddd;">'
        '<span style="color:#666;">Imagen del Producto</span>'
        '</div>', 
        unsafe_allow_html=True
    )

with col_info:
    # Header de información
    st.markdown("<div class='product-header'>", unsafe_allow_html=True)
    st.markdown(f"### {product_name}")
    st.markdown(f"**Estado:** {condition} • **Vendidos:** {sold_count} • **Stock:** {stock_count}")
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Precio
    st.markdown(f"<div class='price'>$ {price:,.0f}</div>", unsafe_allow_html=True)
    
    # Rating y Vendedor
    st.markdown(f"<span class='rating'>⭐ {rating}/10</span> | <span class='seller'>🏪 {seller}</span>", unsafe_allow_html=True)
    
    # Descripción
    st.markdown("<div class='box'>**📝 Descripción**</div>", unsafe_allow_html=True)
    st.write(description)
    
    # Características
    st.markdown("<div class='box'>**🔍 Características**</div>", unsafe_allow_html=True)
    st.write("""
    - **Origen:** Argentina
    - **Material:** 98% Algodón, 2% Elastano
    - **Talle:** 28 al 44
    - **Color:** Azul Denim
    - **Cuidados:** Lavar a máquina 30°
    """)
    
    # Comentarios
    st.markdown("<div class='box'>**💬 Comentarios y Valoraciones**</div>", unsafe_allow_html=True)
    st.write("⭐️⭐️⭐️⭐️⭐️ *'Excelente calidad, muy cómodo'* - María L.")
    st.write("⭐️⭐️⭐️⭐️⭐️ *'Perfecto ajuste, lo recomiendo'* - Carlos R.")
    
    # Botones de acción
    st.markdown("---")
    col_buy, col_cart = st.columns(2)
    with col_buy:
        st.button("🛒 COMPRAR YA", key="btn_buy", type="primary")
    with col_cart:
        st.button("➕ Agregar al Carrito", key="btn_add_cart")

st.markdown("</div>", unsafe_allow_html=True)

# Información adicional
with st.expander("📦 Información de Envío y Devoluciones"):
    st.markdown("""
    **🚚 Envíos a todo el país**
    - Gratis en compras mayores a $30.000
    - Entrega en 3-5 días hábiles
    - Seguimiento online incluido
    
    **↩️ Devoluciones**
    - 30 días para cambios y devoluciones
    - Producto debe estar en perfecto estado
    - El costo de envío corre por el cliente
    """)