import streamlit as st
import base64
from pathlib import Path
import time

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(
    page_title="AgriDetectAI",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- 2. SESSION STATE & NAVIGATION ---
if 'page' not in st.session_state: st.session_state.page = 'landing'
if 'logged_in' not in st.session_state: st.session_state.logged_in = False
if 'username' not in st.session_state: st.session_state.username = 'Guest'

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

bg_image_base64 = get_base64(ASSETS_DIR / "plant bg.avif")

flow_images = {
    "login.png": get_base64(ASSETS_DIR / "login.png"),
    "upload.png": get_base64(ASSETS_DIR / "upload.png"),
    "ai.png": get_base64(ASSETS_DIR / "ai.png"),
    "disease.png": get_base64(ASSETS_DIR / "disease.png"),
    "insights.png": get_base64(ASSETS_DIR / "insights.png")
}

# --- 4. CSS STYLING (FRIEND'S UI + FUNCTIONAL BUTTONS) ---
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

/* === ANIMATIONS === */
@keyframes fadeUp {{
    from {{ opacity: 0; transform: translateY(40px); }} 
    to {{ opacity: 1; transform: translateY(0); }}
}}

/* === HERO SECTION STYLES === */
.hero-text {{
    text-align: center;
    padding-top: 8vh;
    animation: fadeUp 1.3s ease-in-out;
    margin-bottom: 30px;
}}
.hero-text h1 {{
    font-size: 4.6rem; font-weight: 900; line-height: 1.1; margin-bottom: 20px; color: white;
}}
.hero-text span {{
    background: linear-gradient(90deg, #22d3ee, #34d399);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
}}
.hero-text p {{
    font-size: 1.5rem; max-width: 820px; color: #d1fae5; margin: 0 auto;
}}

/* === CUSTOMIZING STREAMLIT BUTTONS TO MATCH UI === */
div.stButton > button {{
    border-radius: 999px;
    font-weight: 800;
    padding: 0.5rem 2rem;
    height: 3.5rem;
    width: 100%;
    font-size: 1.1rem;
    transition: all 0.3s ease;
    animation: fadeUp 1.5s ease-in-out; /* Keeps the animation */
}}

/* PRIMARY BUTTON (Login) - Maps to your 'btn-primary' */
button[kind="primary"] {{
    background: linear-gradient(90deg, #22d3ee, #34d399);
    color: #020617;
    border: none;
}}
button[kind="primary"]:hover {{
    transform: translateY(-3px);
    box-shadow: 0 10px 20px rgba(52, 211, 153, 0.4);
    color: black;
}}

/* SECONDARY BUTTON (Register) - Maps to your 'btn-secondary' */
button[kind="secondary"] {{
    background: transparent;
    border: 2px solid #34d399;
    color: #ecfeff;
}}
button[kind="secondary"]:hover {{
    background: rgba(52, 211, 153, 0.1);
    border-color: #22d3ee;
    color: #22d3ee;
    transform: translateY(-3px);
}}

/* === CARDS (Why Section) === */
.section {{ padding: 5rem 6rem; animation: fadeUp 1.2s ease-in-out; }}
.grid {{ display: grid; grid-template-columns: repeat(3, minmax(280px, 1fr)); gap: 35px; }}
.card {{
    background: rgba(255, 255, 255, 0.15); backdrop-filter: blur(22px);
    padding: 38px 34px; border-radius: 26px;
    box-shadow: 0 20px 60px rgba(0,0,0,0.45);
    text-align: center; transition: all 0.4s ease;
}}
.card:hover {{ transform: translateY(-12px) scale(1.02); background: rgba(255, 255, 255, 0.25); }}
.card h3 {{ font-size: 1.35rem; font-weight: 700; margin-bottom: 14px; color: white; }}
.card p {{ font-size: 1rem; line-height: 1.55; color: #d1fae5; }}

/* === FLOW STEPS === */
.flow {{ display: flex; justify-content: space-between; gap: 22px; margin-top: 30px; }}
.flow div {{
    flex: 1; text-align: center; padding: 24px 16px;
    background: rgba(255,255,255,0.18); border-radius: 20px;
    display: flex; flex-direction: column; align-items: center; justify-content: center;
    gap: 15px; min-height: 140px; transition: all 0.3s ease;
}}
.flow div:hover {{ background: rgba(255, 255, 255, 0.25); transform: translateY(-5px); }}
.flow img {{ width: 64px; height: 64px; border-radius: 12px; object-fit: cover; display: block; }}
.flow-step-title {{ font-size: 1.1rem; font-weight: 700; color: #ecfeff; }}

/* === INPUT FIELDS (Glass Style for Login) === */
.stTextInput input {{
    background-color: rgba(0, 0, 0, 0.3) !important;
    color: white !important;
    border: 1px solid rgba(255, 255, 255, 0.2) !important;
    border-radius: 12px;
    padding: 15px;
}}
/* FOOTER */
.footer {{ text-align: center; padding: 35px; color: #99f6e4; opacity: 0.8; }}
</style>
""", unsafe_allow_html=True)

# --- 5. LANDING PAGE ---
def show_landing():
    # HERO TEXT (HTML)
    st.markdown("""
    <div class="hero-text">
        <h1>AgriDetect<span>AI</span></h1>
        <p>
            An intelligent crop-health platform that detects plant diseases early, 
            explains risks clearly, and helps farmers protect yield using AI.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # HERO BUTTONS (Functional Streamlit Buttons)
    # We use columns to center them and apply the mapped styles
    col1, col2, col3, col4 = st.columns([1, 0.6, 0.6, 1])
    
    with col2:
        # Type="primary" triggers our Gradient CSS
        if st.button("Login", type="primary"):
            navigate_to('login')
            
    with col3:
        # Type="secondary" triggers our Outline/Border CSS
        if st.button("Register", type="secondary"):
            navigate_to('signup')

    # WHY SECTION (Cards)
    st.markdown("""
    <div class="section">
        <h2 style="text-align:center; font-size: 2.8rem; font-weight: 800; margin-bottom: 45px;">Why AgriDetectAI?</h2>
        <div class="grid">
            <div class="card">
                <h3>🌾 Unified Crop Intelligence</h3>
                <p>Farmers don't need separate tools. Our unified model detects diseases across multiple plants using a single pipeline.</p>
            </div>
            <div class="card">
                <h3>🧠 Deep Learning Accuracy</h3>
                <p>Built on fine-tuned ResNet architectures trained on real agricultural datasets for research-grade predictions.</p>
            </div>
            <div class="card">
                <h3>🔍 Explainable AI</h3>
                <p>Visual indicators and confidence scores help users understand *why* a disease was detected.</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # HOW IT WORKS (Flow)
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

# --- 6. LOGIN PAGE ---
def show_login():
    st.markdown("<br><br>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns([1, 1.2, 1])
    with c2:
        # We reuse the .card style for the form container to keep consistency
        st.markdown("""
        <div class="card" style="animation: fadeUp 0.8s ease-in-out;">
            <h2 style='color: white; margin-bottom: 10px;'>Welcome Back</h2>
            <p style='color: #d1fae5; margin-bottom: 20px;'>Please enter your credentials.</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Functional Inputs
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        
        st.write("")
        # Use Primary (Gradient) button for action
        if st.button("Sign In"):
            if username == "admin" and password == "admin":
                st.session_state.logged_in = True
                st.session_state.username = username
                st.success("Success!")
                time.sleep(0.5)
                # THIS IS THE KEY LINE:
                st.switch_page("pages/dashboard.py") 
            else:
                st.error("Invalid Credentials")

# --- 7. SIGNUP PAGE ---
def show_signup():
    st.markdown("<br><br>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns([1, 1.2, 1])
    with c2:
        st.markdown("""
        <div class="card" style="animation: fadeUp 0.8s ease-in-out;">
            <h2 style='color: white;'>Create Account</h2>
            <p style='color: #d1fae5;'>Join the future of farming.</p>
        </div>
        """, unsafe_allow_html=True)
        
        col_a, col_b = st.columns(2)
        with col_a: st.text_input("First Name")
        with col_b: st.text_input("Last Name")
        
        st.text_input("Email Address")
        st.text_input("Choose Password", type="password")
        
        st.write("")
        if st.button("Create Account", type="primary"):
            st.success("Account created successfully! Please Login.")
            time.sleep(1.5)
            navigate_to('login')
            
        if st.button("⬅ Back to Home", type="secondary"):
            navigate_to('landing')

# --- 8. PAGE ROUTER ---
if st.session_state.page == 'landing':
    show_landing()
elif st.session_state.page == 'login':
    show_login()
elif st.session_state.page == 'signup':
    show_signup()