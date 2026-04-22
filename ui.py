import streamlit as st
import os
from encrypt import encrypt_file
from decrypt import decrypt_file

st.set_page_config(page_title="🔐 Encryption Tool", layout="centered")

st.title("🔐 Advanced Encryption Tool")

menu = ["Encrypt File", "Decrypt File", "Encrypt Folder"]
choice = st.sidebar.selectbox("Select Option", menu)

st.sidebar.markdown("---")
st.sidebar.info("Secure AES-based File Encryption Tool")

# ---------------- ENCRYPT FILE ----------------
if choice == "Encrypt File":
    st.header("📁 Encrypt a File")

    uploaded_file = st.file_uploader("Choose a file")

    password = st.text_input("Enter Password", type="password")

    if st.button("Encrypt"):
        if uploaded_file and password:
            file_path = os.path.join("temp_" + uploaded_file.name)

            with open(file_path, "wb") as f:
                f.write(uploaded_file.read())

            encrypt_file(file_path, password)

            st.success("✅ File Encrypted Successfully!")

        else:
            st.error("⚠️ Please provide file and password")

# ---------------- DECRYPT FILE ----------------
elif choice == "Decrypt File":
    st.header("🔓 Decrypt a File")

    uploaded_file = st.file_uploader("Upload .enc file")

    password = st.text_input("Enter Password", type="password")

    if st.button("Decrypt"):
        if uploaded_file and password:
            file_path = os.path.join("temp_" + uploaded_file.name)

            with open(file_path, "wb") as f:
                f.write(uploaded_file.read())

            decrypt_file(file_path, password)

            st.success("✅ File Decrypted Successfully!")

        else:
            st.error("⚠️ Please provide file and password")

# ---------------- ENCRYPT FOLDER ----------------
elif choice == "Encrypt Folder":
    st.header("📂 Encrypt Folder")

    folder_path = st.text_input("Enter Folder Path")

    password = st.text_input("Enter Password", type="password")

    if st.button("Encrypt Folder"):
        if folder_path and password:
            if os.path.exists(folder_path):
                from main import encrypt_folder
                encrypt_folder(folder_path, password)

                st.success("✅ Folder Encrypted Successfully!")
            else:
                st.error("❌ Invalid folder path")
        else:
            st.error("⚠️ Enter folder path and password")