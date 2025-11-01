import streamlit as st

st.set_page_config(page_title="Planes Premium", layout="centered")
st.title("💎 Planes Premium")

c1,c2 = st.columns(2)
with c1:
    st.header("Vendedor")
    st.write("""
- +20% visibilidad en Home
- Hasta 200 productos (vs 20)
- Reportes avanzados, exportaciones
- Soporte prioritario
    """)
    if st.button("Elegir Vendedor Premium", key="pv", type="primary"):
        st.session_state["premium_intent"] = {"role":"VENDEDOR","plan":"mensual"}
        st.switch_page("pages/10_💳_Checkout.py")

with c2:
    st.header("Comprador")
    st.write("""
- Cupones exclusivos
- Prioridad en soporte
- Historial extendido y alertas de precio
    """)
    if st.button("Elegir Comprador Premium", key="pc", type="primary"):
        st.session_state["premium_intent"] = {"role":"COMPRADOR","plan":"mensual"}
        st.switch_page("pages/10_💳_Checkout.py")
