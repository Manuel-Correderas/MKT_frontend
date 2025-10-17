# streamlit_app/pages/0b_🆕_Registrar_Usuario.py
import streamlit as st

st.set_page_config(page_title="Registrar Usuario - Ecom MKT Lab", layout="centered")

# ---- Estilos ----
st.markdown("""
<style>
.stApp { background:#FF8C00; }
.card{
  background:#ffffff; border-radius:22px; padding:30px 26px;
  box-shadow: 0 10px 24px rgba(0,0,0,.28);
}
.logo{
  background:#fff; border-radius:22px; padding:20px; margin-bottom:22px; text-align:center;
  border: 2px solid #eee;
}
.logo h1{ margin:0; font-size:1.8rem; color:#1f2e5e; }
.logo small{ color:#666; }
.btn-azul{
  background:#0b3a91; color:#fff; border:none; border-radius:8px;
  padding:10px 18px; font-weight:800; width:100%;
}
.btn-marron{
  background:#936037; color:#fff; border:none; border-radius:8px;
  padding:10px 18px; font-weight:800; width:100%;
}
.opcion label{ font-weight:700; color:#1f2e5e; }
</style>
""", unsafe_allow_html=True)

# ---- UI ----
col = st.columns([1,2,1])[1]

with col:
    st.markdown("""
    <div class="logo">
      <h1>🛒 Ecom MKT Lab</h1>
      <small>Soluciones de Marketing Digital y Comercio Electrónico</small>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🆕 Registrar Usuario")

    # Roles combinables
    st.markdown("**Seleccioná uno o más roles:**")
    comprador = st.checkbox("Registrar comprador")
    vendedor = st.checkbox("Registrar vendedor")
    admin = st.checkbox("Registrar administrador")

    st.write("")  # espacio

    colA, colB = st.columns(2)
    with colA:
        st.button("CONTINUAR", key="btn_continuar", use_container_width=True)
    with colB:
        st.button("SALIR", key="btn_salir", use_container_width=True)

    st.markdown("</div>", unsafe_allow_html=True)

# Pie de ayuda
with st.expander("ℹ️ ¿Qué rol elijo?"):
    st.markdown("""
- **Comprador**: navega productos, agrega al carrito, paga, deja comentarios y valoraciones (1–10).  
- **Vendedor**: publica y edita productos, gestiona stock y ventas, ve métricas y cobranza (alias/CBU y wallet).  
- **Administrador**: aprueba/verifica vendedores (KYC), modera contenido y ve tableros globales.
""")