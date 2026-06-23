import streamlit as st
import hashlib

# One-way hashing checker engine to shield answers from source repositories
def check_hash(user_input, correct_hash):
    # Standardize input variations: strips white space and forces upper-case matching
    scrambled_input = hashlib.sha256(user_input.strip().upper().encode()).hexdigest()
    return scrambled_input == correct_hash

# Set page configuration with a wide canvas structure
st.set_page_config(page_title="Cyber Defense Escape Room", page_icon="⚡", layout="centered")

# Injection of an elite, modern dark-mode gaming layout with custom styling hooks
st.markdown("""
    <style>
    /* Dark Theme Core Resets */
    .stApp {
        background-color: #080a0f;
    }
    
    /* Immersive Typography Elements */
    .terminal-title {
        color: #00f3ff;
        font-family: 'Courier New', monospace;
        text-align: center;
        font-weight: 800;
        text-shadow: 0 0 12px rgba(0, 243, 255, 0.4);
        margin-bottom: 5px;
    }
    .terminal-subtitle {
        color: #b4b9c3;
        font-family: -apple-system, sans-serif;
        text-align: center;
        font-size: 14px;
        margin-bottom: 25px;
    }
    
    /* Modern Dashboard Node Cards (Glassmorphism design) */
    .stage-card {
        background: rgba(17, 24, 39, 0.7);
        border: 1px solid rgba(0, 243, 255, 0.2);
        border-radius: 16px;
        padding: 24px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        backdrop-filter: blur(4px);
        margin-bottom: 20px;
    }
    
    /* Dynamic Dashboard Navigation Banner badges */
    .progress-banner {
        display: flex;
        justify-content: space-between;
        margin-bottom: 25px;
        font-family: 'Courier New', monospace;
        font-size: 11px;
    }
    .progress-node {
        padding: 6px 12px;
        border-radius: 20px;
        background: #111827;
        color: #4b5563;
        border: 1px solid #1f2937;
    }
    .progress-node.active {
        background: rgba(0, 243, 255, 0.1);
        color: #00f3ff;
        border: 1px solid #00f3ff;
        box-shadow: 0 0 8px rgba(0, 243, 255, 0.2);
    }
    .progress-node.complete {
        background: rgba(168, 85, 247, 0.1);
        color: #a855f7;
        border: 1px solid #a855f7;
    }

    /* Cyberpunk Styled Control Buttons */
    .stButton>button {
        background: linear-gradient(90deg, #00f3ff 0%, #a855f7 100%);
        color: #000000 !important;
        font-weight: 700;
        letter-spacing: 1px;
        border: none;
        border-radius: 8px;
        padding: 10px 24px;
        font-family: 'Courier New', monospace;
        width: 100%;
        box-shadow: 0 4px 14px 0 rgba(0, 243, 255, 0.3);
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px 0 rgba(168, 85, 247, 0.5);
    }
    </style>
""", unsafe_allow_html=True)

# Central session tracking configuration 
if "stage" not in st.session_state:
    st.session_state.stage = 1

# Header Layout Elements
st.markdown('<h1 class="terminal-title">⚡ MAINFRAME BREACH</h1>', unsafe_allow_html=True)
st.markdown('<p class="terminal-subtitle">Secured Security Architecture Diagnostic Suite v3.2.6</p>', unsafe_allow_html=True)

# Build Dynamic Navigation Steps Layout Indicator Bar
nodes = ["Cryptogram", "Circuitry", "Binary", "Debugging", "Data Schema", "Network"]
banner_html = '<div class="progress-banner">'
for i, name in enumerate(nodes, 1):
    status_class = "progress-node"
    if st.session_state.stage == i:
        status_class += " active"
    elif st.session_state.stage > i:
        status_class += " complete"
    banner_html += f'<div class="{status_class}">S{i}: {name}</div>'
banner_html += '</div>'
st.markdown(banner_html, unsafe_allow_html=True)


