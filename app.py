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

# Ocultar chrome de Streamlit y hacer el iframe full-width
st.markdown(
    """
    <style>
    #MainMenu, footer, header { visibility: hidden; height: 0; }
    .block-container {
        padding: 0 !important;
        max-width: 100% !important;
    }
    [data-testid="stSidebar"],
    [data-testid="collapsedControl"] { display: none !important; }
    iframe {
        width: 100% !important;
        border: none !important;
        display: block !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

html = prepare_page("index.html", BASE_DIR)
components.html(html, height=8000, scrolling=False)
