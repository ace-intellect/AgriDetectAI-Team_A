import streamlit as st
import base64
from pathlib import Path

# PAGE CONFIG
st.set_page_config(
    page_title="AgriDetectAI",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# PATH + BG IMAGE
BASE_DIR = Path(__file__).parent
BG_IMAGE_PATH = BASE_DIR / "assets" / "plant bg.avif"

def get_base64(path: Path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

try:
    bg_image_base64 = get_base64(BG_IMAGE_PATH)
except FileNotFoundError:
    bg_image_base64 = ""

# LOAD FLOW IMAGES
flow_images = {
    "login.png": BASE_DIR / "assets" / "login.png",
    "upload.png": BASE_DIR / "assets" / "upload.png", 
    "ai.png": BASE_DIR / "assets" / "ai.png",
    "disease.png": BASE_DIR / "assets" / "disease.png",
    "insights.png": BASE_DIR / "assets" / "insights.png"
}

flow_base64 = {}
for filename, filepath in flow_images.items():
    try:
        flow_base64[filename] = get_base64(filepath)
    except FileNotFoundError:
        # If image not found, this prevents the code from crashing, 
        # but the icon will look broken on UI.
        flow_base64[filename] = ""

# CSS
st.markdown(f"""
<style>

/* GLOBAL */
html, body {{
    font-family: 'Inter', sans-serif;
}}

/* APP BACKGROUND WITH IMAGE */
.stApp {{
    background: 
        linear-gradient(135deg, 
            rgba(2,6,23,0.95), 
            rgba(15,23,42,0.92), 
            rgba(6,78,59,0.90)
        ),
        url("data:image/avif;base64,{bg_image_base64}");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
    color: white;
}}

/* HERO */
.hero {{
    min-height: 90vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    padding: 0 3rem;
    animation: fadeUp 1.3s ease-in-out;
}}

.hero h1 {{
    font-size: 4.6rem;
    font-weight: 900;
    line-height: 1.1;
    margin-bottom: 20px;
}}

.hero span {{
    background: linear-gradient(90deg, #22d3ee, #34d399);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}}

.hero p {{
    font-size: 1.5rem;
    max-width: 820px;
    color: #d1fae5;
}}

/* BUTTONS */
.btn-primary {{
    background: linear-gradient(90deg, #22d3ee, #34d399);
    color: #020617;
    padding: 16px 44px;
    border-radius: 999px;
    font-weight: 800;
    margin: 35px 15px 0 0;
    display: inline-block;
}}

.btn-secondary {{
    border: 2px solid #34d399;
    color: #ecfeff;
    padding: 16px 44px;
    border-radius: 999px;
    font-weight: 800;
    display: inline-block;
}}

/* SECTION */
.section {{
    padding: 5rem 6rem;
    animation: fadeUp 1.2s ease-in-out;
}}

.section h2 {{
    font-size: 2.8rem;
    font-weight: 800;
    margin-bottom: 45px;
    text-align: center;
}}

/* GRID */
.grid {{
    display: grid;
    grid-template-columns: repeat(3, minmax(280px, 1fr));
    gap: 35px;
}}

/* CARD */
.card {{
    background: rgba(255, 255, 255, 0.15);
    backdrop-filter: blur(22px);
    padding: 38px 34px;
    border-radius: 26px;
    box-shadow: 0 20px 60px rgba(0,0,0,0.45);
    transition: all 0.4s ease;
    text-align: center;
}}

.card:hover {{
    transform: translateY(-12px) scale(1.02);
    background: rgba(255, 255, 255, 0.25);
}}

.card h3 {{
    font-size: 1.35rem;
    font-weight: 700;
    margin-bottom: 14px;
}}

.card p {{
    font-size: 1rem;
    line-height: 1.55;
    color: #d1fae5;
}}

/* FLOW - SIMPLIFIED (IMAGE + TITLE ONLY) */
.flow {{
    display: flex;
    justify-content: space-between;
    gap: 22px;
    align-items: stretch;
}}

.flow div {{
    flex: 1;
    text-align: center;
    padding: 24px 16px;
    background: rgba(255,255,255,0.18);
    border-radius: 20px;
    position: relative;
    overflow: hidden;
    
    /* Centering logic */
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 15px; /* Space between image and title */
    
    min-height: 140px;
    transition: all 0.3s ease;
}}

.flow div:hover {{
    background: rgba(255, 255, 255, 0.25);
    transform: translateY(-5px);
}}

.flow-step-image {{
    width: 64px !important;  /* Slightly larger since no text */
    height: 64px !important;
    border-radius: 12px;
    box-shadow: 0 8px 24px rgba(0,0,0,0.4);
    object-fit: cover !important;
    display: block;
}}

.flow-step-title {{
    font-size: 1.1rem; /* Slightly larger title */
    font-weight: 700;
    color: #ecfeff;
}}

/* FOOTER */
.footer {{
    text-align: center;
    padding: 35px;
    color: #99f6e4;
    opacity: 0.8;
}}

/* ANIMATION */
@keyframes fadeUp {{
    from {{
        opacity: 0;
        transform: translateY(45px);
    }}
    to {{
        opacity: 1;
        transform: translateY(0);
    }}
}}

</style>
""", unsafe_allow_html=True)

# HERO
st.markdown("""
<div class="hero">
    <h1>AgriDetect<span>AI</span></h1>
    <p>
        An intelligent crop-health platform that detects plant diseases early, 
        explains risks clearly, and helps farmers protect yield using AI.
    </p>
    <div>
        <a class="btn-primary">Login</a>
        <a class="btn-secondary">Register</a>
    </div>
</div>
""", unsafe_allow_html=True)

# WHY 
st.markdown("""
<div class="section">
    <h2>Why AgriDetectAI?</h2>
    <div class="grid">
        <div class="card">
            <h3>🌾 Unified Crop Intelligence</h3>
            <p>
                Farmers don't need separate tools for each crop. 
                Our unified model detects diseases across multiple plants 
                using a single intelligent pipeline.
            </p>
        </div>
        <div class="card">
            <h3>🧠 Deep Learning Accuracy</h3>
            <p>
                Built on fine-tuned ResNet architectures trained on 
                real agricultural datasets to ensure consistent, 
                research-grade predictions.
            </p>
        </div>
        <div class="card">
            <h3>🔍 Explainable AI</h3>
            <p>
                Visual indicators and confidence scores help users 
                understand *why* a disease was detected, not just the label.
            </p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# FLOW
st.markdown(f"""
<div class="section">
    <h2>How It Works</h2>
    <div class="flow">
        <div>
            <img src="data:image/png;base64,{flow_base64.get('login.png', '')}" class="flow-step-image" alt="Login">
            <div class="flow-step-title">Login</div>
        </div>
        <div>
            <img src="data:image/png;base64,{flow_base64.get('upload.png', '')}" class="flow-step-image" alt="Upload">
            <div class="flow-step-title">Upload Image</div>
        </div>
        <div>
            <img src="data:image/png;base64,{flow_base64.get('ai.png', '')}" class="flow-step-image" alt="AI">
            <div class="flow-step-title">AI Processing</div>
        </div>
        <div>
            <img src="data:image/png;base64,{flow_base64.get('disease.png', '')}" class="flow-step-image" alt="Disease">
            <div class="flow-step-title">Disease Detection</div>
        </div>
        <div>
            <img src="data:image/png;base64,{flow_base64.get('insights.png', '')}" class="flow-step-image" alt="Insights">
            <div class="flow-step-title">Get Insights</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# FUTURE 
st.markdown("""
<div class="section">
    <h2>What's Coming Next</h2>
    <div class="grid">
        <div class="card">
            <h3>🌐 AgriConnect</h3>
            <p>
                A collaborative ecosystem where farmers, 
                experts, and researchers share insights and solutions.
            </p>
        </div>
        <div class="card">
            <h3>🌦 Climate-Aware Alerts</h3>
            <p>
                AI-driven alerts that factor weather patterns 
                to predict disease outbreaks before they spread.
            </p>
        </div>
        <div class="card">
            <h3>📈 Smart Analytics</h3>
            <p>
                Historical crop health tracking, severity analysis, 
                and yield trend visualization.
            </p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# FOOTER
st.markdown("""
<div class="footer">
    © 2026 AgriDetectAI · AI for Smarter Agriculture 🌱
</div>
""", unsafe_allow_html=True)