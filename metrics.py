import os
import json
import numpy as np
from phi.agent import Agent
from phi.model.openai import OpenAIChat
from phi.tools.googlesearch import GoogleSearch
from phi.embedder.openai import OpenAIEmbedder

# Para métricas adicionales:
from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction
from rouge_score import rouge_scorer
from bert_score import score as bert_score

# Agente 1: Resume el contenido completo de las notas.
summary_agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    instructions=[
        "Lee el siguiente contenido de notas de clase y genera un breve resumen en pocas oraciones que capture los puntos clave."
    ],
    markdown=False,
)

# Agente 2: A partir del título de la clase, busca en Google y resume la información encontrada.
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

# Directorio base que contiene las carpetas de cada clase.
base_dir = "06a9d41b-e91b-4ad0-8ceb-ca459964711f"

# Diccionario para almacenar los resultados de evaluación.
evaluation_results = {}

def evaluate_summaries(summary1, summary2, vec1, vec2):
    results = {}
    # 1. Similaridad coseno.
    cosine_similarity = float(np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2)))
    results["cosine similarity"] = cosine_similarity

    # 2. Distancia Euclidiana.
    results["euclidean distance"] = float(np.linalg.norm(vec1 - vec2))

    # 3. Distancia Manhattan.
    results["manhattan distance"] = float(np.sum(np.abs(vec1 - vec2)))

    # 4. Métricas ROUGE (usamos ROUGE-1, ROUGE-2 y ROUGE-L F1).
    scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL'], use_stemmer=True)
    rouge_scores = scorer.score(summary1, summary2)
    results["rouge"] = {
        "rouge1": rouge_scores["rouge1"].fmeasure,
        "rouge2": rouge_scores["rouge2"].fmeasure,
        "rougeL": rouge_scores["rougeL"].fmeasure,
    }

    # 5. BLEU (utilizando nltk con suavizado).
    smoothie = SmoothingFunction().method4
    bleu_score = sentence_bleu([summary1.split()], summary2.split(), smoothing_function=smoothie)
    results["bleu"] = bleu_score

    # 6. BERTScore (F1 promedio).
    P, R, F1 = bert_score([summary1], [summary2], lang="en", verbose=False)
    results["bert_score_f1"] = F1[0].item()

    return results

# Iterar sobre cada carpeta de clase (se asume que su nombre empieza con "clase_").
for clase in sorted(os.listdir(base_dir)):
    class_dir = os.path.join(base_dir, clase)
    notes_path = os.path.join(class_dir, "notes.md")
    if os.path.exists(notes_path):
        with open(notes_path, "r", encoding="utf-8") as f:
            notes_content = f.read()

        # 1. Obtener resumen de las notas completo (resumen_agentes).
        summary_response = summary_agent.run(notes_content)
        resumen_agentes = summary_response.to_dict()["messages"][-1]["content"].strip()

        # 2. Extraer el título de la clase (se asume formato: "# Notas de Clase: <Título>").
        lines = notes_content.splitlines()
        if lines:
            first_line = lines[0]
            if ":" in first_line:
                title = first_line.split(":", 1)[1].strip()
            else:
                title = first_line.strip()
        else:
            title = "Tema Desconocido"

        # 3. Obtener resumen basado en búsqueda de Google (resumen_google).
        google_response = google_agent.run(title)
        resumen_google = google_response.to_dict()["messages"][-1]["content"].strip()

        # 4. Generar embeddings para ambos resúmenes.
        emb_agentes = embedder.get_embedding(resumen_agentes)[0]
        emb_google = embedder.get_embedding(resumen_google)[0]
        vec1 = np.array(emb_agentes)
        vec2 = np.array(emb_google)

        # 5. Evaluar métricas.
        metrics = evaluate_summaries(resumen_agentes, resumen_google, vec1, vec2)

        # Almacenar resultados en el diccionario.
        evaluation_results[clase] = {
            "metrics": metrics,
            "resumen_agentes": resumen_agentes,
            "resumen_google": resumen_google
        }

        print(f"Evaluación para {clase}:")
        print(f"  Cosine Similarity: {metrics['cosine similarity']:.4f}")
        print(f"  Euclidean Distance: {metrics['euclidean distance']:.4f}")
        print(f"  Manhattan Distance: {metrics['manhattan distance']:.4f}")
        print(f"  ROUGE-1 F1: {metrics['rouge']['rouge1']:.4f}")
        print(f"  ROUGE-2 F1: {metrics['rouge']['rouge2']:.4f}")
        print(f"  ROUGE-L F1: {metrics['rouge']['rougeL']:.4f}")
        print(f"  BLEU Score: {metrics['bleu']:.4f}")
        print(f"  BERTScore F1: {metrics['bert_score_f1']:.4f}")
        print("-----------------------------------------------------")

# Guardar el diccionario de evaluación en un archivo JSON en el directorio base.
output_json_path = os.path.join(base_dir, "notes_evaluation.json")
with open(output_json_path, "w", encoding="utf-8") as json_file:
    json.dump(evaluation_results, json_file, indent=4, ensure_ascii=False)

print(f"\nSe ha guardado la evaluación en: {output_json_path}")
