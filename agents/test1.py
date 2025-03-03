from phi.agent import Agent
from phi.model.openai import OpenAIChat
from phi.utils.pprint import pprint_run_response


# Definimos el agente con instrucciones claras para transformar el input
agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    instructions=[
        "Recibe el siguiente texto en el que se indican capítulos y títulos.",
        "Genera un contenido en Markdown donde cada capítulo se convierte en una 'Clase' con un encabezado del tipo '## Clase X: Título'.",
        "Debajo de cada encabezado, agrega una lista con 5 puntos que profundicen o amplíen el tema, de forma que se estructure el contenido de un curso."
    ],
    markdown=True,
)

# Texto de entrada
texto = """
Capítulo 001
Cerebro e inteligencia.
Capítulo 002
Aprendizaje heurístico.
Capítulo 003
Perceptrones.
Capítulo 004
Adaline, Madaline y Modelos asociativos.
Capítulo 005
Perceptron continuo y perceptron multicapa.
"""


# Ejecuta el agente con el texto
response = agent.run(texto)

## Imprime la respuesta
# pprint_run_response(response)

response_assistant = response.to_dict()["messages"][2]["content"]

with open("output.md", "w") as file:
    file.write(response_assistant)