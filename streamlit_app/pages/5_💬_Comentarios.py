# streamlit_app/pages/5_💬_Comentarios.py
import streamlit as st

st.set_page_config(page_title="Comentarios y Valoración", layout="centered")

# --------- estilos ----------
st.markdown("""
<style>
.stApp { background:#FF8C00; }
.panel{
  background:#f79b2f; border-radius:12px; padding:16px 18px;
  box-shadow:0 8px 18px rgba(0,0,0,.18);
}
.hdr{
  text-align:center; font-weight:900; letter-spacing:.6px;
  color:#10203a; margin-bottom:10px;
}
.row{
  background:#ffa84d; border-radius:10px; padding:6px 8px; margin:6px 0;
  box-shadow:0 1px 4px rgba(0,0,0,.12);
}
.row .lbl{ color:#1b2749; font-weight:700; }
.counter{
  display:flex; gap:6px; justify-content:flex-end; align-items:center;
}
.counter .score{
  background:#d6d6d6; color:#000; font-weight:900; border-radius:6px; padding:3px 8px; min-width:28px; text-align:center;
}
.counter button{ font-weight:900; }
.badge{
  display:inline-block; background:#d6d6d6; color:#000; font-weight:900; border-radius:8px;
  padding:6px 10px; margin:6px 0;
}
.btn-primary{ 
  background:#0b3a91 !important; 
  color:#fff !important; 
  border:none !important; 
  border-radius:8px !important; 
  padding:10px 18px !important; 
  font-weight:900 !important;
}
.btn-secondary{ 
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
</style>
""", unsafe_allow_html=True)

# --------- cabecera ----------
st.markdown('<div class="hdr"><h3>💬 COMENTARIOS Y VALORACIÓN</h3></div>', unsafe_allow_html=True)
st.markdown('<div class="panel">', unsafe_allow_html=True)

# Información del producto (simulada)
product_info = {
    "name": "Jean Slim Azul",
    "seller": "H&M",
    "rating": 9.2,
    "category": "Indumentaria",
    "subcategory": "Pantalones"
}

# Header del producto
colL, colR = st.columns([4,1])
with colL:
    st.markdown("<div class='product-header'>", unsafe_allow_html=True)
    st.write(f"**📦 PRODUCTO:** {product_info['name']}")
    st.caption(
        f"**🏪 VENDEDOR:** {product_info['seller']} • **⭐ VALORACIÓN:** {product_info['rating']}/10  \n"
        f"**📂 CATEGORÍA:** {product_info['category']}  \n"
        f"**🔍 SUBCATEGORÍA:** {product_info['subcategory']}"
    )
    st.markdown("</div>", unsafe_allow_html=True)
with colR:
    st.markdown(
        '<div style="background:#f8f9fa; border-radius:8px; padding:40px 20px; text-align:center; border:1px solid #ddd;">'
        '<span style="color:#666;">📸</span>'
        '</div>', 
        unsafe_allow_html=True
    )

st.write("")

# --------- criterios de valoración 1-10 ----------
criteria = [
    ("calidad_general", "⭐ CALIDAD GENERAL"),
    ("relacion_calidad_precio", "💰 RELACIÓN CALIDAD-PRECIO"),
    ("durabilidad", "🛡️ DURABILIDAD"),
    ("descripcion_fiel", "📝 DESCRIPCIÓN FIEL"),
    ("embalaje_recepcion", "📦 EMBALAJE / ESTADO AL RECIBIR"),
    ("satisfaccion_global", "😊 SATISFACCIÓN GLOBAL"),
    ("diseno_estetica", "🎨 DISEÑO Y ESTÉTICA"),
]

# Inicializar puntuaciones
for key, _ in criteria:
    if f"rating_{key}" not in st.session_state:
        st.session_state[f"rating_{key}"] = 9

total_points = 0
for key, label in criteria:
    current_rating = st.session_state[f"rating_{key}"]
    
    colA, colB = st.columns([3,2])
    with colA:
        st.markdown(f'<div class="row"><span class="lbl">{label}</span></div>', unsafe_allow_html=True)
    with colB:
        c1, c2, c3 = st.columns([1,1,2])
        with c1:
            if st.button("−", key=f"sub_{key}"):
                st.session_state[f"rating_{key}"] = max(1, current_rating - 1)
                st.rerun()
        with c2:
            st.markdown(f"<div class='counter'><span class='score'>{st.session_state[f'rating_{key}']}</span></div>", unsafe_allow_html=True)
        with c3:
            if st.button("+", key=f"add_{key}"):
                st.session_state[f"rating_{key}"] = min(10, current_rating + 1)
                st.rerun()
    
    total_points += st.session_state[f"rating_{key}"]

# Puntuación final (promedio)
avg_score = round(total_points / len(criteria), 1)
st.markdown(f"<span class='badge'>🎯 PUNTUACIÓN FINAL: {avg_score}/10</span>", unsafe_allow_html=True)

# Comentario
st.markdown("### 💭 TU COMENTARIO")
comment = st.text_area(
    "Compartí tu experiencia con este producto...",
    height=120,
    placeholder="¿Qué te pareció el producto? ¿Recomendarías la compra? ¿Algún aspecto a mejorar?",
    label_visibility="collapsed"
)

# Botones de acción
st.write("")
col_send, col_back = st.columns(2)
with col_send:
    st.button("📤 ENVIAR VALORACIÓN", key="btn_send", type="primary")
with col_back:
    st.button("⬅️ VOLVER", key="btn_back")

st.markdown("</div>", unsafe_allow_html=True)

# Comentarios existentes (ejemplo)
with st.expander("📖 COMENTARIOS EXISTENTES"):
    st.markdown("""
    **⭐️⭐️⭐️⭐️⭐️ María González**
    *"Excelente calidad, el jean es tal como se ve en las fotos. Muy cómodo y buena terminación."*
    
    **⭐️⭐️⭐️⭐️⭐️ Carlos Rodríguez**  
    *"Perfecto ajuste, lo recomiendo 100%. El envío llegó antes de lo esperado."*
    
    **⭐️⭐️⭐️⭐️ Laura Martínez**
    *"Buen producto en general, aunque el color es un poco más claro que en la foto."*
    """)