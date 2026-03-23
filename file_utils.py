import PyPDF2
from docx import Document
import io

def extract_text(file):
    filename = file.name
    
    # Handle PDF
    if filename.endswith('.pdf'):
        pdf_reader = PyPDF2.PdfReader(file)
        text = ""
        for page in pdf_reader.pages:
            content = page.extract_text()
            if content:
                text += content + "\n"
        return text
    
    # Handle DOCX
    elif filename.endswith('.docx'):
        doc = Document(file)
        text = "\n".join([para.text for para in doc.paragraphs])
        return text
    
    # Handle TXT
    elif filename.endswith('.txt'):
        return str(file.read(), "utf-8")
    
    else:
        return None