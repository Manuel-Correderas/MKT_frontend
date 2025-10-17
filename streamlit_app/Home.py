# streamlit_app/Home.py
import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(page_title="Ecom MKT Lab - Home", page_icon="🛒", layout="wide")

# =========================
# ESTILOS — LIMPIO, SIN RECTÁNGULOS
# =========================
st.markdown("""
<style>
:root { --primary:#0b3a91; }

body, .stApp { background:#ffffff; }

.topbar {
  display:flex; flex-wrap:wrap; align-items:center;
  gap:10px; margin:8px 0 16px;
}
.brand { font-weight:900; color:var(--primary); font-size:1.2rem; }

/* Buscador */
div[data-baseweb="input"] input {
  border-radius:10px; height:40px; border:2px solid var(--primary) !important;
}

/* Botones/chips */
.stButton > button {
  background:#fff !important; color:var(--primary) !important;
  border:2px solid var(--primary) !important; border-radius:999px !important;
  padding:6px 12px !important; font-weight:800 !important;
  box-shadow:none !important; white-space:nowrap !important;
}

/* Tarjetas sin fondo ni borde (la imagen queda adentro) */
.card {
  background:transparent; border:none; box-shadow:none; border-radius:0;
  padding:0; margin-bottom:10px; display:flex; flex-direction:column; align-items:center;
}
.card-img {
  width:100%; height:260px; object-fit:contain; background:transparent; display:block;
}

/* Texto */
.name { font-weight:900; color:var(--primary); margin:8px 0 4px; text-align:center; font-size:1rem; }
.price { color:#111; text-align:center; font-weight:800; font-size:1.05rem; margin:2px 0 6px; }
.meta { color:#444; text-align:center; font-size:.9rem; margin:0 0 8px; }

/* CTA debajo de la tarjeta */
.cta { display:flex; justify-content:center; }
</style>
""", unsafe_allow_html=True)

# =========================
# CARGA DE DATOS
# =========================
def csv_path():
    for p in [
        Path(__file__).resolve().parents[1] / "data" / "products.csv",
        Path.cwd() / "data" / "products.csv",
        Path(__file__).resolve().parent / "data" / "products.csv",
    ]:
        if p.exists(): return p
    return None

@st.cache_data(ttl=60)
def load_products():
    p = csv_path()
    if p:
        df = pd.read_csv(p, encoding="utf-8-sig").fillna("")
        for c in ["name","description","category","subcategory","image_url"]:
            if c in df.columns: df[c] = df[c].astype(str)
        return df
    # Demo
    return pd.DataFrame([
        {"id":1,"name":"Remera Básica Negra","price":9999,"category":"Indumentaria","subcategory":"Remeras",
         "image_url":"https://i.imgur.com/pTgqgQw.png","description":"Remera algodón peinado color negro"},
        {"id":2,"name":"Jean Slim Azul","price":25999,"category":"Indumentaria","subcategory":"Pantalones",
         "image_url":"https://i.imgur.com/8m7Zy0Z.png","description":"Jean slim fit azul clásico"},
        {"id":3,"name":"Zapatillas Urbanas","price":45999,"category":"Calzado","subcategory":"Urbano",
         "image_url":"https://i.imgur.com/5z9m3FJ.png","description":"Suela antideslizante"},
        {"id":4,"name":"Auriculares In-Ear","price":14999,"category":"Electrónicos","subcategory":"Audio",
         "image_url":"https://i.imgur.com/yX0sVwA.png","description":"Aislamiento de ruido"},
        {"id":5,"name":"Taladro Percutor 500W","price":79999,"category":"Herramientas","subcategory":"Taladros",
         "image_url":"https://i.imgur.com/fm0wZrL.png","description":"Uso profesional"}
    ])

def money(v):
    try: return f"$ {int(float(v)):,}".replace(",", ".")
    except: return "$ --"

# =========================
# TOPBAR (incluye CARRITO)
# =========================
st.markdown('<div class="topbar">', unsafe_allow_html=True)
c1, c2, c3 = st.columns([2,4,1])
with c1:
    st.markdown('<div class="brand">🛍️ Ecom MKT Lab</div>', unsafe_allow_html=True)
with c2:
    q = st.text_input("Buscar productos…", label_visibility="collapsed", key="q")
with c3:
    if st.button("🛒 Carrito"):
        st.switch_page("pages/4_🛒_Mi_Carrito.py")
st.markdown('</div>', unsafe_allow_html=True)

# =========================
# LISTADO + FILTROS
# =========================
df = load_products().copy()

if q:
    ql = q.lower()
    df = df[df["name"].str.lower().str.contains(ql) | df["description"].str.lower().str.contains(ql)]

cats = ["Todos"] + sorted(df["category"].dropna().unique().tolist())
subs = ["Todas"] + sorted(df["subcategory"].dropna().unique().tolist())

sel_cat = st.session_state.get("sel_cat", "Todos")
sel_sub = st.session_state.get("sel_sub", "Todas")

st.caption("Categorías")
cat_cols = st.columns(len(cats))
for i, c in enumerate(cats):
    with cat_cols[i]:
        if st.button(c, key=f"cat_{c}"):
            sel_cat = c
            st.session_state["sel_cat"] = c

st.caption("Subcategorías")
sub_cols = st.columns(len(subs))
for i, s in enumerate(subs):
    with sub_cols[i]:
        if st.button(s, key=f"sub_{s}"):
            sel_sub = s
            st.session_state["sel_sub"] = s

# Aplicar filtros
view = df.copy()
if sel_cat != "Todos":
    view = view[view["category"] == sel_cat]
if sel_sub != "Todas":
    view = view[view["subcategory"] == sel_sub]

# =========================
# GRID DE PRODUCTOS (con VER DETALLE)
# =========================
st.markdown("## Productos Disponibles")
cols = st.columns(3)

if view.empty:
    st.info("No se encontraron productos.")
else:
    for i, row in view.reset_index(drop=True).iterrows():
        with cols[i % 3]:
            img = str(row.get("image_url","")).strip()
            if not (img and img.startswith("http")):
                img = "https://via.placeholder.com/800x600.png?text=Sin+Imagen"

            # Tarjeta y contenido visual
            html = f"""
            <div class="card">
              <img class="card-img" src="{img}" alt="{row.get('name','Producto')}">
              <div class="name">{row.get('name','Producto')}</div>
              <div class="price">{money(row.get('price',''))}</div>
              <div class="meta">{row.get('description','')}</div>
            </div>
            """
            st.markdown(html, unsafe_allow_html=True)

            # CTA VER DETALLE (fuera del HTML para que sea interactivo)
            with st.container():
                cta = st.columns([1,1,1])
                with cta[1]:
                    if st.button("🔎 Ver detalle", key=f"det_{row.get('id', i)}"):
                        st.session_state["last_product"] = int(row.get("id", i))
                        st.switch_page("pages/3_🧥_Producto.py")
