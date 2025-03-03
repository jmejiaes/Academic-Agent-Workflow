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

### 1 abc

### 2 abc
### 3 abc
### 4 abc
### 5 abc
### 6 abc

## Suite
This is a small interface running in local for testing the app, made using streamlit

### Usage
After running the application go to `localhost:8501` (generally this is the port)

1. Upload a text file using the file uploader in the Streamlit app.
2. The app will extract the text from the file.
3. The extracted text will be processed for the multiple agents
4. The resulting Markdown content will be displayed on the app interface and saved in the `output` folder
