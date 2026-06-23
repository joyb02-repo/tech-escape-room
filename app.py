import streamlit as st
import hashlib

# One-way hashing checker engine
def check_hash(user_input, correct_hash):
    scrambled_input = hashlib.sha256(user_input.strip().upper().encode()).hexdigest()
    return scrambled_input == correct_hash

# Page setup
st.set_page_config(page_title="Cyber Defense Escape Room", page_icon="⚡", layout="centered")

# Sleek, unified modern terminal styling
st.markdown("""
    <style>
    /* Dark Minimalist Background */
    .stApp {
        background-color: #0b0f17;
    }
    
    /* Neon Terminal Typography */
    .terminal-title {
        color: #00f3ff;
        font-family: 'Courier New', monospace;
        text-align: center;
        font-weight: 800;
        text-shadow: 0 0 10px rgba(0, 243, 255, 0.3);
        margin-bottom: 2px;
    }
    .terminal-subtitle {
        color: #788296;
        font-family: -apple-system, BlinkMacSystemFont, sans-serif;
        text-align: center;
        font-size: 13px;
        margin-bottom: 20px;
    }
    
    /* Force Streamlit's native container to match our dark glassmorphic layout */
    div[data-testid="stVerticalBlockBorderWithDetails"] {
        background-color: rgba(17, 24, 39, 0.85) !important;
        border: 1px solid rgba(0, 243, 255, 0.25) !important;
        border-radius: 12px !important;
        padding: 26px !important;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.5) !important;
    }
    
    /* Navigation Step Progress Badges */
    .progress-banner {
        display: flex;
        justify-content: space-between;
        gap: 6px;
        margin-bottom: 25px;
        font-family: 'Courier New', monospace;
        font-size: 11px;
    }
    .progress-node {
        flex: 1;
        text-align: center;
        padding: 6px 4px;
        border-radius: 6px;
        background: #141b29;
        color: #4b5563;
        border: 1px solid #1f2937;
    }
    .progress-node.active {
        background: rgba(0, 243, 255, 0.1);
        color: #00f3ff;
        border: 1px solid #00f3ff;
        box-shadow: 0 0 8px rgba(0, 243, 255, 0.15);
    }
    .progress-node.complete {
        background: rgba(168, 85, 247, 0.08);
        color: #a855f7;
        border: 1px solid rgba(168, 85, 247, 0.4);
    }

    /* Vibrant UI Custom Buttons */
    .stButton>button {
        background: linear-gradient(90deg, #00f3ff 0%, #a855f7 100%) !important;
        color: #000000 !important;
        font-weight: 700 !important;
        letter-spacing: 0.5px !important;
        border: none !important;
        border-radius: 6px !important;
        padding: 10px 20px !important;
        font-family: 'Courier New', monospace !important;
        width: 100% !important;
        transition: all 0.2s ease-in-out !important;
    }
    .stButton>button:hover {
        transform: translateY(-1px) !important;
        box-shadow: 0 4px 15px 0 rgba(168, 85, 247, 0.4) !important;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize game stage configuration 
if "stage" not in st.session_state:
    st.session_state.stage = 1

# Header Identity Elements
st.markdown('<h1 class="terminal-title">⚡ MAINFRAME BREACH</h1>', unsafe_allow_html=True)
st.markdown('<p class="terminal-subtitle">Secured Security Architecture Diagnostic Suite v3.2.6</p>', unsafe_allow_html=True)

# Navigation Step Progress Bar
nodes = ["Cryptogram", "Circuitry", "Binary", "Debugging", "Data Schema", "Network"]
banner_html = '<div class="progress-banner">'
for i, name in enumerate(nodes, 1):
    status_class = "progress-node"
    if st.session_state.stage == i:
        status_class += " active"
    elif st.session_state.stage > i:
        status_class += " complete"
    banner_html += f'<div class="{status_class}">S{i}</div>'
banner_html += '</div>'
st.markdown(banner_html, unsafe_allow_html=True)


# =========================================================================
# CENTRALIZED SECURE CONTAINER 
# All challenge activity renders directly inside this unified element
# =========================================================================
with st.container(border=True):

    # CHALLENGE 1
    if st.session_state.stage == 1:
        st.subheader("🔒 Challenge 1: Cipher Matrix Decryption")
        st.write("An anonymous proxy node left an encrypted intercept packet. Reconstruct the alphabet mapping array.")
        st.code("""
Cipher text: X S B   P S Q O W   G T   W S Q O T H U   G S P   S Q P P T H U 

Decoder Array: X=T, S=H, B=E, P=P, O=O, W=W, G=S, T=I, U=G, H=N
        """, language="text")
        st.caption("🔍 Strategy: Decode the second word string block (`P S Q O W`) to find the bypass key.")
        
        user_input = st.text_input("Decrypt key word payload:", key="in_1", placeholder="Type response here...").strip().upper()
        if st.button("EXECUTE HANDSHAKE UNLOCK 🔓", key="b_1"):
            if user_input == "POWER" or check_hash(user_input, "2f8263cf8bb82ec7da117c2be6d11a8080f83359d48b1116c905327b73840e79"):
                st.session_state.stage = 2
                st.rerun()
            else:
                st.error("❌ Handshake Rejected: Invalid encryption signature decryption.")

    # CHALLENGE 2
    elif st.session_state.stage == 2:
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
        
        user_input = st.text_input("Enter the terminal bit registry output value (0 or 1):", key="in_2").strip()
        if st.button("VERIFY VOLTAGE LOGIC 🔓", key="b_2"):
            if user_input == "0" or check_hash(user_input, "5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9"):
                st.session_state.stage = 3
                st.rerun()
            else:
                st.error("❌ Logic Check Fault: Circuit configuration loop detected.")

    # CHALLENGE 3
    elif st.session_state.stage == 3:
        st.subheader("💾 Challenge 3: Core Hex/Binary Memory Trace")
        st.write("The secondary firewall folder requires a 4-character ASCII access string phrase. Extract the hidden bytes:")
        st.code("""
Registers: [01000011]  [01001111]  [01000100]  [01000101]
        """, language="text")
        st.caption("💡 Reference Dictionary: Decimal equivalents: 67, 79, 68, 69. (Note: Upper-case letter 'A' matches index 65)")
        
        user_input = st.text_input("Translate extracted target string sequence:", key="in_3").strip().upper()
        if st.button("BYPASS MEMORY FIREWALL 🔓", key="b_3"):
            if user_input == "CODE" or check_hash(user_input, "9a661b0a52df03aa6240292797e88f00072b49c001cbe3d007ec1dfb1b60f588"):
                st.session_state.stage = 4
                st.rerun()
            else:
                st.error("❌ Character Check Mismatch: Corruption signature detected inside tracking arrays.")

    # CHALLENGE 4
    elif st.session_state.stage == 4:
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

    # CHALLENGE 5
    elif st.session_state.stage == 5:
        st.subheader("🗄️ Challenge 5: Database Query Isolation")
        st.write("The table schema contains an authentication block list. Identify the command keyword required to isolate unique un-duplicated records.")
        st.code("""
SELECT ___________ client_ip FROM mainframe_security_logs;
        """, language="sql")
        
        user_input = st.text_input("Complete the missing SQL keyword pattern string:", key="in_5", placeholder="Keyword...").strip().upper()
        if st.button("EXECUTE STRUCTURED DATA QUERY 🔓", key="b_5"):
            if user_input == "DISTINCT" or check_hash(user_input, "601e3895bd97ff645e9987a0709b456db97f8c057692095b6a71e1f74463402e"):
                st.session_state.stage = 6
                st.rerun()
            else:
                st.error("❌ Command Exception: Syntax indexing returned duplicate row sets.")

    # CHALLENGE 6
    elif st.session_state.stage == 6:
        st.subheader("🌐 Challenge 6: Network Layer Protocol Mapping")
        st.write("Confirm which networking layer core system protocol translates dynamic domain URL name links into structured numerical destination IP addresses.")
        
        user_input = st.text_input("Enter the 3-letter acronym designator string:", key="in_6", placeholder="e.g. FTP, SSL...").strip().upper()
        if st.button("TERMINATE ROOT ROUTING HANDSHAKE 🔓", key="b_6"):
            if user_input == "DNS" or check_hash(user_input, "e5b72195f22e700cf1cb765f606e10885e35e7df5d1bf25577609278065c711a"):
                st.session_state.stage = 7
                st.rerun()
            else:
                st.error("❌ Routing Failure: Destination resolving host name unverified.")

    # ESCAPE SUCCESS TERMINAL
    elif st.session_state.stage == 7:
        st.balloons()
        st.markdown("<h3 style='color:#00f3ff; font-family:\"Courier New\", monospace; text-align: center;'>[🎉 ACCESS GRANTED]</h3>", unsafe_allow_html=True)
        st.write("Fantastic work, Agent. You verified the circuitry maps, patched compiler errors, decoupled the query layer data logs, and successfully broke out of the mainframe.")
        
        if st.button("RESET MATRIX NETWORK HANDSHAKER 🔁"):
            st.session_state.stage = 1
            st.rerun()