# =========================================================================
# CHALLENGE 1: THE CRYPTOGRAM
# =========================================================================
if st.session_state.stage == 1:
    st.markdown('<div class="stage-card">', unsafe_allow_html=True)
    st.subheader("🔒 Challenge 1: Cipher Matrix Decryption")
    st.write("An anonymous proxy node left an encrypted intercept packet. Reconstruct the system alphabet string mapping array.")
    
    st.code("""
    Cipher text: X S B   P S Q O W   G T   W S Q O T H U   G S P   S Q P P T H U 
    
    Decoder Array: X=T, S=H, B=E, P=P, O=O, W=W, G=S, T=I, U=G, H=N
    """, language="text")
    st.caption("🔍 Strategy: Decode the second word string block (`P S Q O W`) to find the sector bypass key.")
    
    user_input = st.text_input("Decrypt key word payload:", key="in_1", placeholder="Type response here...").strip().upper()
    
    if st.button("EXECUTE HANDSHAKE UNLOCK 🔓", key="b_1"):
        if user_input == "POWER" or check_hash(user_input, "2f8263cf8bb82ec7da117c2be6d11a8080f83359d48b1116c905327b73840e79"):
            st.session_state.stage = 2
            st.rerun()
        else:
            st.error("❌ Handshake Rejected: Invalid encryption signature decryption.")
    st.markdown('</div>', unsafe_allow_html=True)

# =========================================================================
# CHALLENGE 2: THE LOGIC GATE MAZE
# =========================================================================
elif st.session_state.stage == 2:
    st.markdown('<div class="stage-card">', unsafe_allow_html=True)
    st.subheader("🧩 Challenge 2: Logic Circuit Topology Evaluation")
    st.write("A power surge tripped the internal safety relay architecture. Compute the end result bit stream state below.")
    
    st.code("""
    [Input Node A: 1] ───┐
                        ├───► [ AND Gate ] ───┐
    [Input Node B: 0] ───┘                     │
                                               ├───► [ OR Gate ] ───► TERMINAL OUTPUT?
                                               │
    [Input Node C: 1] ───► [ NOT Gate ] ───────┘
    """, language="text")
    
    user_input = st.text_input("Enter the terminal bit registry integer output value (0 or 1):", key="in_2").strip()
    
    if st.button("VERIFY VOLTAGE LOGIC 🔓", key="b_2"):
        if user_input == "0" or check_hash(user_input, "5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9"):
            st.session_state.stage = 3
            st.rerun()
        else:
            st.error("❌ Logic Check Fault: Circuit configuration loop detected.")
    st.markdown('</div>', unsafe_allow_html=True)

# =========================================================================
# CHALLENGE 3: BINARY CODE BREAKER
# =========================================================================
elif st.session_state.stage == 3:
    st.markdown('<div class="stage-card">', unsafe_allow_html=True)
    st.subheader("💾 Challenge 3: Core Hex/Binary Memory Trace")
    st.write("The secondary firewall folder requires a 4-character ASCII access string phrase. Extract the hidden bytes:")
    
    st.code("""
    Registers: [01000011]  [01001111]  [01000100]  [01000101]
    """, language="text")
    st.caption("💡 Reference Dictionary: Decimal equivalents evaluate to: 67, 79, 68, 69. (Note: Upper-case letter 'A' matches index 65)")
    
    user_input = st.text_input("Translate extracted target string sequence:", key="in_3").strip().upper()
    
    if st.button("BYPASS MEMORY FIREWALL 🔓", key="b_3"):
        if user_input == "CODE" or check_hash(user_input, "9a661b0a52df03aa6240292797e88f00072b49c001cbe3d007ec1dfb1b60f588"):
            st.session_state.stage = 4
            st.rerun()
        else:
            st.error("❌ Character Check Mismatch: Corruption signature detected inside bit tracking arrays.")
    st.markdown('</div>', unsafe_allow_html=True)

