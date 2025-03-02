import os
import numpy as np
from phi.agent import Agent
from phi.model.openai import OpenAIChat
from phi.tools.googlesearch import GoogleSearch
from phi.embedder.openai import OpenAIEmbedder

# Inicializamos los agentes:
# Agente 1: Resume el contenido de las notas de clase.
summary_agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    instructions=[
        "Lee el siguiente contenido de notas de clase y genera un breve resumen en pocas oraciones que capture los puntos clave."
    ],
    markdown=False,
)

# Agente 2: Extrae el título y, a partir de él, realiza una búsqueda en Google y resume la información encontrada.
google_agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    tools=[GoogleSearch()],
    instructions=[
        "A partir del siguiente título, realiza una búsqueda en Google para encontrar información relevante sobre el tema y resume la información en pocas oraciones."
    ],
    markdown=False,
)

# Inicializamos el embedder de OpenAI para generar los embeddings.
embedder = OpenAIEmbedder(model="text-embedding-ada-002")

# Directorio base que contiene las carpetas de cada clase
base_dir = "06a9d41b-e91b-4ad0-8ceb-ca459964711f"

# Diccionario para almacenar los resultados
evaluation_results = {}

# Iteramos sobre cada carpeta de clase (se asume que su nombre empieza con "clase_")
for clase in sorted(os.listdir(base_dir)):
    class_dir = os.path.join(base_dir, clase)
    notes_path = os.path.join(class_dir, "notes.md")
    if os.path.exists(notes_path):
        with open(notes_path, "r", encoding="utf-8") as f:
            notes_content = f.read()
        
        # 1. Agente que resume las notas (resumen_agentes)
        summary_response = summary_agent.run(notes_content)
        resumen_agentes = summary_response.to_dict()["messages"][-1]["content"].strip()
        
        # 2. Extraer el título de la clase de la primera línea del archivo.
        lines = notes_content.splitlines()
        if lines:
            # Se espera un formato similar a: "# Notas de Clase: <Título>"
            first_line = lines[0]
            if ":" in first_line:
                title = first_line.split(":", 1)[1].strip()
            else:
                title = first_line.strip()
        else:
            title = "Tema Desconocido"
        
        # 3. Agente que busca en Google a partir del título y resume la información (resumen_google)
        google_response = google_agent.run(title)
        resumen_google = google_response.to_dict()["messages"][-1]["content"].strip()
        
        # 4. Obtener embeddings de ambos resúmenes y calcular la similitud coseno.
        # Nota: embedder.embed espera una lista de textos.
        embedding_agent = embedder.get_embedding(resumen_agentes)
        embedding_google = embedder.get_embedding(resumen_google)
        vec1 = np.array(embedding_agent[0])
        vec2 = np.array(embedding_google[0])
        cosine_similarity = float(np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2)))
        
        # Almacenar resultados en el diccionario
        evaluation_results[clase] = {
            "cosine similarity": cosine_similarity,
            "resumen_agentes": resumen_agentes,
            "resumen_google": resumen_google
        }
        
        print("\nResumen de agentes:", resumen_agentes)
        print("Resumen de Google:", resumen_google)
        print(f"Evaluación para {clase}: similitud coseno = {cosine_similarity:.4f}")
        exit()

# Mostrar resultados finales
print("\nResultados de Evaluación:")
for clase, result in evaluation_results.items():
    print(f"{clase}: {result}")
