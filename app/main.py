import streamlit as st
import fitz  # PyMuPDF
import docx  # python-docx
import os
import sys

# Ajusta la ruta del sistema para incluir el directorio padre
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from agents.agents import generate_contents

ENVIRONMENT = 'local'
is_generated = False

# Cargar archivo Markdown
def write_data(file_path):
    print('-----------------------file_path', file_path)
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

# Cargar archivo PDF
def load_pdf(file):
    """
    Carga un archivo PDF y devuelve su contenido como texto
    args:
        - file (file): Archivo PDF
    returns:
        - text (str): Contenido del archivo
    """
    pdf_document = fitz.open(stream=file.read(), filetype="pdf")
    text = ""
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        text += page.get_text()
    return text

# Cargar archivo DOCX
def load_docx(file):
    """
    Carga un archivo DOCX y devuelve su contenido como texto
    args:
        file (file): Archivo DOCX
    returns:
        text (str): Contenido del archivo
    """
    doc = docx.Document(file)
    text = ""
    for paragraph in doc.paragraphs:
        text += paragraph.text + "\n"
    return text

def main():
    # Just add a simple title
    st.title("ACOCO")
    st.write("Automatic Course Content")

    # File uploader
    uploaded_file = st.file_uploader("Choose a text file", type="txt, pdf, docx")

    # Check for the file
    if uploaded_file is not None:
        file_extension = uploaded_file.name.split(".")[-1].lower()
        if file_extension == "txt":
            text = uploaded_file.read().decode("utf-8") # For txt files, we can directly read the content
        elif file_extension == "pdf":
            text = load_pdf(uploaded_file)
            st.text(text)
        elif file_extension == "docx":
            text = load_docx(uploaded_file)
            st.text(text)
        else:
            st.error("Unsupported file type")
            return
        st.write('File uploaded successfully, now thinking...')

        # Give the text to the agent
        response = generate_contents(text)

        # Display the path
        if ENVIRONMENT == 'local':
            response_path = response
        else:
            response_path = response.to_dict()["messages"][-1]["content"]
        
        # Display the response
        root_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        markdown_path = f'{root_folder}/outputs/{response_path}/output.md'
        markdown_content = write_data(markdown_path)
        
        # Display the content    
        st.markdown(markdown_content, unsafe_allow_html=True)
        st.markdown(f'> Puedes ver el resto del contenido generado en el folder: outputs/`{response_path}`')

if __name__ == "__main__":
    main()