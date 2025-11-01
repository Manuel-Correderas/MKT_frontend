# streamlit_app/pages/4b_💳_Checkout.py
import streamlit as st

st.set_page_config(page_title="Checkout - Ecom MKT Lab", layout="centered")

# ============== ESTILOS ==============
st.markdown("""
<style>
.stApp { background:#FF8C00; }
.panel {
  background:#f79b2f; border-radius:12px; padding:16px 18px;
  box-shadow:0 8px 18px rgba(0,0,0,.18);
}
.hdr { 
    text-align:center; 
    font-weight:900; 
    color:#10203a; 
    letter-spacing:.5px; 
    margin-bottom:15px;
}
.item {
  background:#fff5e6; border-radius:10px; padding:12px; margin-bottom:10px;
  box-shadow:0 2px 8px rgba(0,0,0,.12);
}
.badge {
  display:inline-block; background:#d6d6d6; color:#000; font-weight:900;
  border-radius:8px; padding:6px 10px; margin:6px 0;
}
.btn-primary { 
    background:#0b3a91 !important; 
    color:#fff !important; 
    border:none !important; 
    border-radius:8px !important; 
    padding:10px 18px !important; 
    font-weight:800 !important;
}
.btn-secondary { 
    background:#936037 !important; 
    color:#fff !important; 
    border:none !important; 
    border-radius:8px !important; 
    padding:10px 18px !important; 
    font-weight:800 !important;
}
.section-title {
    color:#1f2e5e;
    font-weight:800;
    margin:20px 0 10px 0;
    border-bottom:2px solid #0b3a91;
    padding-bottom:5px;
}
.qr-container {
    background:#ffffff;
    border-radius:10px;
    padding:20px;
    text-align:center;
    border:2px solid #0b3a91;
    margin:15px 0;
}
</style>
""", unsafe_allow_html=True)

# ============== RESUMEN DEL PEDIDO ==============
st.markdown('<div class="hdr"><h3>💳 CHECKOUT</h3></div>', unsafe_allow_html=True)
st.markdown('<div class="panel">', unsafe_allow_html=True)

# Información del pedido
st.markdown("### 📦 RESUMEN DE TU PEDIDO")

# Productos de ejemplo en el carrito
order_items = [
    {
        "name": "Jean Slim Azul",
        "seller": "H&M",
        "quantity": 1,
        "price": 25999,
        "subtotal": 25999,
        "category": "Indumentaria",
        "subcategory": "Pantalones"
    },
    {
        "name": "Remera Básica Negra",
        "seller": "H&M", 
        "quantity": 2,
        "price": 8999,
        "subtotal": 17998,
        "category": "Indumentaria",
        "subcategory": "Remeras"
    }
]

total_pedido = sum(item["subtotal"] for item in order_items)

