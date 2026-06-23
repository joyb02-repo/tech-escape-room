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
    
    # Force clean input right at the widget layer
    user_input = st.text_input("Decrypt key word payload:", key="in_1", placeholder="Type POWER here...").strip().upper()
    
    if st.button("EXECUTE HANDSHAKE UNLOCK 🔓", key="b_1"):
        # Hard check both the hash AND a plaintext backup check just in case your server python environment is hashing differently!
        if user_input == "POWER" or check_hash(user_input, "2f8263cf8bb82ec7da117c2be6d11a8080f83359d48b1116c905327b73840e79"):
            st.session_state.stage = 2
            st.rerun()
        else:
            st.error(f"❌ Handshake Rejected: '{user_input}' is an invalid encryption signature.")
            
    st.markdown('</div>', unsafe_allow_html=True)
