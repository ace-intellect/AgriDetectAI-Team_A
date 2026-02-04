import streamlit as st
import time
import database as db

# --- MODERN AUTHENTICATION UI ---
def inject_auth_css():
    st.markdown("""
    <style>
    /* 1. TARGET THE FORM CONTAINER DIRECTLY (The Glass Card) */
    [data-testid="stForm"] {
        background: rgba(15, 23, 42, 0.6);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 24px;
        padding: 50px 40px;
        box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
        text-align: center;
        animation: slideUp 0.6s cubic-bezier(0.16, 1, 0.3, 1);
    }

    /* 2. INPUT FIELDS (Modern & Sleek) */
    div[data-baseweb="input"] > div {
        background-color: rgba(0, 0, 0, 0.3) !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 12px !important;
        color: white !important;
        padding: 6px;
        transition: all 0.3s ease;
    }
    
    /* Input Focus State */
    div[data-baseweb="input"] > div:focus-within {
        border-color: #34d399 !important;
        box-shadow: 0 0 15px rgba(52, 211, 153, 0.3) !important;
        background-color: rgba(0, 0, 0, 0.5) !important;
    }
    
    /* Text Color */
    input[class] {
        color: #ecfeff !important;
        font-weight: 500 !important;
    }

    /* Animations */
    @keyframes slideUp {
        from { opacity: 0; transform: translateY(30px); }
        to { opacity: 1; transform: translateY(0); }
    }

    /* 3. TYPOGRAPHY */
    .auth-header {
        font-size: 2.5rem;
        font-weight: 800;
        margin-bottom: 10px;
        background: linear-gradient(to right, #ffffff, #94a3b8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
    }
    .auth-sub {
        color: #64748b;
        font-size: 0.95rem;
        margin-bottom: 30px;
        text-align: center;
    }
    
    /* 4. BUTTONS (Inside Form) */
    .stButton button {
        background: linear-gradient(135deg, #34d399 0%, #059669 100%) !important;
        color: white !important;
        border: none !important;
        padding: 12px 24px !important;
        font-weight: 600 !important;
        border-radius: 12px !important;
        width: 100%;
        transition: transform 0.2s;
    }
    .stButton button:hover {
        transform: scale(1.02);
        box-shadow: 0 10px 25px -5px rgba(52, 211, 153, 0.4);
    }
    
    /* Secondary Link Button (Outside Form) */
    button[kind="secondary"] {
        background: transparent !important;
        border: 1px dashed #475569 !important;
        color: #94a3b8 !important;
    }
    button[kind="secondary"]:hover {
        border-color: #34d399 !important;
        color: #34d399 !important;
        background: rgba(52, 211, 153, 0.05) !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- LOGIN UI ---
def show_login():
    inject_auth_css()
    
    # Center the Layout: [Space] [Card] [Space]
    c1, c2, c3 = st.columns([1, 1.2, 1])
    
    with c2:
        # HEADER (Outside form so it doesn't get submitted)
        st.markdown("""
            <div style="text-align: center; font-size: 3.5rem; margin-bottom: 15px;">👋</div>
            <div class="auth-header">Welcome Back</div>
            <div class="auth-sub">Enter your credentials to access the dashboard.</div>
        """, unsafe_allow_html=True)

        # THE FORM (This is the Glass Card)
        with st.form("login_form"):
            username = st.text_input("Username", placeholder="e.g. farmer_yeshwanth")
            st.write("") # Micro-spacing
            password = st.text_input("Password", type="password", placeholder="••••••••")
            
            st.write("") 
            st.write("") 
            
            # Submit Button
            submitted = st.form_submit_button("Sign In")
            
            if submitted:
                if username and password:
                    user = db.get_user(username)
                    if user and user[1] == password:
                        st.session_state.logged_in = True
                        st.session_state.username = username
                        st.success("Login Successful!")
                        time.sleep(0.5)
                        st.session_state.page = 'dashboard'
                        st.rerun()
                    else:
                        st.error("Invalid Credentials. Please try again.")
                else:
                    st.warning("Please fill in both fields.")

        # Divider
        st.markdown("""
            <div style="display: flex; align-items: center; margin: 25px 0; color: #475569;">
                <div style="flex-grow: 1; height: 1px; background: #334155;"></div>
                <span style="padding: 0 10px; font-size: 0.8rem;">OR</span>
                <div style="flex-grow: 1; height: 1px; background: #334155;"></div>
            </div>
        """, unsafe_allow_html=True)

        # Register Switch
        if st.button("Create New Account", type="secondary"):
            st.session_state.page = 'signup'
            st.rerun()

# --- SIGNUP UI ---
def show_signup():
    inject_auth_css()
    
    c1, c2, c3 = st.columns([1, 1.2, 1])
    
    with c2:
        # Header
        st.markdown("""
            <div style="text-align: center; font-size: 3.5rem; margin-bottom: 15px;">🌱</div>
            <div class="auth-header">Join AgriDetect</div>
            <div class="auth-sub">Start your smart farming journey today.</div>
        """, unsafe_allow_html=True)
        
        # THE FORM (Glass Card)
        with st.form("signup_form"):
            new_user = st.text_input("Choose Username", placeholder="e.g. crop_master")
            new_email = st.text_input("Email Address", placeholder="you@example.com")
            
            # Split Password Fields
            p1, p2 = st.columns(2)
            with p1: new_pass = st.text_input("Password", type="password")
            with p2: confirm_pass = st.text_input("Confirm", type="password")
            
            st.write("")
            
            # Submit Button
            submitted = st.form_submit_button("Create Account")
            
            if submitted:
                if new_user and new_pass and new_email:
                    if new_pass != confirm_pass:
                        st.error("Passwords do not match.")
                    else:
                        success = db.add_user(new_user, new_pass, new_email)
                        if success:
                            st.balloons()
                            st.success("Account Created! Redirecting to Login...")
                            time.sleep(1.5)
                            st.session_state.page = 'login'
                            st.rerun()
                        else:
                            st.error("Username already exists.")
                else:
                    st.warning("All fields are required.")

        # Divider
        st.markdown("""
            <div style="display: flex; align-items: center; margin: 25px 0; color: #475569;">
                <div style="flex-grow: 1; height: 1px; background: #334155;"></div>
                <span style="padding: 0 10px; font-size: 0.8rem;">ALREADY HAVE AN ACCOUNT?</span>
                <div style="flex-grow: 1; height: 1px; background: #334155;"></div>
            </div>
        """, unsafe_allow_html=True)
        
        if st.button("Sign In", type="secondary"):
            st.session_state.page = 'login'
            st.rerun()