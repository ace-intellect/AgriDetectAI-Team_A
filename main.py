import streamlit as st
import base64
from pathlib import Path
import time
import database as db
import auth  # <--- Uses your Modern Auth file

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(page_title="AgriDetect AI", page_icon="🌿", layout="wide")

# --- INITIALIZE DB ---
db.create_tables()

# --- 2. SESSION STATE SETUP ---
if 'logged_in' not in st.session_state: st.session_state.logged_in = False
if 'page' not in st.session_state: st.session_state.page = 'landing'
if 'username' not in st.session_state: st.session_state.username = 'Guest'

# --- NAVIGATION HELPER ---
def navigate_to(page):
    st.session_state.page = page
    st.rerun()

# --- 3. ASSETS LOADING ---
BASE_DIR = Path(__file__).parent
ASSETS_DIR = BASE_DIR / "assets"

def get_base64(path: Path):
    try:
        with open(path, "rb") as f: return base64.b64encode(f.read()).decode()
    except FileNotFoundError: return ""

# Load Background
bg_image_base64 = get_base64(ASSETS_DIR / "plant bg.avif")

# Load Flow Images
flow_images = {
    "login.png": get_base64(ASSETS_DIR / "login.png"),
    "upload.png": get_base64(ASSETS_DIR / "upload.png"),
    "ai.png": get_base64(ASSETS_DIR / "ai.png"),
    "disease.png": get_base64(ASSETS_DIR / "disease.png"),
    "insights.png": get_base64(ASSETS_DIR / "insights.png")
}

# --- 4. GLOBAL CSS ---
st.markdown(f"""
<style>
/* GLOBAL FONTS */
html, body {{ font-family: 'Inter', sans-serif; }}

/* APP BACKGROUND */
.stApp {{
    background: 
        linear-gradient(135deg, rgba(2,6,23,0.95), rgba(15,23,42,0.92), rgba(6,78,59,0.90)),
        url("data:image/avif;base64,{bg_image_base64}");
    background-size: cover;
    background-attachment: fixed;
    color: white;
}}

/* HIDE DEFAULTS */
#MainMenu, footer, header {{ visibility: hidden; }}

/* === ANIMATIONS (Defined at top) === */
@keyframes fadeUp {{
    0% {{ opacity: 0; transform: translateY(50px); }} 
    100% {{ opacity: 1; transform: translateY(0); }}
}}

/* === HERO SECTION === */
.hero-text {{ text-align: center; padding-top: 8vh; animation: fadeUp 1s ease-out; margin-bottom: 30px; }}
.hero-text h1 {{ font-size: 4.6rem; font-weight: 900; line-height: 1.1; margin-bottom: 20px; color: white; }}
.hero-text span {{ background: linear-gradient(90deg, #22d3ee, #34d399); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }}
.hero-text p {{ font-size: 1.5rem; max-width: 820px; color: #d1fae5; margin: 0 auto; }}

/* === BUTTON STYLES === */
div.stButton > button {{
    border-radius: 999px;
    font-weight: 800;
    padding: 0.5rem 2rem;
    height: 3.5rem;
    width: 100%;
    font-size: 1.1rem;
    transition: all 0.3s ease;
    /* FORCE ANIMATION ON ALL BUTTONS */
    animation: fadeUp 1.2s cubic-bezier(0.175, 0.885, 0.32, 1.275) both;
}}

/* Primary (Login) */
button[kind="primary"] {{ background: linear-gradient(90deg, #22d3ee, #34d399); color: #020617; border: none; }}
button[kind="primary"]:hover {{ transform: translateY(-5px); box-shadow: 0 10px 20px rgba(52, 211, 153, 0.4); color: black; }}

/* Secondary (Register) */
button[kind="secondary"] {{ background: transparent; border: 2px solid #34d399; color: #ecfeff; }}
button[kind="secondary"]:hover {{ background: rgba(52, 211, 153, 0.1); border-color: #22d3ee; color: #22d3ee; transform: translateY(-5px); }}

/* === CARDS === */
.section {{ padding: 5rem 6rem; animation: fadeUp 1.2s ease-in-out; }}
.grid {{ display: grid; grid-template-columns: repeat(3, minmax(280px, 1fr)); gap: 35px; }}
.card {{ background: rgba(255, 255, 255, 0.15); backdrop-filter: blur(22px); padding: 38px 34px; border-radius: 26px; box-shadow: 0 20px 60px rgba(0,0,0,0.45); text-align: center; transition: all 0.4s ease; }}
.card:hover {{ transform: translateY(-12px) scale(1.02); background: rgba(255, 255, 255, 0.25); }}
.card h3 {{ font-size: 1.35rem; font-weight: 700; margin-bottom: 14px; color: white; }}
.card p {{ font-size: 1rem; line-height: 1.55; color: #d1fae5; }}

/* === FLOW STEPS === */
.flow {{ display: flex; justify-content: space-between; gap: 22px; margin-top: 30px; }}
.flow div {{ flex: 1; text-align: center; padding: 24px 16px; background: rgba(255,255,255,0.18); border-radius: 20px; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 15px; min-height: 140px; transition: all 0.3s ease; }}
.flow div:hover {{ background: rgba(255, 255, 255, 0.25); transform: translateY(-5px); }}
.flow img {{ width: 64px; height: 64px; border-radius: 12px; object-fit: cover; display: block; }}
.flow-step-title {{ font-size: 1.1rem; font-weight: 700; color: #ecfeff; }}

.footer {{ text-align: center; padding: 35px; color: #99f6e4; opacity: 0.8; }}
</style>
""", unsafe_allow_html=True)

