# Agents
This is a project for using IA agents, for the course RNA (Universidad Nacional de Colombia)


```
Academic-Agent-Workflow
|-- app
|   |-- main.py          # Main entry point of the Streamlit 
|   |-- test.txt         # example file test
|
|-- agents
|   |-- agents.py        # Got all the agents for the project 
|   |-- metrics.py       # Execute the validation metrics
|
|-- outputs
|   |-- Ejemplo Output
|   |-- Ejemplo_Clase
|   |-- generated-<uuid> # Files generated (course content)
|
|-- .gitignore
|-- requirements.txt    # Packages to install with pip
└── README.md           # Documentation for the project
```

## Quick start 
The basic Configuration for the project

### Installation

To set up the project (Unix-like systems) follow these steps:

1. Clone the repository:
   ```
   git clone <repository-url>
   cd <repo-name>
   ```
2. Create virtual environment
   ```
   python3 -m venv .venv
   ```
3. Activate python environment
   ```
   source .venv/bin/activate
   ```

4. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

### Running the Application

To run the Streamlit application, execute the following command in your terminal:

```
streamlit run suite/main.py
```

Once the application is running, you can upload a text file, and the app will display the converted Markdown content.

## Agents
There are 6 agents, each one in charge of one functionality

### 1. Organizer

**Instructions**
- "Recibe el siguiente texto en el que se indican capítulos y títulos."
- "Genera un contenido en Markdown donde cada capítulo se convierte en una 'Clase' con un encabezado del tipo `## Clase X: Título`"
- "Debajo de cada encabezado, agrega una lista con 5 puntos que profundicen o amplíen el tema, de forma que se estructure el contenido de un curso."

### 2 notes agent

**Instructions**
- "A partir del siguiente fragmento markdown que describe una clase, genera notas de clase extendidas en Markdown. "
- "Incluye una introducción detallada, explicación profunda de cada punto con ejemplos y una conclusión clara."

### 3 objectives agent

**Instructions**
- "A partir del siguiente fragmento markdown que describe una clase, genera de manera breve los objetivos de la clase. "
- "Resume los puntos clave y lo que se pretende lograr, en formato Markdown."

### 4. Quiz agent

**Instructions**
- "Utiliza las notas de clase extendidas (en Markdown) proporcionadas para generar un conjunto de ejercicios tipo quiz. "
- "Cada ejercicio debe incluir un enunciado, varias opciones y la solución correcta, todo formateado en Markdown."

### 5. Discussion agent

**Instructions**
- "A partir de las notas de clase extendidas (en Markdown) proporcionadas, genera preguntas para discusión que estimulen "
- "la reflexión y el debate sobre el contenido de la clase. Formatea las preguntas en Markdown."

### 6. Resources agent

**Instructions**
- "Eres un agente experto en recomendar recursos de interés para profundizar en temas académicos y técnicos."
- "Dado el tema de una clase, recomienda 3 o 4 recursos relevantes, incluyendo blogs de Medium y papers de Arxiv."
- "Para los blogs de Medium, utiliza Google Search para buscar posts recientes y de calidad. Para los papers, utiliza ArxivToolkit para buscar publicaciones académicas sobre el tema."
- "Devuelve la respuesta en formato Markdown, enumerando cada recurso con su título, una breve descripción y el enlace correspondiente."

**Other tools**
We import from `phidata` another objects that make possible the interaction between the LLM and internet, so it will be able to search for real articles, papers and books in the internet, instead of just hallucinated


## Suite
This is a small interface running in local for testing the app, made using streamlit

### Usage
After running the application go to `localhost:8501` (generally this is the port)

1. Upload a text file using the file uploader in the Streamlit app.
2. The app will extract the text from the file.
3. The extracted text will be processed for the multiple agents
4. The resulting Markdown content will be displayed on the app interface and saved in the `output` folder

### Testing

For using the test for validation metrics, use the `metrics.py` file, insert the course base directory, and then the file `notes_evaluation.json` will have all the metric data about it