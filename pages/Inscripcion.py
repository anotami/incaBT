import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent))
from utils import prepare_page

BASE_DIR = Path(__file__).parent.parent

st.set_page_config(
    page_title="Inscripción — CALLADO BT",
    page_icon="📨",
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

html = prepare_page("inscripcion.html", BASE_DIR)
components.html(html, height=600, scrolling=True)
