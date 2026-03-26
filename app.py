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

# Elimina TODO el padding/margin de Streamlit y hace el iframe flush al tope
st.markdown(
    """
    <style>
    /* Ocultar chrome */
    #MainMenu, footer, header { display: none !important; }

    /* Quitar padding de TODOS los contenedores de Streamlit */
    .stApp,
    .stApp > div,
    section.main,
    section.main > div,
    .block-container,
    [data-testid="stAppViewContainer"],
    [data-testid="stAppViewContainer"] > section,
    [data-testid="stVerticalBlock"],
    [data-testid="stVerticalBlockBorderWrapper"] {
        padding: 0 !important;
        margin: 0 !important;
        max-width: 100% !important;
    }

    /* Sidebar oculto */
    [data-testid="stSidebar"],
    [data-testid="collapsedControl"] { display: none !important; }

    /* iframe sin bordes ni desplazamiento propio */
    iframe {
        width: 100% !important;
        border: none !important;
        display: block !important;
        margin: 0 !important;
        padding: 0 !important;
        vertical-align: top !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

html = prepare_page("index.html", BASE_DIR)
components.html(html, height=8000, scrolling=False)
