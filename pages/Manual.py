import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent))
from utils import prepare_page

BASE_DIR = Path(__file__).parent.parent

st.set_page_config(
    page_title="Manual — CALLADO BT",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
    #MainMenu, footer, header { visibility: hidden; height: 0; }
    .block-container { padding: 0 !important; max-width: 100% !important; }
    [data-testid="stSidebar"],
    [data-testid="collapsedControl"] { display: none !important; }
    iframe { width: 100% !important; border: none !important; display: block !important; }
    </style>
    """,
    unsafe_allow_html=True,
)

html = prepare_page("manual.html", BASE_DIR)
components.html(html, height=9000, scrolling=False)
