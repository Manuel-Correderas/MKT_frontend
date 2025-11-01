# streamlit_app/pages/7_📦_Mis_Productos.py
import streamlit as st

st.set_page_config(page_title="Mis Productos (Vendedor)", layout="centered")

# ------------- estilos -------------
st.markdown("""
<style>
.stApp { background:#FF8C00; }
.panel{
  background:#f79b2f; border-radius:14px; padding:16px 18px;
  box-shadow:0 8px 18px rgba(0,0,0,.18);
}
.hdr{ 
    text-align:center; 
    font-weight:900; 
    letter-spacing:.6px; 
    color:#10203a; 
    margin-bottom:10px;
}
.sub{ 
    color:#162c56; 
    font-size:.92rem; 
}
.list{
  background:#ffa84d; border-radius:10px; padding:10px; margin-top:8px;
  max-height: 460px; overflow-y: auto; box-shadow: inset 0 1px 4px rgba(0,0,0,.12);
}
.card{
  background:#fff5e6; border-radius:10px; padding:12px;
  box-shadow:0 2px 8px rgba(0,0,0,.12); margin-bottom:10px;
}
.small{ 
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
.btn-danger { 
    background:#c0392b !important; 
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
</style>
""", unsafe_allow_html=True)

# ------------- cabecera -------------
st.markdown('<div class="hdr"><h3>📦 MIS PRODUCTOS</h3></div>', unsafe_allow_html=True)
st.markdown('<div class="panel">', unsafe_allow_html=True)

# Información del vendedor
st.markdown("<div class='seller-header'>", unsafe_allow_html=True)
st.markdown("### 🏪 H&M - VENDEDOR")
st.markdown("**📊 RESUMEN:** 12 PRODUCTOS • ⭐ 9.2 VALORACIÓN PROMEDIO • 🎯 156 VENTAS TOTALES")
st.markdown("</div>", unsafe_allow_html=True)

# Configuración del vendedor
st.markdown("### ⚙️ CONFIGURACIÓN DE VENDEDOR")
col_alias, col_logo = st.columns([2, 2])
with col_alias:
    seller_alias = st.text_input("Alias de vendedor", value="H&M", placeholder="Nombre de tu tienda")
with col_logo:
    logo_url = st.text_input("URL del logo (opcional)", placeholder="https://ejemplo.com/logo.png")

# ------------- lista de productos -------------
st.markdown("### 🛍️ MIS PRODUCTOS PUBLICADOS")
st.markdown('<div class="list">', unsafe_allow_html=True)

# Productos de ejemplo
products = [
    {
        "id": 1,
        "name": "Jean Slim Azul",
        "category": "Indumentaria",
        "subcategory": "Pantalones",
        "price": 25999,
        "stock": 15,
        "rating": 9.2,
        "sold": 45,
        "image": "📸",
        "description": "Jean slim fit color azul, corte moderno",
        "features": "98% Algodón, 2% Elastano\nTallas 28-44\nColor Azul Denim"
    },
    {
        "id": 2,
        "name": "Remera Básica Negra",
        "category": "Indumentaria",
        "subcategory": "Remeras", 
        "price": 8999,
        "stock": 20,
        "rating": 8.7,
        "sold": 32,
        "image": "📸",
        "description": "Remera básica de algodón peinado",
        "features": "100% Algodón\nTalles S-XXL\nColor Negro"
    },
    {
        "id": 3,
        "name": "Zapatillas Urbanas",
        "category": "Calzado",
        "subcategory": "Urbano",
        "price": 45999,
        "stock": 8,
        "rating": 9.5,
        "sold": 18,
        "image": "📸",
        "description": "Zapatillas urbanas con suela antideslizante",
        "features": "Cuero sintético\nSuela de goma\nTalles 36-44"
    }
]

for product in products:
    st.markdown('<div class="card">', unsafe_allow_html=True)

    # Header del producto
    col_header1, col_header2, col_header3 = st.columns([4, 1, 1])
    with col_header1:
        st.markdown(f"**{product['name']}**")
        st.caption(f"📂 {product['category']} • 🔍 {product['subcategory']}")
    with col_header2:
        st.markdown(
            '<div style="background:#f8f9fa; border-radius:8px; padding:20px; text-align:center; border:1px solid #ddd;">'
            f'<span style="color:#666;">{product["image"]}</span>'
            '</div>', 
            unsafe_allow_html=True
        )
    with col_header3:
        st.markdown(f"**⭐ {product['rating']}**")
        st.markdown(f"**🎯 {product['sold']} vendidos**")

    # Campos editables
    col_name, col_category = st.columns(2)
    with col_name:
        product_name = st.text_input("Nombre del producto", value=product["name"], key=f"name_{product['id']}")
    with col_category:
        product_category = st.text_input("Categoría", value=product["category"], key=f"cat_{product['id']}")
    
    col_subcategory, col_price = st.columns(2)
    with col_subcategory:
        product_subcategory = st.text_input("Subcategoría", value=product["subcategory"], key=f"sub_{product['id']}")
    with col_price:
        product_price = st.number_input("Precio unitario", value=product["price"], min_value=0, key=f"price_{product['id']}")
    
    col_stock, col_image = st.columns(2)
    with col_stock:
        product_stock = st.number_input("Stock disponible", value=product["stock"], min_value=0, key=f"stock_{product['id']}")
    with col_image:
        product_image = st.text_input("URL de imagen", value=product["image"], key=f"img_{product['id']}")
    
    product_description = st.text_area("Descripción breve", value=product["description"], key=f"desc_{product['id']}")
    product_features = st.text_area("Características", value=product["features"], key=f"feat_{product['id']}")

    # Botones de acción
    col_btn1, col_btn2, col_btn3 = st.columns(3)
    with col_btn1:
        st.button("💾 GUARDAR CAMBIOS", key=f"save_{product['id']}", use_container_width=True)
    with col_btn2:
        st.button("✏️ EDITAR COMPLETO", key=f"edit_{product['id']}", use_container_width=True)
    with col_btn3:
        st.button("🗑 ELIMINAR", key=f"delete_{product['id']}", use_container_width=True)

    st.markdown("</div>", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)  # /list

# ------------- agregar nuevo producto -------------
st.markdown("### ➕ AGREGAR NUEVO PRODUCTO")
with st.form("nuevo_producto"):
    col_new1, col_new2 = st.columns(2)
    with col_new1:
        new_name = st.text_input("Nombre del producto", key="new_name")
        new_category = st.text_input("Categoría", key="new_category")
        new_subcategory = st.text_input("Subcategoría", key="new_subcategory")
    with col_new2:
        new_price = st.number_input("Precio unitario", min_value=0, value=0, key="new_price")
        new_stock = st.number_input("Stock inicial", min_value=0, value=0, key="new_stock")
        new_image = st.text_input("URL de imagen", key="new_image")
    
    new_description = st.text_area("Descripción breve", key="new_description")
    new_features = st.text_area("Características", key="new_features")
    
    col_submit, col_clear = st.columns(2)
    with col_submit:
        submitted = st.form_submit_button("✅ AGREGAR PRODUCTO", use_container_width=True)
    with col_clear:
        st.form_submit_button("🔄 LIMPIAR FORMULARIO", use_container_width=True)

# Botón de volver
st.write("")
st.button("⬅️ VOLVER AL PANEL", key="btn_back", use_container_width=True)

st.markdown('</div>', unsafe_allow_html=True)  # /panel