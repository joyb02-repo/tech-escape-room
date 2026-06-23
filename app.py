import streamlit as st
import hashlib

# One-way hashing helper function to hide answers from source code
def check_hash(user_input, correct_hash):
    # Convert input to uppercase, remove spaces, and hash it
    scrambled_input = hashlib.sha256(user_input.strip().upper().encode()).hexdigest()
    return scrambled_input == correct_hash

# Set page configuration
st.set_page_config(page_title="Digital Escape Room", page_icon="🔐", layout="centered")

# Immersive dark theme CSS styling
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    h1 { color: #2ecc71; text-align: center; font-family: 'Courier New', monospace; }
    h3 { color: #00ff66; font-family: 'Courier New', monospace; }
    .stButton>button {
        background-color: #1f2937; color: #00ff66; 
        border: 2px solid #00ff66; font-family: 'Courier New', monospace;
        width: 100%; transition: 0.3s;
    }
    .stButton>button:hover { background-color: #00ff66; color: #0e1117; }
    </style>
""", unsafe_allow_html=True)

if "stage" not in st.session_state:
    st.session_state.stage = 1

st.title("⚡ DIGITAL TECH ESCAPE ROOM")
st.write("---")

# =========================================================================
# STAGE 1: THE CRYPTOGRAM
# =========================================================================
if st.session_state.stage == 1:
    st.header("🔒 Stage 1: The Cryptogram")
    st.write("An anonymous hacker left an encrypted message. Break the cipher to discover the secret access word.")
    
    st.code("""
    Cipher text: X S B   P S Q O W   G T   W S Q O T H U   G S P   S Q P P T H U 
    
    Hint Table: X=T, S=H, B=E, P=P, O=O, W=W, G=S, T=I, U=G, H=N
    """, language="text")
    
    user_input = st.text_input("Enter the decoded second word:", key="stage1_input")
    
    if st.button("Submit Code 🔑", key="btn1"):
        # Scrambled fingerprint of "POWER"
        if check_hash(user_input, "2f8263cf8bb82ec7da117c2be6d11a8080f83359d48b1116c905327b73840e79"):
            st.session_state.stage = 2
            st.rerun()
        else:
            st.error("❌ Access Denied. The system remains locked.")

# =========================================================================
# STAGE 2: THE LOGIC GATE MAZE
# =========================================================================
elif st.session_state.stage == 2:
    st.header("🧩 Stage 2: The Logic Gate Circuit")
    st.write("Trace the binary signals down through the network gates to evaluate the final system output state.")
    
    st.code("""
    [Input A: 1] ───┐
                    ├───► [ AND Gate ] ───┐
    [Input B: 0] ───┘                     │
                                          ├───► [ OR Gate ] ───► FINAL OUTPUT?
                                          │
    [Input C: 1] ───► [ NOT Gate ] ───────┘
    """, language="text")
    
    user_input = st.text_input("What is the final Output digit (0 or 1)?:", key="stage2_input")
    
    if st.button("Submit Signal 🔑", key="btn2"):
        # Scrambled fingerprint of "0"
        if check_hash(user_input, "5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9"):
            st.session_state.stage = 3
            st.rerun()
        else:
            st.error("❌ Circuit Overload! Wrong binary bit sequence.")

# =========================================================================
# STAGE 3: BINARY CODE BREAKER
# =========================================================================
elif st.session_state.stage == 3:
    st.header("💾 Stage 3: Raw Memory Dump")
    st.write("A hidden directory requires a 4-letter password string. Decipher these binary memory bytes.")
    
    st.code("""
    Byte 1: 01000011  |  Byte 2: 01001111  |  Byte 3: 01000100  |  Byte 4: 01000101
    """, language="text")
    st.markdown("*(Note: Capital letter 'A' starts at ASCII decimal value 65)*")
    
    user_input = st.text_input("Enter the 4-letter decoded password:", key="stage3_input")
    
    if st.button("Bypass Firewall 🔑", key="btn3"):
        # Scrambled fingerprint of "CODE"
        if check_hash(user_input, "9a661b0a52df03aa6240292797e88f00072b49c001cbe3d007ec1dfb1b60f588"):
            st.session_state.stage = 4
            st.rerun()
        else:
            st.error("❌ Invalid Character Stream string detected.")

# =========================================================================
# STAGE 4: THE PYTHON BUG HUNT
# =========================================================================
elif st.session_state.stage == 4:
    st.header("🐛 Stage 4: Debug the Mainframe")
    st.write("What single punctuation character is missing from lines 1 and 2 to make this python code valid?")
    
    st.code("""
    def check_password(password)
        if len(password) < 8
            print("Password too short!")
    """, language="python")
    
    user_input = st.text_input("Missing symbol:", key="stage4_input")
    
    if st.button("Execute Patch 🛠️", key="btn4"):
        # Scrambled fingerprint of ":"
        if check_hash(user_input, "76f0d14b4369a473468087920bb6148303f8fcb151bf99994c979cf7b198889a"):
            st.session_state.stage = 5
            st.rerun()
        else:
            st.error("❌ Compilation failure. Code bug is still present.")

# =========================================================================
# ESCAPE SUCCESS
# =========================================================================
elif st.session_state.stage == 5:
    st.balloons()
    st.success("🎉 ESCAPE SUCCESSFUL!")
    st.markdown("<h3 style='text-align: center;'>SYSTEM ACCESS RESTORED</h3>", unsafe_allow_html=True)
    
    if st.button("Reset System Simulator 🔁"):
        st.session_state.stage = 1
        st.rerun()
