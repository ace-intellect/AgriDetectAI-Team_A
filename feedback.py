import streamlit as st
import time

def show():
    # --- CUSTOM CSS ---
    st.markdown("""
    <style>
    /* 1. APPLY GLASS STYLE DIRECTLY TO THE FORM (Fixes the Empty Div issue) */
    [data-testid="stForm"] {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 30px;
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    /* 2. RECENT FEEDBACK CARDS (Right Side) */
    .feedback-card {
        background: rgba(0, 0, 0, 0.2);
        border-left: 4px solid #34d399;
        border-radius: 10px;
        padding: 15px;
        margin-bottom: 15px;
        transition: transform 0.2s;
    }
    .feedback-card:hover {
        transform: translateX(5px);
        background: rgba(0, 0, 0, 0.3);
    }
    .user-name {
        color: #34d399;
        font-weight: bold;
        font-size: 0.9rem;
        margin-bottom: 5px;
    }
    .user-role {
        color: #94a3b8;
        font-size: 0.8rem;
        font-weight: normal;
    }
    .feedback-text {
        color: #e2e8f0;
        font-size: 0.95rem;
        font-style: italic;
    }
    .star-rating {
        color: #fbbf24;
        font-size: 0.8rem;
        margin-top: 5px;
    }

    /* 3. INPUT STYLING */
    .stTextInput input, .stTextArea textarea {
        background-color: rgba(0,0,0,0.3) !important;
        border: 1px solid rgba(255,255,255,0.1) !important;
        color: white !important;
        border-radius: 8px;
    }
    .stSelectbox div[data-baseweb="select"] > div {
        background-color: rgba(0,0,0,0.3) !important;
        color: white !important;
        border: 1px solid rgba(255,255,255,0.1) !important;
    }
    
    /* 4. SUBMIT BUTTON */
    .stButton button {
        background: linear-gradient(90deg, #22d3ee, #34d399);
        color: #020617;
        font-weight: 800;
        width: 100%;
        border-radius: 10px;
        padding: 10px;
        border: none;
    }
    </style>
    """, unsafe_allow_html=True)

    # --- TITLE ---
    st.markdown("<h1 style='text-align: center;'>💬 Community <span style='color:#34d399'>Feedback</span></h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #cbd5e1; margin-bottom: 40px;'>Help us improve the AI by sharing your field experience.</p>", unsafe_allow_html=True)

    # --- LAYOUT: LEFT (FORM) | RIGHT (WALL OF LOVE) ---
    c1, c2 = st.columns([1.5, 1], gap="large")

    # === LEFT COLUMN: THE FORM ===
    with c1:
        # We start the form immediately. The CSS above targets [data-testid="stForm"] 
        # so we DO NOT need to wrap this in a div anymore.
        with st.form("user_feedback"):
            st.markdown("### 📝 Submit Your Review")
            
            # 1. Category Selection
            st.markdown("<p style='margin-bottom: 5px; color:#cbd5e1;'>What is this feedback about?</p>", unsafe_allow_html=True)
            category = st.radio(
                "Hidden Label",
                ["🌱 Accuracy Issue", "🐛 Bug Report", "💡 Feature Request", "❤️ General Appreciation"],
                horizontal=True,
                label_visibility="collapsed"
            )

            st.write("") # Spacer

            # 2. Main Inputs
            col_in1, col_in2 = st.columns(2)
            with col_in1:
                name = st.text_input("Your Name (Optional)", placeholder="e.g. Rahul Verma")
            with col_in2:
                crop = st.selectbox("Related Crop", ["General", "Rice", "Potato", "Wheat", "Tomato", "Cotton"])

            subject = st.text_input("Subject", placeholder="Brief summary...")
            message = st.text_area("Detailed Feedback", placeholder="Describe your experience or issue...", height=120)

            # 3. Rating & Accuracy Check
            st.write("")
            st.markdown("---")
            c_r1, c_r2 = st.columns(2)
            with c_r1:
                st.markdown("**Overall Experience**")
                rating = st.slider("Rate Us", 1, 5, 5, label_visibility="collapsed")
            with c_r2:
                st.markdown("**Did the AI diagnose correctly?**")
                accuracy = st.radio("AI Accuracy", ["Yes, Spot on! ✅", "Partially ⚠️", "No, Incorrect ❌"], horizontal=True, label_visibility="collapsed")

            # 4. Submit
            st.write("")
            submitted = st.form_submit_button("🚀 Submit Feedback")
            
            if submitted:
                # Simulate backend processing
                with st.spinner("Sending to server..."):
                    time.sleep(1.5)
                st.success("✅ Thank you! Your feedback helps our model learn.")
                st.balloons()

    # === RIGHT COLUMN: RECENT REVIEWS ===
    with c2:
        st.markdown("### 🌍 Recent Activity")
        st.markdown("<p style='color:#94a3b8; font-size:0.9rem; margin-bottom:20px;'>See what other farmers are saying.</p>", unsafe_allow_html=True)

        # Static Feedback Cards (HTML)
        st.markdown("""
        <div class="feedback-card">
            <div class="user-name">Venkatesh K. <span class="user-role">· Rice Farmer</span></div>
            <div class="star-rating">⭐⭐⭐⭐⭐</div>
            <div class="feedback-text">"The Rice Blast detection saved my crop this season. The chemical suggestion was exactly what the local officer recommended too."</div>
            <div style="margin-top:10px; font-size:0.8rem; color:#34d399;">✅ AI Diagnosis Confirmed</div>
        </div>
        
        <div class="feedback-card" style="border-left-color: #fbbf24;">
            <div class="user-name">Sarah Jenkins <span class="user-role">· Researcher</span></div>
            <div class="star-rating">⭐⭐⭐⭐</div>
            <div class="feedback-text">"Great accuracy on Potato Late Blight. Would love to see support for Maize crops in the next update."</div>
        </div>

        <div class="feedback-card" style="border-left-color: #f87171;">
            <div class="user-name">Rajesh Kumar <span class="user-role">· Farmer</span></div>
            <div class="star-rating">⭐⭐⭐</div>
            <div class="feedback-text">"The app is good but sometimes takes time to load in my village due to low network. Please add offline mode."</div>
        </div>

        <div class="feedback-card">
            <div class="user-name">Anitha R. <span class="user-role">· Student</span></div>
            <div class="star-rating">⭐⭐⭐⭐⭐</div>
            <div class="feedback-text">"Used this for my final year project reference. The UI is incredibly smooth and modern!"</div>
        </div>
        """, unsafe_allow_html=True)