# =========================================================================
# CHALLENGE 4: THE PYTHON BUG HUNT
# =========================================================================
elif st.session_state.stage == 4:
    st.markdown('<div class="stage-card">', unsafe_allow_html=True)
    st.subheader("🐛 Challenge 4: Diagnostic Script Compilation Fix")
    st.write("The authentication loop checker program contains a missing punctuation syntax flaw. Patch the file script execution anomaly.")
    
    st.code("""
    def check_password(password)
        if len(password) < 8
            print("Password flagged: Weak security index profile.")
    """, language="python")
    
    user_input = st.text_input("Enter the single character token symbol missing from lines 1 and 2:", key="in_4").strip()
    
    if st.button("COMPILE SYNTAX OVERRIDE PATCH 🔓", key="b_4"):
        if user_input == ":" or check_hash(user_input, "76f0d14b4369a473468087920bb6148303f8fcb151bf99994c979cf7b198889a"):
            st.session_state.stage = 5
            st.rerun()
        else:
            st.error("❌ Script Error: Interpreter output returned a runtime compilation failure.")
    st.markdown('</div>', unsafe_allow_html=True)

# =========================================================================
# CHALLENGE 5: SQL DATA MODEL EXCLUSION
# =========================================================================
elif st.session_state.stage == 5:
    st.markdown('<div class="stage-card">', unsafe_allow_html=True)
    st.subheader("🗄️ Challenge 5: Database Query Isolation")
    st.write("The table schema contains an authentication block list. Identify the command keyword required to isolate unique un-duplicated records from data pools.")
    
    st.code("""
    SELECT ___________ client_ip FROM mainframe_security_logs;
    """, language="sql")
    
    user_input = st.text_input("Complete the missing SQL keyword pattern string:", key="in_5", placeholder="Keyword...").strip().upper()
    
    if st.button("EXECUTE STRUCTURED DATA QUERY 🔓", key="b_5"):
        if user_input == "DISTINCT" or check_hash(user_input, "601e3895bd97ff645e9987a0709b456db97f8c057692095b6a71e1f74463402e"):
            st.session_state.stage = 6
            st.rerun()
        else:
            st.error("❌ Command Exception: Syntax indexing returned duplicate row sets. Target isolated record query failed.")
    st.markdown('</div>', unsafe_allow_html=True)

# =========================================================================
# CHALLENGE 6: SUBNET ROUTING RESOLUTION
# =========================================================================
elif st.session_state.stage == 6:
    st.markdown('<div class="stage-card">', unsafe_allow_html=True)
    st.subheader("🌐 Challenge 6: Network Layer Protocol Mapping")
    st.write("To route the egress escape transmission packet outside the perimeter zone, confirm which networking layer core system protocol translates dynamic domain URL name links into structured numerical destination IP addresses.")
    
    user_input = st.text_input("Enter the 3-letter acronym designator string:", key="in_6", placeholder="e.g. FTP, SSL...").strip().upper()
    
    if st.button("TERMINATE ROOT ROUTING HANDSHAKE 🔓", key="b_6"):
        if user_input == "DNS" or check_hash(user_input, "e5b72195f22e700cf1cb765f606e10885e35e7df5d1bf25577609278065c711a"):
            st.session_state.stage = 7
            st.rerun()
        else:
            st.error("❌ Routing Failure: Destination resolving host name unverified.")
    st.markdown('</div>', unsafe_allow_html=True)

# =========================================================================
# MAINFRAME BREACH ESCAPE COMPLETE
# =========================================================================
elif st.session_state.stage == 7:
    st.balloons()
    st.markdown('<div class="stage-card" style="border-color: #a855f7; text-align: center;">', unsafe_allow_html=True)
    st.success("🎉 SYSTEM MAINFRAME ESCAPE SUCCESSFUL!")
    st.markdown("<h2 style='color:#00f3ff; font-family:\"Courier New\", monospace;'>[ACCESS GRANTED]</h2>", unsafe_allow_html=True)
    st.write("Fantastic work, Agent. You verified the circuitry maps, patched compiler errors, decoupled the query layer data logs, and routed the escape stream clean past the firewalls.")
    
    if st.button("RESET MATRIX NETWORK HANDSHAKER 🔁"):
        st.session_state.stage = 1
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
