# streamlit_app/pages/4_🛒_Mi_Carrito.py
import streamlit as st

st.set_page_config(page_title="Mi Carrito", layout="centered")

# ===== estilos =====
st.markdown("""
<style>
.stApp { background:#FF8C00; }
.cart-panel{
  background:#f79b2f; border-radius:12px; padding:16px 18px;
  box-shadow:0 8px 18px rgba(0,0,0,.18);
}
.hdr { text-align:center; font-weight:900; letter-spacing:.5px;
  color:#113; margin-bottom:12px; font-size:1.1rem; }
.item{
  background:#fff5e6; border-radius:10px; padding:12px 12px;
  box-shadow:0 2px 8px rgba(0,0,0,.12); margin-bottom:10px;
}
.item .title{ font-weight:800; color:#1f2e5e; margin-bottom:4px; }
.item .meta { font-size:.9rem; color:#222; line-height:1.15rem; }
.badge-total{ display:inline-block; background:#d6d6d6; color:#000; font-weight:900;
  border-radius:8px; padding:6px 10px; margin:6px 0; }
.controls{ display:flex; gap:8px; align-items:center; justify-content:flex-end; }
.controls button{ background:#0b3a91; color:#fff; border:none; border-radius:8px; padding:6px 10px; font-weight:800; }
.controls .danger{ background:#c0392b; }
.footer-btn{ background:#0b3a91; color:#fff; border:none; border-radius:8px; padding:10px 18px; font-weight:900; }
.footer-btn.secondary{ background:#936037; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="hdr">🛒 MI CARRITO</div>', unsafe_allow_html=True)

# ===== productos de ejemplo en el carrito =====
cart_items = [
    {
        "name": "Jean Slim Azul",
        "seller": "H&M",
        "rating": 9.2,
        "category": "Indumentaria",
        "subcategory": "Pantalones",
        "stock": 15,
        "qty": 1,
        "price": 25999,
        "subtotal": 25999
    },
    {
        "name": "Remera Básica Negra", 
        "seller": "H&M",
        "rating": 8.7,
        "category": "Indumentaria",
        "subcategory": "Remeras",
        "stock": 20,
        "qty": 2,
        "price": 8999,
        "subtotal": 17998
    }
]

if not cart_items:
    st.info("Tu carrito está vacío.")
    st.stop()

total_general = sum(item["subtotal"] for item in cart_items)

st.markdown('<div class="cart-panel">', unsafe_allow_html=True)

for idx, item in enumerate(cart_items):
    # tarjeta de producto
    with st.container():
        st.markdown('<div class="item">', unsafe_allow_html=True)
        st.markdown(f'<div class="title">{item["name"]}</div>', unsafe_allow_html=True)

        colL, colM, colR = st.columns([3,1,2])
        with colL:
            st.markdown(
                f"""<div class="meta">
                <b>VENDEDOR:</b> {item["seller"]} &nbsp;&nbsp; <b>VALORACIÓN:</b> {item["rating"]}/10<br>
                <b>CATEGORÍA:</b> {item["category"]}<br>
                <b>SUBCATEGORÍA:</b> {item["subcategory"]}<br>
                <b>STOCK:</b> {item["stock"]}<br>
                <b>CANTIDAD:</b> {item["qty"]}<br>
                <b>PRECIO UNITARIO:</b> ${item["price"]:,}$ 
                </div>""".replace(",", "."),
                unsafe_allow_html=True
            )
            st.checkbox("Añadir al checkout", value=True, key=f"chk_{idx}")
            st.markdown(f'<span class="badge-total">SUBTOTAL: ${item["subtotal"]:,}$</span>'.replace(",", "."), unsafe_allow_html=True)

        with colM:
            st.markdown(
                '<div style="background:#f8f9fa; border-radius:8px; padding:40px 20px; text-align:center; border:1px solid #ddd;">'
                '<span style="color:#666;">📸</span>'
                '</div>', 
                unsafe_allow_html=True
            )

        with colR:
            st.markdown('<div class="controls">', unsafe_allow_html=True)
            c_sub, c_qty, c_add = st.columns([1,1,1])
            with c_sub:
                st.button("−", key=f"sub_{idx}")
            with c_qty:
                st.write(f"**{item['qty']}**")
            with c_add:
                st.button("+", key=f"add_{idx}")

            st.write("")
            st.button("🗑 Quitar", key=f"rm_{idx}")
            st.markdown('</div>', unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)
        st.divider()

st.markdown("</div>", unsafe_allow_html=True)

# Total y botones de acción
st.subheader(f"💰 TOTAL A PAGAR: ${total_general:,}$".replace(",", "."))

col1, col2 = st.columns(2)
with col1:
    st.button("💳 PAGAR", key="pay", use_container_width=True)
with col2:
    st.button("⬅️ VOLVER", key="back", use_container_width=True)

# Información adicional
with st.expander("📦 Información de Compra"):
    st.markdown("""
    **Métodos de pago aceptados:**
    - 💳 Tarjetas de crédito/débito
    - 🏦 Transferencia bancaria
    - ₿ Criptomonedas
    - 📱 Mercado Pago
    
    **Envío:** Gratis en compras mayores a $30.000
    **Tiempo de entrega:** 3-5 días hábiles
    """)