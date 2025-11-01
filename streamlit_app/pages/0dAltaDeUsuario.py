# streamlit_app/pages/0c_📝_Alta_de_usuario.py
import streamlit as st

st.set_page_config(page_title="Alta / Edición de Usuario", layout="centered")

# ---------- Estilos ----------
st.markdown("""
<style>
.stApp { background:#FF8C00; }
.panel{
  background: #f79b2f;
  border-radius: 12px;
  padding: 18px;
  box-shadow: 0 8px 18px rgba(0,0,0,.18);
}
.hdr{ font-size:1.25rem; font-weight:800; color:#1f2e5e; margin-bottom:8px; }
.lbl{ font-weight:700; color:#1f2e5e; }
.small{ color:#333; font-size:.9rem; }
.btn-azul{
  background:#0b3a91; color:#fff; border:none; border-radius:8px;
  padding:.65rem 1rem; font-weight:800; width:100%;
}
.btn-marron{
  background:#936037; color:#fff; border:none; border-radius:8px;
  padding:.65rem 1rem; font-weight:800; width:100%;
}
.divisor{ border-top:2px solid rgba(0,0,0,.1); margin:12px 0; }
</style>
""", unsafe_allow_html=True)

# ---------- UI ----------
col = st.columns([1,2,1])[1]
with col:
    st.markdown('<div class="panel">', unsafe_allow_html=True)
    st.markdown('<div class="hdr">🧑‍💻 Alta / Edición de Usuario</div>', unsafe_allow_html=True)

    # ----- Datos básicos -----
    c1, c2 = st.columns(2)
    with c1:
        nombre = st.text_input("Nombre")
        tipo_doc = st.selectbox("Tipo de Documento", ["DNI","LC","LE","CI","Pasaporte"], index=0)
        dom_env = st.text_input("Domicilio de envío")
        email = st.text_input("Email")
        tel = st.text_input("Teléfono")
    with c2:
        apellido = st.text_input("Apellido")
        nro_doc = st.text_input("N° Documento")
        dom_ent = st.text_input("Domicilio de entrega")
        cuit = st.text_input("CUIT")
        cuil = st.text_input("CUIL")

    st.markdown('<div class="divisor"></div>', unsafe_allow_html=True)

    # ----- Documentación KYC -----
    st.markdown('<span class="lbl">Adjuntar documentación</span>', unsafe_allow_html=True)
    st.file_uploader(
        "Subí DNI/CUIT/comprobante (1 o más)",
        type=["png","jpg","jpeg","pdf"],
        accept_multiple_files=True,
        label_visibility="collapsed"
    )

    st.markdown('<div class="divisor"></div>', unsafe_allow_html=True)

    # ----- Seguridad & Acceso -----
    c3, c4 = st.columns(2)
    with c3:
        palabra_seg = st.text_input("Palabra de seguridad")
        password = st.text_input("Contraseña", type="password")
    with c4:
        alias_cbu = st.text_input("CBU/CBU Alias (banco)")
        wallet = st.text_input("Wallet pública (cripto)")
        red = st.selectbox("Red", ["BEP20","ERC20","TRC20","Polygon","Arbitrum"], index=0)

    st.caption("Estos datos bancarios/cripto se usarán para generar QR y recibir pagos. "
               "El usuario es responsable de su validez.")

    st.markdown('<div class="divisor"></div>', unsafe_allow_html=True)

    # ----- Roles (multi) -----
    st.markdown("**Roles del usuario** (podés marcar uno o ambos):")
    comprador_ck = st.checkbox("COMPRADOR", value=True)
    vendedor_ck = st.checkbox("VENDEDOR", value=False)

    st.markdown('<div class="divisor"></div>', unsafe_allow_html=True)

    # ----- Términos -----
    acepto = st.checkbox("Acepto los términos de uso y privacidad")

    st.markdown('<div class="divisor"></div>', unsafe_allow_html=True)

    # ----- Botones -----
    colA, colB, colC = st.columns(3)
    with colA:
        st.button("REGISTRAR", key="btn_registrar", use_container_width=True)
    with colB:
        st.button("ACTUALIZAR", key="btn_actualizar", use_container_width=True)
    with colC:
        st.button("SALIR", key="btn_salir", use_container_width=True)

    st.markdown('</div>', unsafe_allow_html=True)

# ---- Ayuda contextual ----
with st.expander("ℹ️ Requisitos por rol"):
    st.write("""
- **COMPRADOR**
  - Datos personales, email y contraseña
  - **Domicilio de entrega** (obligatorio)
  - Aceptar Términos y Privacidad

- **VENDEDOR**
  - Todo lo anterior
  - **CBU/Alias bancario** y **Wallet pública** (obligatorio)
  - Adjuntar documentos **KYC** (DNI/CUIT/comprobante)

- **ADMIN**
  - No se auto-asigna desde esta pantalla.
""")