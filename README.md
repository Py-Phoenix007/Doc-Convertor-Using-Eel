# 🌟 Doc ↔ PDF Converter

**A dynamic, Python-driven document transformation tool** that seamlessly converts DOCX to PDF and PDF to DOCX with a single click, all wrapped in a stunning, user-friendly graphical interface. Crafted with Python, Eel, HTML/CSS, JavaScript, and a spark of innovation 🔥.

---

## 🚀 Project Overview

Say goodbye to clunky software and unreliable online converters! **Doc ↔ PDF Converter** is your all-in-one, offline solution for effortless document conversion. Designed for speed, simplicity, and style, this tool empowers students, professionals, and creators to transform documents with ease.

### Why Choose Doc ↔ PDF Converter?

- 🖥 **Offline Powerhouse**: No internet? No problem! Convert files locally with confidence.
- 🔄 **Bidirectional Conversion**: Seamlessly switch between `.docx` and `.pdf` formats.
- 🎨 **Elegant Interface**: A responsive, web-based GUI that’s as beautiful as it is intuitive.
- ⚡ **Lightning Fast**: Optimized for performance, delivering results in seconds.
- 🌍 **Cross-Platform Ready**: Works on Windows, with partial support for other platforms.

---

## ✨ Key Features

- ✅ Convert `.docx` to `.pdf` with precision
- ✅ Convert `.pdf` to `.docx` effortlessly
- ✅ Sleek, modern GUI powered by HTML, CSS, and JavaScript
- ✅ Robust Python backend for reliable processing
- ✅ Fully offline after setup for maximum privacy
- ✅ Intuitive design, perfect for beginners and pros alike

---

## 📂 Project Structure

```plaintext
📦 document-converter/
├── 🧠 main.py                    # Core Python logic with Eel integration
├── 📁 templates/                # Frontend templates
│   └── index.html               # Main GUI page
├── 📁 static/                   # Static assets
│   ├── style.css                # Stylish CSS for the GUI
│   ├── main.js                  # JavaScript for frontend interactivity
│   └── demo-screenshot.png      # Optional preview image
├── 📁 uploads/                  # Temporary storage for uploaded files
└── 📄 README.md                 # This file
```

---

## 🔧 Technology Stack

- **Python**: The backbone of the application
- **Eel**: Bridges Python with a modern web-based GUI
- **HTML/CSS/JavaScript**: Powers the responsive frontend
- **docx2pdf**: Handles DOCX to PDF conversion (Windows only)
- **pdf2docx**: Enables PDF to DOCX conversion

---

## 📦 Installation Guide

Get up and running in minutes:

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/yourusername/document-converter.git
   cd document-converter
   ```

2. **Install Dependencies**:

   ```bash
   pip install eel python-docx docx2pdf pdf2docx
   ```

   > ⚠️ **Note**: `docx2pdf` requires Microsoft Word and is Windows-only.

3. **(Optional) Set Up a Virtual Environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

---

## ⚙️ How to Use

1. **Launch the Application**:

   ```bash
   python main.py
   ```

2. **Convert Files**:

   - Upload a `.docx` or `.pdf` file via the GUI
   - Select your desired conversion type
   - Click **Convert**
   - Download your converted file instantly

---

## 🧠 How It Works

- **File Handling**: Uploaded files are temporarily stored in the `/uploads` folder.
- **Conversion Logic**: The `main.py` script orchestrates conversions using `docx2pdf` and `pdf2docx`.
- **Output Delivery**: Converted files are saved in the `/static` folder and available for download via the GUI.

---

## 📜 License

This project is licensed under the **MIT License**. Feel free to use, modify, and share it as you see fit!

---

## 🙌 Acknowledgments

- **Eel**: Thanks to Chris Knott for enabling seamless Python-HTML integration
- **docx2pdf & pdf2docx**: For robust document conversion libraries
- **Icons8**: For providing stunning icons
- **Community**: Inspired by the need for simple, offline productivity tools

---

## 💬 Get Involved

Have ideas for new features or improvements?

- 📧 Reach out via email or GitHub Issues
- 🤝 Connect on LinkedIn for collaboration opportunities
- ⭐ Star the repo to show your support!

---

> **Doc ↔ PDF Converter**: Engineered to simplify your workflow, amplify productivity, and bring a touch of elegance to document conversion.\
> Built with Python, creativity, and a passion for innovation.
