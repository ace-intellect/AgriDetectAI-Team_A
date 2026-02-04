import streamlit as st
import base64
from PIL import Image
from io import BytesIO

# --- HELPER: CONVERT IMAGE TO BASE64 ---
def image_to_base64(image):
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()

def show(username):
    # --- 1. DEFINE CSS (Doctor-Style Upload + Profile Styles) ---
    st.markdown("""
<style>
/* ANIMATIONS */
@keyframes slideInLeft { from { opacity: 0; transform: translateX(-30px); } to { opacity: 1; transform: translateX(0); } }
@keyframes slideInRight { from { opacity: 0; transform: translateX(30px); } to { opacity: 1; transform: translateX(0); } }

/* GLASS CARD STYLES */
.profile-card {
    background: linear-gradient(135deg, rgba(255, 255, 255, 0.1), rgba(255, 255, 255, 0.05));
    backdrop-filter: blur(20px);
    border: 1px solid rgba(255, 255, 255, 0.2);
    border-radius: 24px;
    padding: 40px 20px;
    text-align: center;
    box-shadow: 0 20px 40px rgba(0,0,0,0.3);
    animation: slideInLeft 0.8s ease-out;
}

/* DOCTOR-STYLE UPLOADER FOR PROFILE */
[data-testid='stFileUploader'] section {
    background-color: rgba(255, 255, 255, 0.05);
    backdrop-filter: blur(12px);
    border: 2px dashed rgba(52, 211, 153, 0.5);
    border-radius: 15px;
    padding: 20px;
    text-align: center;
    transition: all 0.3s ease-in-out;
}
[data-testid='stFileUploader'] section:hover {
    background-color: rgba(52, 211, 153, 0.1);
    border-color: #34d399;
    box-shadow: 0 0 15px rgba(52, 211, 153, 0.3);
}
[data-testid='stFileUploader'] button {
    border: 1px solid #34d399;
    color: #34d399;
    border-radius: 50px;
}

/* AVATAR STYLES */
.avatar-container {
    width: 140px;
    height: 140px;
    margin: 0 auto 20px auto;
    position: relative;
}
.avatar-circle {
    width: 100%;
    height: 100%;
    background: linear-gradient(135deg, #34d399, #22d3ee);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 4rem;
    box-shadow: 0 10px 30px rgba(52, 211, 153, 0.5);
    border: 4px solid rgba(255,255,255,0.2);
    overflow: hidden; 
}
.avatar-img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}

/* BADGE & STATS */
.badge-pro {
    background: #fbbf24;
    color: #020617;
    padding: 6px 16px;
    border-radius: 50px;
    font-size: 0.75rem;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    display: inline-block;
    margin-bottom: 15px;
    box-shadow: 0 5px 15px rgba(251, 191, 36, 0.4);
}
.stat-mini {
    background: rgba(0, 0, 0, 0.2);
    padding: 15px;
    border-radius: 15px;
    margin-top: 20px;
    border: 1px solid rgba(255, 255, 255, 0.05);
}

/* RIGHT PANEL STYLES */
.settings-panel {
    background: rgba(0, 0, 0, 0.2);
    border-radius: 24px;
    padding: 40px;
    border: 1px solid rgba(255, 255, 255, 0.05);
    height: 100%;
    animation: slideInRight 1s ease-out;
}

/* WIDGET OVERRIDES */
.stTextInput input, .stSelectbox div[data-baseweb="select"] > div {
    background-color: rgba(0,0,0,0.3) !important;
    color: white !important;
    border-radius: 12px;
    border: 1px solid rgba(255,255,255,0.1) !important;
    padding: 10px;
}
.action-btn button {
    background: transparent;
    border: 1px solid #34d399;
    color: #34d399;
    border-radius: 12px;
    width: 100%;
    padding: 10px;
}
.action-btn button:hover {
    background: #34d399;
    color: black;
}
</style>
""", unsafe_allow_html=True)

    # --- HEADER ---
    st.markdown("<h1 style='margin-bottom: 10px;'>👤 My <span style='color:#34d399'>Profile</span></h1>", unsafe_allow_html=True)
    st.markdown("<p style='color: #cbd5e1; margin-bottom: 40px;'>Manage your account settings and preferences.</p>", unsafe_allow_html=True)

    c1, c2 = st.columns([1, 2], gap="large")

    # === LEFT COLUMN: PROFILE CARD ===
    with c1:
        # 1. BEAUTIFUL GLASS UPLOADER (Doctor Style)
        uploaded_avatar = st.file_uploader("Change Profile Picture", type=['jpg', 'png', 'jpeg'])

        # 2. LOGIC FOR AVATAR
        inner_avatar_html = "👨‍🌾"
        
        if uploaded_avatar is not None:
            image = Image.open(uploaded_avatar)
            img_b64 = image_to_base64(image)
            inner_avatar_html = f'<img src="data:image/png;base64,{img_b64}" class="avatar-img">'

        # 3. HTML STRING (FLUSH LEFT - NO INDENTATION)
        profile_html = f"""
<div class="profile-card">
<div class="badge-pro">PRO MEMBER</div>
<div class="avatar-container">
<div class="avatar-circle">
{inner_avatar_html}
</div>
</div>
<h2 style="margin:0; color: white; font-weight: 800;">{username}</h2>
<p style="color: #94a3b8; font-size: 0.95rem;">Precision Farmer</p>
<p style="color: #cbd5e1; margin-top: 25px; font-size: 0.9rem; line-height: 1.6;">
<b>ID:</b> #AG-8821<br>
<b>Location:</b> Nalgonda, TG
</p>
<div style="display: flex; gap: 10px; justify-content: center;">
<div class="stat-mini" style="flex:1;">
<div style="font-size:1.4rem; font-weight:bold; color:#34d399;">128</div>
<div style="font-size:0.7rem; color:#94a3b8;">SCANS</div>
</div>
<div class="stat-mini" style="flex:1;">
<div style="font-size:1.4rem; font-weight:bold; color:#22d3ee;">A+</div>
<div style="font-size:0.7rem; color:#94a3b8;">RATING</div>
</div>
</div>
</div>
"""
        st.markdown(profile_html, unsafe_allow_html=True)

    # === RIGHT COLUMN: SETTINGS ===
    with c2:
        st.markdown('<div class="settings-panel">', unsafe_allow_html=True)
        st.markdown("### ⚙️ Account Details")
        
        col_form1, col_form2 = st.columns(2)
        with col_form1:
            st.text_input("Full Name", value="Yeshwanth Ashala")
            st.text_input("Email", value="yeshwanth@agridetect.com")
        with col_form2:
            st.text_input("Phone Number", value="+91 98765 43210")
            st.selectbox("App Language", ["English", "Telugu (తెలుగు)", "Hindi (हिंदी)"])

        st.markdown("---")
        
        st.markdown("#### 🔔 Notification Preferences")
        col_t1, col_t2 = st.columns(2)
        with col_t1:
            st.toggle("Email Alerts", value=True)
            st.toggle("Whatsapp Updates", value=True)
        with col_t2:
            st.toggle("Dark Mode", value=True, disabled=True)
            st.toggle("Share Analytics Data", value=False)
        
        st.write("")
        st.write("")
        
        b1, b2, b3 = st.columns([1, 1, 1])
        with b1:
            st.markdown('<div class="action-btn">', unsafe_allow_html=True)
            if st.button("💾 Save Changes"):
                st.toast("Profile updated successfully!", icon="✅")
            st.markdown('</div>', unsafe_allow_html=True)
        
        with b2:
            st.markdown('<div class="action-btn">', unsafe_allow_html=True)
            st.button("🔑 Change Pass")
            st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)