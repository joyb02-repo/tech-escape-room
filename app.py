import streamlit as st
import os

# Page Configuration
st.set_page_config(page_title="Checkout (Version 1.0.4 FINAL RUN)", layout="centered")

# --- CUSTOM HOVER & BAD DESIGN OVERRIDES (CSS) ---
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Comic+Neue:ital,wght@0,400;0,700;1,400&family=Impact&display=swap');

        /* Using an unprofessional font choice for an enterprise checkout page */
        html, body, [data-testid="stAppViewContainer"], [class*="st-"] {
            font-family: 'Comic Neue', cursive !important;
        }

        /* Confusing, inconsistent header colors that conflict with the purple logo */
        .bad-banner {
            background-color: #FFDE59 !important; /* Neon Yellow */
            border: 3px dashed #FF3131 !important; /* Bright Red */
            padding: 15px !important;
            text-align: left !important;
            margin-bottom: 25px !important;
            border-radius: 0px !important;
        }

        .bad-banner h2 {
            color: #0000FF !important; /* Pure saturated Blue */
            font-size: 18px !important;
            margin: 0 0 8px 0 !important;
            font-weight: bold !important;
            text-align: center !important;
        }

        .bad-banner p {
            color: #FF3131 !important;
            font-size: 13px !important;
            margin: 4px 0 !important;
            font-weight: bold !important;
            line-height: 1.4 !important;
        }

        .cipher-box {
            font-family: monospace !important; 
            font-size: 15px !important; 
            background: white !important; 
            padding: 2px 6px !important; 
            border: 1px solid black !important; 
            color: black !important;
            display: inline-block !important;
            margin-top: 4px !important;
        }

        /* Tiny sneaky text for terms and conditions */
        .sneaky-text label p {
            font-size: 9px !important;
            color: #94A3B8 !important;
        }

        /* Force square inputs */
        div[data-testid="stTextInput"] input, div[data-testid="stSelectbox"] div {
            background-color: #FFFBEB !important;
            border-radius: 0px !important;
        }

        /* Making the primary cancel button look more attractive than the purchase button */
        div.stButton > button {
            border-radius: 0px !important;
        }
    </style>
""", unsafe_allow_html=True)

# --- BRAND LOGO (Color-matched to your theme) ---
logo_path = "logo.png"
if os.path.exists(logo_path):
    left, center, right = st.columns([1, 1.5, 1])
    with center:
        st.markdown("""
            <div style="text-align: center; margin-bottom: 5px; filter: invert(34%) sepia(85%) saturate(1915%) hue-rotate(253deg) brightness(96%) contrast(97%);">
                <img src="app/static/logo.png" width="130" style="display: block; margin: 0 auto;"/>
            </div>
        """, unsafe_allow_html=True)
else:
    st.markdown("<h2 style='text-align: center; color: #9333EA; font-family: Impact; letter-spacing: 4px;'>SHARK TANK</h2>", unsafe_allow_html=True)

# --- POORLY DESIGNED HEADER BANNER WITH CIPHER CHALLENGE ---
st.markdown("""
    <div class="bad-banner">
        <h2>⚠️ SYSTEM LOCKED BY SYSTEM ADMINISTRATOR</h2>
        <p><strong>SECURITY CIPHER:</strong> <span class="cipher-box">Wkh sdvvzrug lv Srzhu</span></p>
        <p><strong>HINT 1:</strong> The shift key algorithm used to lock this screen is '3'.</p>
        <p><strong>HINT 2:</strong> The third character of the decrypted text string resolves to the letter 'e'.</p>
    </div>
""", unsafe_allow_html=True)

# --- SHOPPING CART SUMMARY ---
st.subheader("Your Items")
col1, col2 = st.columns([3, 1])
with col1:
    st.caption("Premium Ultra-Soft Gaming Socks (Size: Random)")
with col2:
    st.markdown("**$89.99**")

st.markdown("---")

# --- BAD USER INTERFACE FORMS ---
st.subheader("Delivery & Financial Data Entry")

country = st.text_input("Enter Country First", value="Worldwide")
full_name = st.text_input("Type everything here (First Name, Middle, Last Name, Title, Apartment Number)")
card_type = st.selectbox("Select Payment Method Type", ["- Select One -", "Crypto Token", "Gift Voucher Code", "Standard Credit Card", "Bank Wire transfer"])
card_number = st.text_input("Type your 16 digit card number out loud (No spaces allowed)", placeholder="4111222233334444")

c1, c2, c3 = st.columns(3)
with c1:
    expiry_month = st.text_input("Month (MM)")
with c2:
    expiry_year = st.text_input("Year (YYYY)")
with c3:
    cvv = st.text_input("Secret Code")

# Pre-checked recurring hidden options
st.markdown('<div class="sneaky-text">', unsafe_allow_html=True)
opt_in_1 = st.checkbox("Sign me up for the weekly magazine and share my address with trusted third-party marketing affiliates.", value=True)
opt_in_2 = st.checkbox("Automatically renew this ordering attempt as a monthly recurring subscription fee.", value=True)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")

# --- CONFLICTING BUTTON HIERARCHY ---
btn_col1, btn_col2 = st.columns(2)

with btn_col1:
    if st.button("CANCEL ORDER AND ERASE ALL HISTORY", type="primary", use_container_width=True):
        st.error("Cart emptied successfully.")

with btn_col2:
    if st.button("submit data", type="secondary", use_container_width=True):
        st.success("Processing payment...")