for item in order_items:
    col_item1, col_item2 = st.columns([3, 1])
    with col_item1:
        st.markdown('<div class="item">', unsafe_allow_html=True)
        st.markdown(f"**{item['name']}**")
        st.markdown(f"Vendedor: {item['seller']} • {item['category']} • {item['subcategory']}")
        st.markdown(f"Cantidad: {item['quantity']} • Precio unitario: ${item['price']:,}")
        st.markdown(f'<span class="badge">Subtotal: ${item["subtotal"]:,}</span>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    with col_item2:
        st.markdown(
            '<div style="background:#f8f9fa; border-radius:8px; padding:30px 15px; text-align:center; border:1px solid #ddd;">'
            '<span style="color:#666;">📸</span>'
            '</div>', 
            unsafe_allow_html=True
        )

st.markdown(f"### 💰 TOTAL DEL PEDIDO: ${total_pedido:,}")

st.markdown("</div>", unsafe_allow_html=True)

# ============== MÉTODO DE PAGO ==============
st.markdown('<div class="panel">', unsafe_allow_html=True)
st.markdown('<div class="section-title">💳 MÉTODO DE PAGO</div>', unsafe_allow_html=True)

payment_method = st.radio(
    "Seleccioná tu método de pago:",
    ["Transferencia Bancaria", "Mercado Pago", "Tarjeta de Crédito", "Criptomonedas"],
    horizontal=True
)

if payment_method == "Transferencia Bancaria":
    st.markdown("#### 🏦 Transferencia Bancaria")
    col_bank1, col_bank2 = st.columns(2)
    with col_bank1:
        st.markdown("**Datos para transferencia:**")
        st.markdown("""
        - **Banco:** Galicia
        - **Titular:** H&M Argentina
        - **CBU:** 0070000000001234567890
        - **Alias:** HMVENTAS.GALICIA
        """)
    with col_bank2:
        st.markdown('<div class="qr-container">', unsafe_allow_html=True)
        st.markdown("**📱 Código QR**")
        st.markdown(
            '<div style="background:#f8f9fa; border-radius:8px; padding:60px 30px; text-align:center; border:1px solid #ddd; margin:10px 0;">'
            '<span style="color:#666;">QR Code</span>'
            '</div>', 
            unsafe_allow_html=True
        )
        st.markdown("Escaneá con tu app bancaria")
        st.markdown('</div>', unsafe_allow_html=True)

elif payment_method == "Mercado Pago":
    st.markdown("#### 📱 Mercado Pago")
    st.markdown("**🔗 Link de pago:** https://mpago.la/1a2b3c4d")
    st.markdown("**💡 Instrucciones:**")
    st.markdown("1. Hacé clic en el link de arriba")
    st.markdown("2. Completá los datos de tu tarjeta o cuenta de Mercado Pago")
    st.markdown("3. Confirmá el pago")

elif payment_method == "Tarjeta de Crédito":
    st.markdown("#### 💳 Tarjeta de Crédito")
    col_card1, col_card2 = st.columns(2)
    with col_card1:
        st.text_input("Número de tarjeta", placeholder="1234 5678 9012 3456")
        st.text_input("Nombre del titular", placeholder="Como figura en la tarjeta")
    with col_card2:
        col_exp, col_cvv = st.columns(2)
        with col_exp:
            st.text_input("Vencimiento", placeholder="MM/AA")
        with col_cvv:
            st.text_input("CVV", placeholder="123")
    st.markdown("💡 Pago procesado de forma segura")

elif payment_method == "Criptomonedas":
    st.markdown("#### ₿ Criptomonedas")
    col_crypto1, col_crypto2 = st.columns(2)
    with col_crypto1:
        crypto_network = st.selectbox("Red", ["BEP-20", "ERC-20", "TRC-20", "Polygon"])
        st.markdown(f"**Wallet:** 0x742d35Cc6634C0532925a3b8D...")
        st.markdown(f"**Monto aproximado en USDT:** {total_pedido/1000:.2f}")
    with col_crypto2:
        st.markdown('<div class="qr-container">', unsafe_allow_html=True)
        st.markdown("**📱 QR Cripto**")
        st.markdown(
            '<div style="background:#f8f9fa; border-radius:8px; padding:60px 30px; text-align:center; border:1px solid #ddd; margin:10px 0;">'
            '<span style="color:#666;">QR Code</span>'
            '</div>', 
            unsafe_allow_html=True
        )
        st.markdown("Escaneá con tu wallet")
        st.markdown('</div>', unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# ============== INFORMACIÓN DE ENVÍO ==============
st.markdown('<div class="panel">', unsafe_allow_html=True)
st.markdown('<div class="section-title">🚚 INFORMACIÓN DE ENVÍO</div>', unsafe_allow_html=True)

col_shipping1, col_shipping2 = st.columns(2)
with col_shipping1:
    shipping_name = st.text_input("Nombre completo", value="María González")
    shipping_address = st.text_area("Dirección de envío", value="Av. Siempre Viva 123, CABA")
with col_shipping2:
    shipping_phone = st.text_input("Teléfono de contacto", value="+54 9 11 1234-5678")
    shipping_notes = st.text_area("Instrucciones especiales", placeholder="Ej: Timbre azul, dejar con portero")

st.markdown("**📦 Método de envío:** Estándar (3-5 días hábiles)")
st.markdown("**💰 Costo de envío:** Gratis (compra mayor a $30.000)")

st.markdown("</div>", unsafe_allow_html=True)

# ============== CONFIRMACIÓN ==============
st.markdown('<div class="panel">', unsafe_allow_html=True)
st.markdown('<div class="section-title">✅ CONFIRMAR COMPRA</div>', unsafe_allow_html=True)

# Comprobante de pago
st.markdown("#### 📎 Comprobante de Pago")
proof_file = st.file_uploader("Subí tu comprobante de pago (opcional)", type=["jpg", "png", "pdf"])

# Notas adicionales
order_notes = st.text_area("Notas para el vendedor", placeholder="Algún comentario especial sobre tu pedido...")

# Botones de acción
col_confirm1, col_confirm2 = st.columns(2)
with col_confirm1:
    if st.button("✅ CONFIRMAR PEDIDO", key="btn_confirm", type="primary", use_container_width=True):
        st.success("🎉 ¡Pedido confirmado! Te enviaremos un email con los detalles.")
        st.balloons()
with col_confirm2:
    if st.button("⬅️ VOLVER AL CARRITO", key="btn_back", use_container_width=True):
        st.switch_page("pages/4_🛒_Mi_Carrito.py")

st.markdown("</div>", unsafe_allow_html=True)

# Información de contacto
with st.expander("📞 CONTACTO Y AYUDA"):
    st.markdown("""
    **¿Necesitás ayuda con tu compra?**
    
    📧 Email: soporte@ecommktlab.com
    📞 Teléfono: +54 11 1234-5678
    💬 WhatsApp: +54 9 11 8765-4321
    
    **Horarios de atención:**
    Lunes a Viernes: 9:00 - 18:00
    Sábados: 9:00 - 13:00
    """)