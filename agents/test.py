import os
import uuid
from phi.agent import Agent
from phi.model.openai import OpenAIChat
from phi.model.ollama import Ollama

# Configuración de agentes
modelo_local = Ollama(id="deepseek-r1")
modelo_openai = OpenAIChat(id="gpt-4o")

# Agentes

# Agente de prueba
organizer = Agent(
    model=modelo_local,
    markdown=True
)

def generate_contents(text):
    """
    Genera contenido en Markdown a partir de un texto que describe capítulos y títulos
    por cada capítulo
    args:
        text (str): Texto que describe capítulos y títulos
    returns:
        None
    """
    # Crear un directorio único para esta ejecución usando un UUID
    output_path: str = 'generated-'+str(uuid.uuid4())
    base_output_dir = '../outputs/' + output_path
    os.makedirs(base_output_dir, exist_ok=True)
    print(f"Directorio base de salida: {base_output_dir}")

    organizer_response = organizer.run(text)
    organizer_content = organizer_response.to_dict()["messages"][-1]["content"]
    organizer_path = os.path.join(base_output_dir, "output.md")

    with open(organizer_path, "w", encoding="utf-8") as f:
        f.write(organizer_content)

    print(f"Output guardadas en: {organizer_path}")
    print(f"Directorio base de salida: {base_output_dir}")

    print("\nProceso de generación de contenido finalizado.")

    return output_path
