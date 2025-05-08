import fitz  # PyMuPDF - used for working with pdf files
import tempfile

def extract_text_from_pdf(uploaded_file):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_file.read())
        tmp_path = tmp_file.name

    text = ""                                           #extracts content form pdf 
    with fitz.open(tmp_path) as doc:
        for page in doc:
            text += page.get_text()
    return text
