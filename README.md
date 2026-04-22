# 🔐 Advanced Encryption Tool

## 🎓 Internship Project

This project was developed as part of my **Cybersecurity Internship at CodTech (Task 4)**.

It demonstrates secure file encryption and decryption using modern cryptographic techniques along with a user-friendly interface.


A secure and user-friendly file encryption and decryption tool built using Python and Streamlit. This project uses strong cryptographic techniques to ensure data confidentiality and integrity.

---

## 🚀 Features

- 🔑 **Strong Key Management**
  - PBKDF2 with salt and 100,000+ iterations
- 🔐 **AES-based Encryption (Fernet)**
- 📁 **Secure File Handling**
  - File metadata protection
  - Automatic `.enc` file generation
  - Overwrite protection
- 📂 **Folder Encryption Support**
- 📜 **Logging System**
  - Tracks encryption, decryption, and errors
- 🖥️ **Modern UI (Streamlit Dashboard)**
- 🔑 **Password-Protected Encryption**

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Cryptography Library

---

## 📦 Installation

1. Clone the repository:e https://github.com/mehakstudio-png/advanced-encryption-tool.git


2. Create virtual environment:python -m venv venv
venv\Scripts\activate


3. Install dependencies:pip install -r requirements.txt


---

## ▶️ Run the Application

---

## 🧪 How It Works

### 🔒 Encryption
- Upload a file
- Enter password
- File is encrypted and saved as `.enc`

### 🔓 Decryption
- Upload `.enc` file
- Enter same password
- Original file is restored

---

## 🔐 Security Features

- PBKDF2 key derivation (secure against brute-force attacks)
- Random salt generation
- Encrypted file packaging (metadata + encrypted data)
- Password is never stored
- Integrity protection using Fernet encryption

---

---

## ⚠️ Important Notes

- Use strong passwords for better security
- Password cannot be recovered if lost
- Do not modify `.enc` files manually

---

## 👩‍💻 Author

**Mehak**  
Cybersecurity Intern (CodTech)

---

## ⭐ Future Improvements

- Download button in UI
- Password strength indicator
- Drag & drop improvements
- Convert to executable (.exe)

---

## 📜 License

This project is for educational and internship purposes.
