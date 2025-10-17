# streamlit_app/pages/1_🔑_Olvidé_mi_contraseña.py
import streamlit as st

st.set_page_config(page_title="Olvidé mi contraseña - Ecom MKT Lab", layout="centered")

# ---- estilos ----
st.markdown("""
<style>
.stApp { background:#FF8C00; }
.card{
  background:#fff; border-radius:18px; padding:28px; 
  box-shadow:0 8px 22px rgba(0,0,0,.25);
}
.logo-box{
  background:#fff; border-radius:18px; padding:18px 22px; 
  margin-bottom:18px; text-align:center;
}
.logo-title{ font-size:1.8rem; font-weight:800; color:#1f2e5e; }
.logo-sub{ font-size:.9rem; color:#666; }
.btn-azul{
  background:#0b3a91; color:#fff; border:none; border-radius:8px; 
  padding:10px 16px; font-weight:700;
}
.btn-marron{
  background:#936037; color:#fff; border:none; border-radius:8px; 
  padding:10px 16px; font-weight:700;
}
</style>
""", unsafe_allow_html=True)

# ---- UI ----
st.write("")
col = st.columns([1,2,1])[1]
with col:
    st.markdown("""
    <div class="logo-box">
        <div class="logo-title">🛒 Ecom MKT Lab</div>
        <div class="logo-sub">Soluciones de Marketing Digital y Comercio Electrónico</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🔑 Olvidé mi contraseña")

    with st.form("forgot_form", clear_on_submit=False):
        email = st.text_input("Email registrado")
        celular = st.text_input("Celular/Móvil", placeholder="+54 9 11 1234-5678")
        palabra = st.text_input("Palabra de seguridad", type="password")
        enviar = st.form_submit_button("ENVIAR")

    colA, colB = st.columns(2)
    if colB.button("SALIR", key="btn_salir", use_container_width=True):
        st.switch_page("pages/0_🔐_Login.py")

    st.markdown('</div>', unsafe_allow_html=True)

# ---- Info de seguridad (opcional) ----
with st.expander("ℹ️ Ayuda y seguridad"):
    st.markdown("""
- Verificamos **email + móvil + palabra de seguridad** para evitar usos indebidos.
- Si no recordás la palabra de seguridad, contactá al soporte del sistema.
- El enlace/código de reseteo expira en pocos minutos por tu seguridad.
""")