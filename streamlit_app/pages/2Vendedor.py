# streamlit_app/pages/2_🧾_Vendedor.py
import streamlit as st

st.set_page_config(page_title="Panel del Vendedor", layout="centered")

# ---------- Estilos ----------
st.markdown("""
<style>
.stApp { background:#FF8C00; }

.ecom-panel {
  max-width: 520px;
  margin: 24px auto 12px auto;
  background: #ff9b2f;
  border-radius: 14px;
  padding: 22px 22px 18px 22px;
  box-shadow: 0 8px 18px rgba(0,0,0,.25);
}

.logo {
  background:#fff;
  border-radius:16px;
  padding:16px 18px;
  margin: 0 auto 16px auto;
  width: 280px;
  text-align:center;
  box-shadow: 0 4px 12px rgba(0,0,0,.18);
  border: 2px solid #f3f3f3;
}
.logo h1 {
  margin:0;
  font-size:1.4rem;
  color:#153063;
}
.logo small { color:#666; }

/* marca en esquina (H&M simulada) */
.brand {
  font-family: 'Brush Script MT', cursive;
  font-size: 1.8rem;
  font-weight: bold;
  color: #b30000;
  position: absolute;
  left: 10px;
  top: 10px;
}

/* Botones azules */
.stButton > button {
  background:#0b3a83;
  color:#fff;
  border: none;
  border-radius: 8px;
  padding: 12px 16px;
  font-weight: 800;
  width: 100%;
  margin: 8px 0;
  box-shadow: 0 4px 10px rgba(0,0,0,.18);
}
.stButton > button:hover { filter: brightness(1.05); }

/* Botón salir */
.btn-exit > button {
  background:#936037 !important;
}

/* Título centrado */
h2.title { text-align:center; color:#1f2e5e; margin-top: 12px; }
</style>
""", unsafe_allow_html=True)

# ---------- UI ----------
st.markdown('<div class="ecom-panel">', unsafe_allow_html=True)
st.markdown('<div class="brand">H&M</div>', unsafe_allow_html=True)

st.markdown("""
<div class="logo">
  <h1>Ecom MKT Lab</h1>
  <small>Soluciones de Marketing Digital y Comercio Electrónico</small>
</div>
""", unsafe_allow_html=True)

# Botones principales
col = st.container()
col.button("VER PRODUCTOS", key="b_ver_prod")
col.button("EDITAR PRODUCTOS", key="b_edit_prod")
col.button("COMENTARIOS", key="b_coment")
col.button("HISTORIAL DE VENTAS", key="b_hist_ventas")
col.button("FINANCIAS Y RENTABILIDAD", key="b_finanzas")

st.markdown("</div>", unsafe_allow_html=True)

# Botón salir
st.write("")
st.markdown('<div class="btn-exit">', unsafe_allow_html=True)
st.button("SALIR", key="b_exit")
st.markdown('</div>', unsafe_allow_html=True)