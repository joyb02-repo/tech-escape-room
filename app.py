import streamlit as st

# Set page configuration with an immersive dark theme/vibe
st.set_page_config(page_title="Digital Escape Room", page_icon="🔐", layout="centered")

# Custom CSS styling for the digital escape room atmosphere
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
    .success-text { color: #2ecc71; font-weight: bold; font-family: 'Courier New', monospace; }
    </style>
""", unsafe_allow_html=True)

# Initialize Session State for tracking progress
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
    
    st.info("💡 Hint: Decrypt the very first word (`X S B`) to confirm your pattern, then decode the second word (`P S Q O W`) for your access key!")
    
    user_input = st.text_input("Enter the decoded second word (All Caps):", key="stage1_input").strip().upper()
    
    if st.button("Submit Code 🔑", key="btn1"):
        # "P S Q O W" decodes to "POWER"
        if user_input == "POWER":
            st.session_state.stage = 2
            st.rerun()
        else:
            st.error("❌ Access Denied. The system remains locked. Check your cipher mapping.")

# =========================================================================
# STAGE 2: THE LOGIC GATE MAZE
# =========================================================================
elif st.session_state.stage == 2:
    st.header("🧩 Stage 2: The Logic Gate Circuit")
    st.write("The backup power grid layout is failing. Trace the binary signals down through the network gates to evaluate the final system output state.")
    
    st.code("""
    [Input A: 1] ───┐
                    ├───► [ AND Gate ] ───┐
    [Input B: 0] ───┘                     │
                                          ├───► [ OR Gate ] ───► FINAL OUTPUT?
                                          │
    [Input C: 1] ───► [ NOT Gate ] ───────┘
    """, language="text")
    
    st.markdown("""
    * **AND Gate:** Outputs `1` only if *both* inputs are 1.
    * **OR Gate:** Outputs `1` if *at least one* input is 1.
    * **NOT Gate:** Flips the incoming signal (`1` becomes `0`, `0` becomes `1`).
    """)
    
    user_input = st.text_input("What is the final Output digit (0 or 1)?:", key="stage2_input").strip()
    
    if st.button("Submit Signal 🔑", key="btn2"):
        if user_input == "0":
            st.session_state.stage = 3
            st.rerun()
        else:
            st.error("❌ Circuit Overload! Wrong binary bit sequence.")

# =========================================================================
# STAGE 3: BINARY CODE BREAKER
# =========================================================================
elif st.session_state.stage == 3:
    st.header("💾 Stage 3: Raw Memory Dump")
    st.write("A hidden directory requires a 4-letter password string. Decipher these binary memory bytes into readable characters.")
    
    st.code("""
    Byte 1: 01000011
    Byte 2: 01001111
    Byte 3: 01000100
    Byte 4: 01000101
    """, language="text")
    
    st.markdown("""
    **ASCII Translation Guide:**
    * `01000011` = 67 in decimal
    * `01001111` = 79 in decimal
    * `01000100` = 68 in decimal
    * `01000101` = 69 in decimal
    *(Note: Capital letter 'A' starts at value 65, 'B' is 66, 'C' is 67, etc.)*
    """)
    
    user_input = st.text_input("Enter the 4-letter decoded password:", key="stage3_input").strip().upper()
    
    if st.button("Bypass Firewall 🔑", key="btn3"):
        if user_input == "CODE":
            st.session_state.stage = 4
            st.rerun()
        else:
            st.error("❌ Invalid Character Stream string detected.")

# =========================================================================
# STAGE 4: THE PYTHON BUG HUNT
# =========================================================================
elif st.session_state.stage == 4:
    st.header("🐛 Stage 4: Debug the Mainframe")
    st.write("The lock mechanism code contains a structural syntax error. Find out what missing character is breaking the program execution.")
    
    st.code("""
    def check_password(password)
        if len(password) < 8
            print("Password too short!")
        else:
            print("Password secure.")
    """, language="python")
    
    user_input = st.text_input("What single punctuation character is missing from lines 1 and 2?", key="stage4_input").strip()
    
    if st.button("Execute Patch 🛠️", key="btn4"):
        if user_input == ":":
            st.session_state.stage = 5
            st.rerun()
        else:
            st.error("❌ Compilation failure. The bug is still crashing the lock sequence.")

# =========================================================================
# ESCAPE SUCCESS
# =========================================================================
elif st.session_state.stage == 5:
    st.balloons()
    st.success("🎉 ESCAPE SUCCESSFUL!")
    st.markdown("<h3 style='text-align: center;'>SYSTEM ACCESS RESTORED</h3>", unsafe_allow_html=True)
    st.write("Congratulations! You bypassed all firewall barriers, traced the circuits, corrected the script syntax flaws, and cracked the room!")
    
    if st.button("Reset System Simulator 🔁"):
        st.session_state.stage = 1
        st.rerun()