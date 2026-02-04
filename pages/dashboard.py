import streamlit as st
import base64
from pathlib import Path

# Import the new tabs
# (Streamlit automatically adds the root folder to path, so we can import 'tabs')
from tabs import home, doctor, analytics, feedback, profile

# --- 1. PAGE CONFIG ---
st.set_page_config(
    page_title="AgriDetect Dashboard",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- 2. ASSETS & CSS ---
BASE_DIR = Path(__file__).parent.parent 
ASSETS_DIR = BASE_DIR / "assets"

def get_base64(path: Path):
    try:
        with open(path, "rb") as f: return base64.b64encode(f.read()).decode()
    except: return ""

bg_image = get_base64(ASSETS_DIR / "plant bg.avif")

st.markdown(f"""
<style>
/* GLOBAL FONTS */
html, body {{ font-family: 'Inter', sans-serif; }}

/* BACKGROUND */
.stApp {{
    background: 
        linear-gradient(135deg, rgba(2,6,23,0.95), rgba(15,23,42,0.92), rgba(6,78,59,0.90)),
        url("data:image/avif;base64,{bg_image}");
    background-size: cover;
    background-attachment: fixed;
    color: white;
}}

/* HIDE DEFAULTS */
#MainMenu, footer, header {{visibility: hidden;}}

/* NAVBAR BUTTONS */
div.stButton > button {{
    background: transparent;
    border: 1px solid rgba(255,255,255,0.2);
    color: #cbd5e1;
    border-radius: 10px;
    height: 3rem;
    width: 100%;
    font-weight: 600;
    transition: all 0.3s;
    white-space: nowrap;
}}
div.stButton > button:hover {{
    background: rgba(52, 211, 153, 0.2);
    border-color: #34d399;
    color: #34d399;
}}
div.stButton > button:focus {{
    background: #34d399;
    color: #020617;
    border-color: #34d399;
}}

/* PRIMARY ACTION BUTTON */
button[kind="primary"] {{
    background: linear-gradient(90deg, #22d3ee, #34d399) !important;
    color: #020617 !important;
    border: none !important;
}}

/* CARDS */
.card {{
    background: rgba(255, 255, 255, 0.1);
    backdrop-filter: blur(20px);
    padding: 30px;
    border-radius: 20px;
    border: 1px solid rgba(255,255,255,0.1);
    margin-bottom: 20px;
}}
/* INPUT FIELDS */
.stTextInput input, .stTextArea textarea {{
    background-color: rgba(0, 0, 0, 0.3) !important;
    color: white !important;
    border: 1px solid rgba(255, 255, 255, 0.2) !important;
    border-radius: 12px;
}}
</style>
""", unsafe_allow_html=True)

# --- 3. SESSION STATE ---
if 'active_tab' not in st.session_state: st.session_state.active_tab = 'Home'
if 'username' not in st.session_state: st.session_state.username = "Farmer"

# --- 4. TOP NAVBAR ---
st.markdown("<br>", unsafe_allow_html=True)
c1, c2, c3, c4, c5, c6 = st.columns(6)

with c1:
    if st.button("🏠 Home", use_container_width=True): st.session_state.active_tab = 'Home'
with c2:
    if st.button("🩺 Doctor", use_container_width=True): st.session_state.active_tab = 'Doctor'
with c3:
    if st.button("📊 Analytics", use_container_width=True): st.session_state.active_tab = 'Analytics'
with c4:
    if st.button("💬 Feedback", use_container_width=True): st.session_state.active_tab = 'Feedback'
with c5:
    if st.button("👤 Profile", use_container_width=True): st.session_state.active_tab = 'Profile'
with c6:
    if st.button("🚪 Logout", use_container_width=True):
        st.session_state.logged_in = False
        st.switch_page("main.py")

st.markdown("---")

# --- 5. PAGE ROUTING ---
# This looks at the button you clicked and loads the correct file from 'tabs/' folder
tab = st.session_state.active_tab

if tab == 'Home':
    home.show(st.session_state.username)
elif tab == 'Doctor':
    doctor.show()
elif tab == 'Analytics':
    analytics.show()
elif tab == 'Feedback':
    feedback.show()
elif tab == 'Profile':
    profile.show(st.session_state.username)
