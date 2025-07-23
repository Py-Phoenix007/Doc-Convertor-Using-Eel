import eel
import os
import shutil
from pathlib import Path
from docx import Document
from docx2pdf import convert as docx2pdf_convert
from pdf2docx import Converter as PDF2DocxConverter

UPLOADS_DIR = Path("uploads")
OUTPUTS_DIR = Path("static")

os.makedirs(UPLOADS_DIR, exist_ok=True)
os.makedirs(OUTPUTS_DIR, exist_ok=True)


eel.init('templates', allowed_extensions=['.js', '.html', '.css'])

@eel.expose
def save_upload(filename, filedata):
    filepath = UPLOADS_DIR / filename
    # filedata is a list of ints from JS, convert to bytes
    with open(filepath, 'wb') as f:
        f.write(bytes(filedata))
    return str(filepath)

@eel.expose
def convert_file(filename, conversion_type):
    try:
        input_path = UPLOADS_DIR / filename
        output_filename = ''
        if conversion_type == 'doc2pdf':
            if not filename.lower().endswith((".doc", ".docx")):
                return {"success": False, "error": "Please upload a DOC or DOCX file."}
            output_filename = filename.rsplit('.', 1)[0] + '.pdf'
            output_path = OUTPUTS_DIR / output_filename
            docx2pdf_convert(str(input_path), str(output_path))
        elif conversion_type == 'pdf2doc':
            if not filename.lower().endswith(".pdf"):
                return {"success": False, "error": "Please upload a PDF file."}
            output_filename = filename.rsplit('.', 1)[0] + '.docx'
            output_path = OUTPUTS_DIR / output_filename
            cv = PDF2DocxConverter(str(input_path))
            cv.convert(str(output_path), start=0, end=None)
            cv.close()
        else:
            return {"success": False, "error": "Invalid conversion type."}
        return {"success": True, "output_file": output_filename}
    except Exception as e:
        return {"success": False, "error": str(e)}

def main():
    eel.start('index.html', mode='edge', size=(500, 500))

if __name__ == "__main__":
    main()
