import streamlit as st
import hashlib

# One-way hashing checker engine
def check_hash(user_input, correct_hash):
    scrambled_input = hashlib.sha256(user_input.strip().upper().encode()).hexdigest()
    return scrambled_input == correct_hash

# Global App Window Settings
st.set_page_config(page_title="Cyber Defense Operations Centre", page_icon="⚡", layout="centered")

# Next-Gen Cyber Terminal Theme Engine Injection
st.markdown("""
    <style>
    /* Premium Ultra-Dark Base */
    .stApp {
        background-color: #05070c;
    }
    
    /* Neon Typography Accents */
    .terminal-title {
        color: #00f3ff;
        font-family: 'Courier New', monospace;
        text-align: center;
        font-weight: 900;
        text-shadow: 0 0 15px rgba(0, 243, 255, 0.4);
        margin-bottom: 2px;
        letter-spacing: 2px;
    }
    .terminal-subtitle {
        color: #5d6b82;
        font-family: -apple-system, BlinkMacSystemFont, sans-serif;
        text-align: center;
        font-size: 13px;
        font-weight: 500;
        margin-bottom: 25px;
    }
    
    /* Brighter Container Box for Ultra-Clear Text Fill Visibility */
    div[data-testid="stVerticalBlockBorderWithDetails"] {
        background-color: #161f30 !important;
        border: 2px solid #24334d !important;
        border-radius: 14px !important;
        padding: 30px !important;
        box-shadow: 0 12px 40px 0 rgba(0, 0, 0, 0.6) !important;
        transition: border 0.3s ease-in-out;
    }
    div[data-testid="stVerticalBlockBorderWithDetails"]:focus-within {
        border: 2px solid #00f3ff !important;
    }
    
    /* Custom Challenge Header Styles */
    .challenge-header {
        font-family: -apple-system, BlinkMacSystemFont, sans-serif;
        font-size: 1.7rem;
        color: #ffffff;
        margin-bottom: 15px;
    }
    .challenge-header strong {
        font-weight: 800 !important;
    }
    .challenge-header span {
        font-weight: 400 !important;
    }

    /* Target Code Blocks & Force Large Font-Size Uniformly */
    div[data-testid="stCodeBlock"] code {
        font-size: 16px !important;
        font-family: 'Courier New', monospace !important;
        line-height: 1.5 !important;
    }
    
    .cipher-label {
        color: #00f3ff !important;
        font-weight: 800 !important;
        font-family: 'Courier New', monospace;
        font-size: 16px !important;
        display: block;
        margin-bottom: 8px;
    }
    
    /* Sleek Horizontal Navigation System */
    .progress-banner {
        display: flex;
        justify-content: space-between;
        gap: 8px;
        margin-bottom: 25px;
        font-family: 'Courier New', monospace;
        font-size: 11px;
        font-weight: bold;
    }
    .progress-node {
        flex: 1;
        text-align: center;
