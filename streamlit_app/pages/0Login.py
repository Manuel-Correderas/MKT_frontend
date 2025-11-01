# streamlit_app/pages/0_🔐_Login.py
import streamlit as st

st.set_page_config(page_title="Login - Ecom MKT Lab", layout="centered")

# ---------- Estilos ----------
st.markdown("""
<style>
.stApp {background:#FF8C00;}
.login-card{
  background:#fff; border-radius:18px; padding:32px 28px;
  box-shadow:0 8px 22px rgba(0,0,0,.25);
}
.btn{
  background:#0b3a91; color:#fff; border:none; border-radius:8px;
  padding:10px 16px; font-weight:700; width:100%;
}
.logo-box{ 
  background:#fff; border-radius:18px; padding:18px 22px; 
  margin-bottom:20px; text-align:center;
  box-shadow:0 4px 14px rgba(0,0,0,.18);
}
.logo-title{ font-size:1.8rem; font-weight:800; color:#1f2e5e; }
.logo-sub{ font-size:.9rem; color:#666; }
</style>
""", unsafe_allow_html=True)

# ---------- UI ----------
st.write("")
col = st.columns([1,2,1])[1]
with col:
    st.markdown("""
        <div class="logo-box">
            <div class="logo-title">🛒 Ecom MKT Lab</div>
            <div class="logo-sub">Soluciones de Marketing Digital y Comercio Electrónico</div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="login-card">', unsafe_allow_html=True)
    st.markdown("### Iniciar sesión")
    st.text_input("Email", placeholder="tu@correo.com")
    st.text_input("Contraseña", type="password", placeholder="••••••••")

    st.write("")
    c1, c2, c3 = st.columns(3)
    with c1:
        if st.button("INGRESAR", use_container_width=True):
            st.switch_page("Home.py")
    with c2:
        if st.button("SALIR", use_container_width=True):
            st.switch_page("Home.py")
    with c3:
        if st.button("REGISTRARSE", use_container_width=True):
            st.switch_page("pages/0b_🆕_Registrar_Usuario.py")

    st.write("")
    if st.button("He olvidado la contraseña", use_container_width=True):
        st.switch_page("pages/0d_🔑_Olvidé_mi_contraseña.py")

    st.markdown('</div>', unsafe_allow_html=True)
