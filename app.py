
import streamlit as st

def caesar_cipher(text, shift):
    result = ""

    for char in text:
        if char.isupper():
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            result += char

    return result


st.set_page_config(
    page_title="DecodeLabs | Cryptography",
    page_icon="🔐",
    layout="centered"
)

st.markdown("""
<style>
.stApp {
    background: #0B1220;
    color: #F4F0E6;
}
h1, h2, h3 {
    color: #D6B56D !important;
}
.stButton > button {
    background: #D6B56D;
    color: #101A2B;
    border-radius: 8px;
    border: none;
    font-weight: bold;
    width: 100%;
}
.stTextArea textarea {
    background: #17263D;
    color: #F4F0E6;
}
</style>
""", unsafe_allow_html=True)

st.title("DECODELABS")
st.subheader("Cryptography Intelligence")
st.caption("Basic Encryption & Decryption System")

st.divider()

operation = st.selectbox(
    "Select Operation",
    ["Encrypt Message", "Decrypt Message"]
)

message = st.text_area(
    "Enter Your Message",
    placeholder="Type your message here..."
)

shift = st.slider(
    "Select Shift Key",
    min_value=1,
    max_value=25,
    value=3
)

if st.button("PROCESS MESSAGE"):
    if message.strip():
        if operation == "Encrypt Message":
            result = caesar_cipher(message, shift)
            st.success("Encryption Completed")
        else:
            result = caesar_cipher(message, -shift)
            st.success("Decryption Completed")

        st.markdown("### Result")
        st.code(result)

    else:
        st.warning("Please enter a message first.")

st.divider()

st.caption(
    "DecodeLabs | Cybersecurity Project 2 | 2026"
)
