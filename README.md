# 🌀 Px - Doc ↔ PDF Converter

**A sleek Python-powered document converter** that transforms your DOCX to PDF and PDF to DOCX in just a click — all through a clean and responsive graphical interface. Built using Python, Eel, HTML/CSS, and love ❤️.

---

## 🚀 Overview

Tired of jumping between bulky apps or online tools just to convert a document?

**Doc ↔ PDF Converter** is your minimalist solution:
- 🖥 Runs locally, no internet required  
- 🧩 Converts between `.docx` and `.pdf`  
- 🎨 Comes with a beautiful, intuitive web-based GUI  
- ⚡ Lightweight and fast

> Ideal for students, writers, professionals, or anyone needing quick, offline conversions.

---

## ✨ Features

✅ Convert `.doc` / `.docx` ➡️ `.pdf`  
✅ Convert `.pdf` ➡️ `.docx`  
✅ Clean, responsive frontend (HTML/CSS + JS)  
✅ Fast backend processing using Python libraries  
✅ Works offline after setup  
✅ Beginner-friendly UI

---

## 🖼 GUI Preview

> Here's what the interface looks like:

![Demo Screenshot](static/demo-screenshot.png)  
<sub>📝 Add your own screenshot and save it as `static/demo-screenshot.png`</sub>

---

## 📁 Folder Structure

📦 document-converter/ ├── 🧠 main.py                # Python backend with Eel ├── 📁 templates/ │   └── index.html           # GUI HTML page ├── 📁 static/ │   ├── style.css            # Beautiful styling │   ├── main.js              # Frontend logic via JavaScript │   └── demo-screenshot.png  # Optional preview image ├── 📁 uploads/               # Temporary folder for user uploads └── 📄 README.md              # You’re reading it!

---

## 🔧 Tech Stack

- **Python** — the powerhouse
- **Eel** — for bridging Python with a frontend GUI
- **HTML + CSS + JS** — frontend design
- **docx2pdf** — for DOCX ➡️ PDF (Windows only)
- **pdf2docx** — for PDF ➡️ DOCX

---

## 📦 Installation

1. **Clone the repo:**

```bash
git clone https://github.com/yourusername/document-converter.git
cd document-converter

2. Install dependencies:



pip install eel python-docx docx2pdf pdf2docx

> ⚠️ docx2pdf requires Microsoft Word and works only on Windows.




---

⚙️ Usage

1. Run the app:



python main.py

2. Convert your file:



Upload a .docx or .pdf file

Choose conversion type

Click "Convert"

Download your file instantly



---

🧠 Behind the Scenes

Files are saved temporarily in /uploads

Conversion logic is handled by main.py

Results are saved in /static, ready for download



---

❗ Limitations

Feature	Support

.docx ➡️ .pdf	✅ (Windows + MS Word only)
.pdf ➡️ .docx	✅
.doc ➡️ .pdf	⚠️ Limited support



---

📜 License

This project is licensed under the MIT License – feel free to use and build on it.


---

🙌 Credits

🧠 Eel by Chris Knott

📄 docx2pdf

📑 pdf2docx

🎨 Icons by Icons8

💡 Inspiration: Simplicity and productivity tools



---

💬 Let's Connect

Feel free to reach out or connect on LinkedIn if you'd like to collaborate or suggest features!


---

> Built to save time, boost productivity, and eliminate the hassle of online converters.
— Made with Python, passion, and a pinch of creativity.
