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
        padding: 8px 4px;
        border-radius: 8px;
        background: #090d14;
        color: #3b4759;
        border: 1px solid #161f2e;
        transition: all 0.3s ease;
    }
    .progress-node.active {
        background: rgba(0, 243, 255, 0.1);
        color: #00f3ff;
        border: 1px solid #00f3ff;
        box-shadow: 0 0 10px rgba(0, 243, 255, 0.2);
    }
    .progress-node.complete {
        background: rgba(168, 85, 247, 0.08);
        color: #a855f7;
        border: 1px solid rgba(168, 85, 247, 0.35);
    }

    /* Beautiful High-Contrast Buttons */
    .stButton>button {
        background: linear-gradient(90deg, #00f3ff 0%, #a855f7 100%) !important;
        color: #05070c !important;
        font-weight: 800 !important;
        text-transform: uppercase !important;
        letter-spacing: 1px !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 12px 24px !important;
        font-family: 'Courier New', monospace !important;
        width: 100% !important;
        box-shadow: 0 4px 15px rgba(0, 243, 255, 0.25) !important;
        transition: all 0.2s ease-in-out !important;
        margin-top: 10px;
    }
    .stButton>button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 20px rgba(168, 85, 247, 0.45) !important;
    }
    
    /* Styled Input Panels */
    input {
        background-color: #0d1421 !important;
        color: #ffffff !important;
        border: 1px solid #2d3f5e !important;
        border-radius: 6px !important;
    }
    input:focus {
        border-color: #00f3ff !important;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize Session Frame State Tracking
if "stage" not in st.session_state:
    st.session_state.stage = 1

# Display Terminal Branding
st.markdown('<h1 class="terminal-title">MAINFRAME BREACH</h1>', unsafe_allow_html=True)
st.markdown('<p class="terminal-subtitle">Secured Security Architecture Diagnostic Suite v3.2.6</p>', unsafe_allow_html=True)

# Generate Dynamic Matrix Tracking Steps Header Bar
nodes = ["Cryptogram", "Circuitry", "Binary", "Debugging", "Data Schema", "Network"]
banner_html = '<div class="progress-banner">'
for i, name in enumerate(nodes, 1):
    status_class = "progress-node"
    if st.session_state.stage == i:
        status_class += " active"
    elif st.session_state.stage > i:
        status_class += " complete"
    banner_html += f'<div class="{status_class}">STAGE {i}</div>'
banner_html += '</div>'
st.markdown(banner_html, unsafe_allow_html=True)


# =========================================================================
# CENTRALIZED SECURE CONTAINER 
# Locks all active challenge parameters into your specified bounding layout box.
# =========================================================================
with st.container(border=True):

    # CHALLENGE 1: CAESAR CIPHER VARIANT
    if st.session_state.stage == 1:
        st.markdown("### **Challenge 1:** Encryption Matrix Override")
        st.write("An intercepted system log contains a shifted string payload. Reconstruct the cipher framework to bypass.")
        st.code("""
Cipher text: Wkh sdvvzrug lv Srzhu
        """, language="text")
        
        st.markdown("""
        **Operational Diagnostic Feed:**
        * The security structure runs on a classic linear **Shift Key of '3'**.
        * Calibration Node: The third character (`h`) evaluates cleanly to the letter **'e'** when decrypted.
        """)
        st.caption("🔍 Strategy: Trace the final string cluster (`Srzhu`) 3 steps backward through the alphabet space to find the access string key.")
        
        user_input = st.text_input("Decrypt key word payload:", key="in_1", placeholder="Type response here...").strip().upper()
        if st.button("EXECUTE HANDSHAKE UNLOCK", key="b_1"):
            if user_input == "POWER" or check_hash(user_input, "2f8263cf8bb82ec7da117c2be6d11a8080f83359d48b1116c905327b73840e79"):
                st.session_state.stage = 2
                st.rerun()
            else:
                st.error("❌ Handshake Rejected: Invalid encryption signature decryption mapping sequence.")

    # CHALLENGE 2: LOGIC GATE TOPOLOGY
    elif st.session_state.stage == 2:
        st.markdown("### **Challenge 2:** Logic Circuit Topology Evaluation")
        st.write("A power spike tripped the hardware safety relays. Calculate the end-terminal state of this logical path grid.")
        st.code("""
[Input Node A: 1] ───┐
                    ├───► [ AND Gate ] ───┐
[Input Node B: 0] ───┘                     │
                                           ├───► [ OR Gate ] ───► TERMINAL OUTPUT?
                                           │
[Input Node C: 1] ───► [ NOT Gate ] ───────┘
        """, language="text")
        
        user_input = st.text_input("Enter the terminal bit registry output value (0 or 1):", key="in_2").strip()
        if st.button("VERIFY VOLTAGE LOGIC", key="b_2"):
            if user_input == "0" or check_hash(user_input, "5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9"):
                st.session_state.stage = 3
                st.rerun()
            else:
                st.error("❌ Logic Check Fault: Circuit configuration loop detected. Output state unverified.")

    # CHALLENGE 3: BINARY DECODER
    elif st.session_state.stage == 3:
        st.markdown("### **Challenge 3:** Core Hex/Binary Memory Trace")
        st.write("The underlying storage sector is guarded by a 4-letter ASCII access phrase. Read the volatile system memory bank:")
        st.code("""
Registers: [01000011]  [01001111]  [01000100]  [01000101]
        """, language="text")
        st.caption("💡 Translation Manual: Array equivalents track to decimal positions: 67, 79, 68, 69. (Note: Upper-case letter 'A' maps to position index 65)")
        
        user_input = st.text_input("Translate extracted target string sequence:", key="in_3").strip().upper()
        if st.button("BYPASS MEMORY FIREWALL", key="b_3"):
            if user_input == "CODE" or check_hash(user_input, "9a661b0a52df03aa6240292797e88f00072b49c001cbe3d007ec1dfb1b60f588"):
                st.session_state.stage = 4
                st.rerun()
            else:
                st.error("❌ Character Check Mismatch: Data stream corruption flagged inside sector validation tables.")

    # CHALLENGE 4: BUG HUNTING
    elif st.session_state.stage == 4:
        st.markdown("### **Challenge 4:** Diagnostic Script Compilation Fix")
        st.write("The secondary firewall validation module has a minor syntax bug preventing launch. Fix the loop declaration syntax.")
        st.code("""
def check_password(password)
    if len(password) < 8
        print("Password flagged: Weak security index profile.")
        """, language="python")
        
        user_input = st.text_input("Enter the missing token operator character from lines 1 and 2:", key="in_4").strip()
        if st.button("COMPILE SYNTAX OVERRIDE PATCH", key="b_4"):
            if user_input == ":" or check_hash(user_input, "76f0d14b4369a473468087920bb6148303f8fcb151bf99994c979cf7b198889a"):
                st.session_state.stage = 5
                st.rerun()
            else:
                st.error("❌ Script Error: Interpreter execution thread crashed. Review structural delimiter markers.")

    # CHALLENGE 5: SQL STRUCTURE
    elif st.session_state.stage == 5:
        st.markdown("### **Challenge 5:** Database Query Isolation")
        st.write("Isolate target entry anomalies from the core logs. Input the correct SQL keyword array statement to weed out redundant duplicate values.")
        st.code("""
SELECT ___________ client_ip FROM mainframe_security_logs;
        """, language="sql")
        
        user_input = st.text_input("Complete the missing query operator pattern keyword string:", key="in_5", placeholder="Keyword...").strip().upper()
        if st.button("EXECUTE STRUCTURED DATA QUERY", key="b_5"):
            if user_input == "DISTINCT" or check_hash(user_input, "601e3895bd97ff645e9987a0709b456db97f8c057692095b6a71e1f74463402e"):
                st.session_state.stage = 6
                st.rerun()
            else:
                st.error("❌ Data Layer Exception: Command execution returned duplicate relational vectors.")

    # CHALLENGE 6: SUBNET DNS PROTOCOLS
    elif st.session_state.stage == 6:
        st.markdown("### **Challenge 6:** Network Layer Protocol Mapping")
        st.write("Complete the external routing handshake. Identify which backbone system structure protocol translates dynamic domain text addresses into clean numeric computer IP strings.")
        
        user_input = st.text_input("Enter the 3-letter networking acronym standard protocol:", key="in_6", placeholder="e.g. BGP, ARP, SSH...").strip().upper()
        if st.button("TERMINATE ROOT ROUTING HANDSHAKE", key="b_6"):
            if user_input == "DNS" or check_hash(user_input, "e5b72195f22e700cf1cb765f606e10885e35e7df5d1bf25577609278065c711a"):
                st.session_state.stage = 7
                st.rerun()
            else:
                st.error("❌ Subnet Routing Failure: Destination host path string target unresolved.")

    # ESCAPE SUCCESS TERMINAL MODULE
    elif st.session_state.stage == 7:
        st.balloons()
        st.markdown("<h3 style='color:#00f3ff; font-family:\"Courier New\", monospace; text-align: center; letter-spacing: 1px;'>EXFILTRATION COMPLETE</h3>", unsafe_allow_html=True)
        st.write("Outstanding deployment, Operator. You realigned encryption arrays, bypassed faulty circuits, read low-level registers, patched code syntax, cleaned database tables, and successfully routed the payload past perimeter defenses.")
        
        if st.button("RESET SIMULATOR COLD-BOOT MATRIX 🔁"):
            st.session_state.stage = 1
            st.rerun()
