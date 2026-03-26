import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent))
from utils import prepare_page

BASE_DIR = Path(__file__).parent.parent

st.set_page_config(
    page_title="Taller Virtual — CALLADO BT",
    page_icon="🔧",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
    header, #MainMenu, footer { display: none !important; height: 0 !important; }
    section[data-testid="stMain"]           { padding: 0 !important; }
    div[data-testid="stMainBlockContainer"] { padding: 0 !important; max-width: 100% !important; }
    div[data-testid="stVerticalBlock"]      { gap: 0 !important; }
    .block-container { padding: 0 !important; max-width: 100% !important; }
    section.main     { padding: 0 !important; }
    .stApp           { margin-top: 0 !important; }
    [data-testid="stSidebar"],
    [data-testid="collapsedControl"] { display: none !important; }
    iframe { width: 100% !important; border: none !important;
             display: block !important; margin: 0 !important; vertical-align: top !important; }
    </style>
    """,
    unsafe_allow_html=True,
)

html = prepare_page("taller.html", BASE_DIR)
components.html(html, height=8000, scrolling=False)
