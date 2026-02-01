import os
import PyPDF2

def load_pdfs(folder_path):
    documents = []
    doc_names = []

    for file in os.listdir(folder_path):
        if file.endswith(".pdf"):
            path = os.path.join(folder_path, file)
            with open(path, "rb") as f:
                reader = PyPDF2.PdfReader(f)
                text = ""
                for page in reader.pages:
                    text += page.extract_text() or ""

            documents.append(text)
            doc_names.append(file)

    return documents, doc_names