# --- 5. LANDING PAGE ---
def show_landing():
    # HERO TEXT
    st.markdown("""
    <div class="hero-text">
        <h1>AgriDetect<span>AI</span></h1>
        <p>An intelligent crop-health platform that detects plant diseases early, explains risks clearly, and helps farmers protect yield using AI.</p>
    </div>
    """, unsafe_allow_html=True)

    # --- CENTERED BUTTONS ---
    # We use 4 columns: [Space, Button1, Button2, Space]
    # Ratios: 2 parts space, 1 part button, 1 part button, 2 parts space
    # This forces the buttons to squeeze into the center
    _, col_btn1, col_btn2, _ = st.columns([2, 1, 1, 2])
    
    with col_btn1:
        if st.button("Login", type="primary"): 
            navigate_to('login')
            
    with col_btn2:
        if st.button("Register", type="secondary"): 
            navigate_to('signup')

    # WHY SECTION
    st.markdown("""
    <div class="section">
        <h2 style="text-align:center; font-size: 2.8rem; font-weight: 800; margin-bottom: 45px;">Why AgriDetectAI?</h2>
        <div class="grid">
            <div class="card"><h3>🌾 Unified Crop Intelligence</h3><p>Detect diseases across multiple plants using a single pipeline.</p></div>
            <div class="card"><h3>🧠 Deep Learning Accuracy</h3><p>Built on fine-tuned ResNet architectures for research-grade predictions.</p></div>
            <div class="card"><h3>🔍 Explainable AI</h3><p>Visual indicators and confidence scores help users understand risks.</p></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # FLOW SECTION
    st.markdown(f"""
    <div class="section">
        <h2 style="text-align:center; font-size: 2.8rem; font-weight: 800; margin-bottom: 45px;">How It Works</h2>
        <div class="flow">
            <div><img src="data:image/png;base64,{flow_images.get('login.png', '')}"><div class="flow-step-title">Login</div></div>
            <div><img src="data:image/png;base64,{flow_images.get('upload.png', '')}"><div class="flow-step-title">Upload</div></div>
            <div><img src="data:image/png;base64,{flow_images.get('ai.png', '')}"><div class="flow-step-title">AI Processing</div></div>
            <div><img src="data:image/png;base64,{flow_images.get('disease.png', '')}"><div class="flow-step-title">Detection</div></div>
            <div><img src="data:image/png;base64,{flow_images.get('insights.png', '')}"><div class="flow-step-title">Insights</div></div>
        </div>
    </div>
    <div class="footer">© 2026 AgriDetectAI · AI for Smarter Agriculture 🌱</div>
    """, unsafe_allow_html=True)

# --- 6. DASHBOARD ---
def show_dashboard():
    # --- 1. IMPORT TABS ---
    from tabs import home, doctor, analytics, feedback, profile

    # --- 2. NAVBAR CSS (Strictly Scoped) ---
    st.markdown("""
    <style>
    /* =========================================
       1. NAVBAR STYLING (Applies ONLY to the 1st Radio Button)
       ========================================= */
    div[data-testid="stRadio"]:first-of-type > div {
        display: flex;
        flex-direction: row;
        justify-content: center;
        align-items: center;
        background-color: rgba(255, 255, 255, 0.1);
        padding: 8px;
        border-radius: 50px;
        border: 1px solid rgba(255, 255, 255, 0.15);
        width: fit-content;
        margin: 0 auto;
        gap: 10px;
    }

    div[data-testid="stRadio"]:first-of-type label {
        background-color: transparent;
        color: #e2e8f0;
        padding: 8px 24px;
        border-radius: 30px;
        border: none;
        transition: all 0.3s ease;
        font-weight: 600;
        cursor: pointer;
        margin: 0;
    }

    div[data-testid="stRadio"]:first-of-type label:hover {
        background-color: rgba(52, 211, 153, 0.1);
        color: #34d399;
    }

    div[data-testid="stRadio"]:first-of-type label[data-baseweb="radio"] {
        background: linear-gradient(90deg, #34d399, #10b981) !important;
        color: black !important;
        box-shadow: 0 4px 10px rgba(52, 211, 153, 0.3);
    }

    div[data-testid="stRadio"]:first-of-type div[role="radio"] {
        display: none; /* Hide circle icon for Navbar */
    }

    /* =========================================
       2. RESET FOR ALL OTHER RADIO BUTTONS (Feedback Page, etc.)
       This forces normal styling for every radio button except the first one.
       ========================================= */
    div[data-testid="stRadio"]:not(:first-of-type) > div {
        background-color: transparent !important;
        border: none !important;
        padding: 0 !important;
        display: flex;
        flex-direction: row; /* Keep them horizontal if requested */
        gap: 15px;
        border-radius: 0 !important;
    }

    div[data-testid="stRadio"]:not(:first-of-type) label {
        background: transparent !important;
        color: white !important;
        padding: 0 !important;
        border-radius: 0 !important;
        box-shadow: none !important;
        font-weight: normal !important;
    }
    
    /* Restore the circle icon for normal radio buttons */
    div[data-testid="stRadio"]:not(:first-of-type) div[role="radio"] {
        display: flex !important; 
    }
    </style>
    """, unsafe_allow_html=True)

    # --- 3. TOP NAVIGATION LAYOUT ---
    top_c1, top_c2, top_c3 = st.columns([2, 6, 2])

    with top_c1:
        st.markdown("<h3 style='margin:0; padding-top:10px;'>🌿 AgriDetect</h3>", unsafe_allow_html=True)

    with top_c2:
        # The Navigation Bar (This is :first-of-type)
        selected_tab = st.radio(
            "Main Navigation",
            ["Home", "AI Doctor", "Analytics", "Feedback", "Profile"],
            horizontal=True,
            label_visibility="collapsed",
            key="nav_bar"
        )

    with top_c3:
        _, col_logout = st.columns([1, 2])
        with col_logout:
            if st.button("🚪 Logout", type="secondary"):
                st.session_state.logged_in = False
                st.session_state.page = 'landing'
                st.rerun()

    st.markdown("---")

    # --- 4. PAGE ROUTING ---
    if selected_tab == "Home":
        home.show(st.session_state.username)
    elif selected_tab == "AI Doctor":
        doctor.show()
    elif selected_tab == "Analytics":
        analytics.show()
    elif selected_tab == "Feedback":
        feedback.show()
    elif selected_tab == "Profile":
        profile.show(st.session_state.username)

# --- 7. MAIN ROUTER ---
if st.session_state.logged_in:
    show_dashboard()
else:
    if st.session_state.page == 'landing': show_landing()
    elif st.session_state.page == 'login': auth.show_login()   # Modern UI
    elif st.session_state.page == 'signup': auth.show_signup() # Modern UI
    else: show_landing()