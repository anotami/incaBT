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

# Mínimo CSS: evita flash de contenido Streamlit antes de que corra el script
st.markdown("""
<style>
header, #MainMenu, footer { display: none !important; }
body { overflow: hidden !important; margin: 0 !important; }
.block-container, [data-testid="stMainBlockContainer"] {
    padding: 0 !important; margin: 0 !important; max-width: 100% !important;
}
</style>
""", unsafe_allow_html=True)

html = prepare_page("index.html", BASE_DIR)
# scrolling=True para que el iframe maneje su propio scroll interno
components.html(html, height=600, scrolling=True)
