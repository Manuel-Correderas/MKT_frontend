# streamlit_app/pages/5b_📖_Ver_Comentarios.py
import streamlit as st

st.set_page_config(page_title="Ver comentarios", layout="centered")

# ---------- estilos ----------
st.markdown("""
<style>
.stApp { background:#FF8C00; }
.wrap{
  background:#f79b2f; border-radius:14px; padding:16px 18px;
  box-shadow:0 8px 18px rgba(0,0,0,.18);
}
.hdr{
  text-align:center; font-weight:900; letter-spacing:.6px; color:#10203a; margin-bottom:8px;
}
.sub{
  font-size:.92rem; color:#162c56;
}
.badge{
  display:inline-block; background:#d6d6d6; color:#000; font-weight:900; border-radius:8px;
  padding:6px 10px; margin:6px 0;
}
.list{
  background:#ffa84d; border-radius:10px; padding:10px; margin-top:8px;
  max-height: 420px; overflow-y: auto;
  box-shadow: inset 0 1px 4px rgba(0,0,0,.12);
}
.card{
  background:#fff5e6; border-radius:10px; padding:10px 12px;
  box-shadow:0 2px 6px rgba(0,0,0,.12); margin-bottom:10px;
}
.card .meta{
  color:#333; font-size:.85rem;
}
.card .score{
  font-weight:900; color:#0b3a91;
}
.btn-primary{ 
  background:#0b3a91 !important; 
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
</style>
""", unsafe_allow_html=True)

# ---------- cabecera ----------
st.markdown('<div class="hdr"><h3>📖 VER COMENTARIOS</h3></div>', unsafe_allow_html=True)
st.markdown('<div class="wrap">', unsafe_allow_html=True)

# Información del producto (simulada)
product_info = {
    "name": "Jean Slim Azul",
    "seller": "H&M",
    "rating": 9.2,
    "category": "Indumentaria",
    "subcategory": "Pantalones"
}

# Header del producto
c1, c2 = st.columns([4,1])
with c1:
    st.markdown("<div class='product-header'>", unsafe_allow_html=True)
    st.write(f"**📦 PRODUCTO:** {product_info['name']}")
    st.markdown(
        f"<div class='sub'>"
        f"<b>🏪 VENDEDOR:</b> {product_info['seller']} • "
        f"<b>⭐ VALORACIÓN:</b> {product_info['rating']}/10<br>"
        f"<b>📂 CATEGORÍA:</b> {product_info['category']}<br>"
        f"<b>🔍 SUBCATEGORÍA:</b> {product_info['subcategory']}"
        f"</div>", 
        unsafe_allow_html=True
    )
    st.markdown("</div>", unsafe_allow_html=True)
with c2:
    st.markdown(
        '<div style="background:#f8f9fa; border-radius:8px; padding:40px 20px; text-align:center; border:1px solid #ddd;">'
        '<span style="color:#666;">📸</span>'
        '</div>', 
        unsafe_allow_html=True
    )

# Estadísticas generales
avg_rating = 9.2
total_reviews = 8
st.markdown(
    f"<span class='badge'>📊 PUNTUACIÓN PROMEDIO: {avg_rating}/10 · {total_reviews} VALORACIONES</span>",
    unsafe_allow_html=True
)

# Filtros
st.markdown("### 🔍 FILTRAR COMENTARIOS")
col_filter1, col_filter2, col_filter3 = st.columns([2,2,2])
with col_filter1:
    min_score = st.slider("Puntuación mínima", 0.0, 10.0, 0.0, 0.5)
with col_filter2:
    search_text = st.text_input("Buscar en comentarios", "")
with col_filter3:
    sort_order = st.toggle("Ordenar por más recientes", value=True)

# ---------- listado de comentarios ----------
st.markdown("### 💬 COMENTARIOS DE CLIENTES")
st.markdown('<div class="list">', unsafe_allow_html=True)

# Comentarios de ejemplo
reviews = [
    {
        "user": "María González",
        "rating": 10.0,
        "comment": "Excelente calidad, el jean es tal como se ve en las fotos. Muy cómodo y buena terminación. Lo recomiendo 100%.",
        "date": "15/03/2024",
        "criteria": {
            "calidad": 10,
            "precio": 9,
            "durabilidad": 10
        }
    },
    {
        "user": "Carlos Rodríguez",
        "rating": 9.5,
        "comment": "Perfecto ajuste, lo recomiendo. El envío llegó antes de lo esperado y el producto en perfecto estado.",
        "date": "12/03/2024",
        "criteria": {
            "calidad": 9,
            "precio": 10,
            "durabilidad": 9
        }
    },
    {
        "user": "Laura Martínez",
        "rating": 8.0,
        "comment": "Buen producto en general, aunque el color es un poco más claro que en la foto. La calidad es aceptable.",
        "date": "10/03/2024",
        "criteria": {
            "calidad": 8,
            "precio": 8,
            "durabilidad": 8
        }
    },
    {
        "user": "Ana López",
        "rating": 9.8,
        "comment": "Increíble relación calidad-precio. Muy contenta con la compra, volvería a comprar sin dudarlo.",
        "date": "08/03/2024",
        "criteria": {
            "calidad": 10,
            "precio": 10,
            "durabilidad": 9
        }
    }
]

# Aplicar filtros
filtered_reviews = [
    r for r in reviews 
    if r["rating"] >= min_score and search_text.lower() in r["comment"].lower()
]

if sort_order:
    filtered_reviews.sort(key=lambda x: x["date"], reverse=True)

if not filtered_reviews:
    st.info("No hay comentarios que coincidan con los filtros aplicados.")
else:
    for i, review in enumerate(filtered_reviews, 1):
        st.markdown('<div class="card">', unsafe_allow_html=True)
        
        # Header del comentario
        st.markdown(f"**#{i} · ⭐ {review['rating']}/10**")
        st.caption(f"👤 por {review['user']} · 📅 {review['date']}")
        
        # Comentario principal
        st.write(f"_{review['comment']}_")
        
        # Detalle de criterios
        st.caption("**Detalle de valoración:**")
        col_crit1, col_crit2, col_crit3 = st.columns(3)
        with col_crit1:
            st.write(f"• Calidad: **{review['criteria']['calidad']}**")
        with col_crit2:
            st.write(f"• Precio: **{review['criteria']['precio']}**")
        with col_crit3:
            st.write(f"• Durabilidad: **{review['criteria']['durabilidad']}**")
        
        st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)  # /list

# Botón de volver
st.write("")
st.button("⬅️ VOLVER AL PRODUCTO", key="btn_back", use_container_width=True)

st.markdown('</div>', unsafe_allow_html=True)  # /wrap