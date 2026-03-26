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
    #MainMenu, footer, header { display: none !important; }
    .stApp, .stApp > div, section.main, section.main > div,
    .block-container,
    [data-testid="stAppViewContainer"],
    [data-testid="stAppViewContainer"] > section,
    [data-testid="stVerticalBlock"],
    [data-testid="stVerticalBlockBorderWrapper"] {
        padding: 0 !important; margin: 0 !important; max-width: 100% !important;
    }
    [data-testid="stSidebar"],
    [data-testid="collapsedControl"] { display: none !important; }
    iframe { width: 100% !important; border: none !important;
             display: block !important; margin: 0 !important; vertical-align: top !important; }
    </style>
    """,
    unsafe_allow_html=True,
)

html = prepare_page("manual.html", BASE_DIR)
components.html(html, height=9000, scrolling=False)
