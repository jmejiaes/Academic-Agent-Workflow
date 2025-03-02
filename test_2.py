import os
import uuid
import re
from phi.agent import Agent
from phi.model.openai import OpenAIChat
from phi.tools.googlesearch import GoogleSearch
from phi.tools.arxiv_toolkit import ArxivToolkit

# Crear un directorio único para esta ejecución usando un UUID
base_output_dir = str(uuid.uuid4())
os.makedirs(base_output_dir, exist_ok=True)
print(f"Directorio base de salida: {base_output_dir}")

# Agente para generar notas de clase extendidas (Markdown)
notes_agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    instructions=[
        "A partir del siguiente fragmento markdown que describe una clase, genera notas de clase extendidas en Markdown. "
        "Incluye una introducción detallada, explicación profunda de cada punto con ejemplos y una conclusión clara."
    ],
    markdown=True,
)

# Agente para generar los objetivos breves de la clase (Markdown)
objectives_agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    instructions=[
        "A partir del siguiente fragmento markdown que describe una clase, genera de manera breve los objetivos de la clase. "
        "Resume los puntos clave y lo que se pretende lograr, en formato Markdown."
    ],
    markdown=True,
)

# Agente para generar ejercicios tipo quiz con soluciones, a partir de las notas extendidas
quiz_agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    instructions=[
        "Utiliza las notas de clase extendidas (en Markdown) proporcionadas para generar un conjunto de ejercicios tipo quiz. "
        "Cada ejercicio debe incluir un enunciado, varias opciones y la solución correcta, todo formateado en Markdown."
    ],
    markdown=True,
)

# Agente para generar preguntas para discusión basadas en las notas extendidas
discussion_agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    instructions=[
        "A partir de las notas de clase extendidas (en Markdown) proporcionadas, genera preguntas para discusión que estimulen "
        "la reflexión y el debate sobre el contenido de la clase. Formatea las preguntas en Markdown."
    ],
    markdown=True,
)


# Agente que recomienda recursos de interés
resources_agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    tools=[GoogleSearch(), ArxivToolkit()],
    instructions=[
        "Eres un agente experto en recomendar recursos de interés para profundizar en temas académicos y técnicos.",
        "Dado el tema de una clase, recomienda 3 o 4 recursos relevantes, incluyendo blogs de Medium y papers de Arxiv.",
        "Para los blogs de Medium, utiliza Google Search para buscar posts recientes y de calidad. Para los papers, utiliza ArxivToolkit para buscar publicaciones académicas sobre el tema.",
        "Devuelve la respuesta en formato Markdown, enumerando cada recurso con su título, una breve descripción y el enlace correspondiente.",
    ],
    markdown=True,
    show_tool_calls=True,
)


# Leer el contenido del archivo Markdown generado previamente (output.md)
with open("output.md", "r", encoding="utf-8") as file:
    content = file.read()

# Dividir el contenido en fragmentos por cada clase usando el encabezado "## Clase"
classes = re.split(r'(?=## Clase)', content)

# Iterar sobre cada fragmento de clase
for index, class_markdown in enumerate(classes):
    if class_markdown.strip():
        print(f"\nProcesando Clase {index}...")
        
        # Crear un directorio para la clase dentro del directorio base
        class_dir = os.path.join(base_output_dir, f"clase_{index}")
        os.makedirs(class_dir, exist_ok=True)
        
        # Generar notas de clase extendidas
        notes_response = notes_agent.run(class_markdown)
        notes_content = notes_response.to_dict()["messages"][-1]["content"]
        notes_path = os.path.join(class_dir, "notes.md")
        with open(notes_path, "w", encoding="utf-8") as f:
            f.write(notes_content)
        print(f"Notas extendidas guardadas en: {notes_path}")
        
        # Generar objetivos breves de la clase
        objectives_response = objectives_agent.run(class_markdown)
        objectives_content = objectives_response.to_dict()["messages"][-1]["content"]
        objectives_path = os.path.join(class_dir, "objectives.md")
        with open(objectives_path, "w", encoding="utf-8") as f:
            f.write(objectives_content)
        print(f"Objetivos guardados en: {objectives_path}")
        
        # Generar ejercicios tipo quiz con soluciones usando las notas extendidas
        quiz_response = quiz_agent.run(notes_content)
        quiz_content = quiz_response.to_dict()["messages"][-1]["content"]
        quiz_path = os.path.join(class_dir, "quiz.md")
        with open(quiz_path, "w", encoding="utf-8") as f:
            f.write(quiz_content)
        print(f"Ejercicios tipo quiz guardados en: {quiz_path}")
        
        # Generar preguntas para discusión basadas en las notas extendidas
        discussion_response = discussion_agent.run(notes_content)
        discussion_content = discussion_response.to_dict()["messages"][-1]["content"]
        discussion_path = os.path.join(class_dir, "discussion.md")
        with open(discussion_path, "w", encoding="utf-8") as f:
            f.write(discussion_content)
        print(f"Preguntas para discusión guardadas en: {discussion_path}")

        # Recomendar recursos de interés basados en el tema de la clase
        resources_response = resources_agent.run(class_markdown)
        resources_content = resources_response.to_dict()["messages"][-1]["content"]
        resources_path = os.path.join(class_dir, "resources.md")
        with open(resources_path, "w", encoding="utf-8") as f:
            f.write(resources_content)
        print(f"Recursos recomendados guardados en: {resources_path}")

        print(f"\nProcesamiento de Clase {index} completado.")
    
print("\nProceso de generación de contenido finalizado.")
print(f"Directorio base de salida: {base_output_dir}")
