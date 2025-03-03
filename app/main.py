import streamlit as st
import os
import sys

# Ajusta la ruta del sistema para incluir el directorio padre
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from agents.agents import generate_contents

ENVIRONMENT = 'local'
is_generated = False

# Cargar archivo Markdown
def load_markdown(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

def main():
    # Just add a simple title
    st.title("ACOCO")
    st.write("Automatic Course Content")

    # File uploader
    uploaded_file = st.file_uploader("Choose a text file", type="txt")

    # Check for the file
    if uploaded_file is not None:
        text = uploaded_file.read().decode("utf-8")
        st.write('File uploaded successfully, now thinking...')
        # Give the text to the agent
        response = generate_contents(text)
        if ENVIRONMENT == 'local':
            response_path = response
            st.write(response_path)
        else:
            response_path = response.to_dict()["messages"][-1]["content"]
        # Display the response
        # markdown_file = '../outputs/generated_ae0e59ee-d097-41fb-92e5-8adf96af714e/output.md'
        markdown_content = load_markdown('outputs/'+response_path+'/output.md')
        

        # Display the content    
        st.markdown(markdown_content, unsafe_allow_html=True)

if __name__ == "__main__":
    main()