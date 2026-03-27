"""
app.py — Streamlit entrypoint.
Routing por query param ?p=index|taller|inscripcion
La navegación desde el iframe usa window.top.location.href = '/?p=xxx'
que navega el tab entero (confiable, sin dependencias de same-origin).
"""
import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path
from utils import prepare_page

BASE_DIR = Path(__file__).parent

st.set_page_config(
    page_title="CALLADO BT",
    page_icon="📡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
header, #MainMenu, footer { display: none !important; }
body { overflow: hidden !important; margin: 0 !important; }
.block-container, [data-testid="stMainBlockContainer"] {
    padding: 0 !important; margin: 0 !important; max-width: 100% !important;
}
</style>
""", unsafe_allow_html=True)

PAGE_MAP = {
    "index":       "index.html",
    "taller":      "taller.html",
    "inscripcion": "inscripcion.html",
}

page_key = st.query_params.get("p", "index")
if page_key not in PAGE_MAP:
    page_key = "index"

html = prepare_page(PAGE_MAP[page_key], BASE_DIR)
components.html(html, height=600, scrolling=True)
