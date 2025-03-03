# Clase 3: Perceptrones

## Introducción

El perceptrón es una de las contribuciones más significativas en la historia de la inteligencia artificial y específicamente en el campo del aprendizaje automático. Concebido en una época en la que la inteligencia artificial estaba en sus etapas formativas, el perceptrón representaba una promesa: crear máquinas que pudieran aprender de la experiencia. Este concepto, en su forma más básica, sentó las bases para el desarrollo de modelos de aprendizaje más complejos y avanzados. En esta clase, exploraremos en detalle la historia, la arquitectura, el funcionamiento, las limitaciones y las aplicaciones del perceptrón para comprender cómo este modelo ha influido en la evolución del aprendizaje automático.

## 1. Historia y origen del perceptrón

La historia del perceptrón se remonta a la década de 1950 cuando Frank Rosenblatt, un psicólogo e ingeniero estadounidense, introdujo este concepto revolucionario. Rosenblatt desarrolló el perceptrón en 1958 como parte de un esfuerzo para entender y emular el funcionamiento del cerebro humano. Este modelo fue inicialmente concebido para realizar tareas de reconocimiento visual, inspirándose en la estructura y funcionamiento de las neuronas en el cerebro. El trabajo de Rosenblatt generó gran entusiasmo al reclutar la atención tanto del mundo académico como del ámbito industrial, ya que parecía capaz de aprender y decidir de manera autónoma.

### Ejemplo Histórico

En 1960, Rosenblatt y su equipo construyeron el primer prototipo de perceptrón, llamado Mark I, que utilizaba componentes electrónicos y ópticos para realizar tareas de reconocimiento de patrones. Este evento fue un parteaguas que mostró el potencial de las máquinas para aprender.

## 2. Arquitectura del perceptrón

El perceptrón es un modelo de red neuronal muy sencillo y sirve como la unidad básica de las redes neuronales más complejas. Su arquitectura incluye esencialmente un conjunto de entradas, pesos, un sesgo, y un nodo de salida que aplica una función de activación.

- **Entradas**: Cada entrada representa una característica del dato que estamos procesando.
- **Pesos**: A cada entrada le corresponde un peso que determina su impacto en la decisión final.
- **Sesgo**: Una constante que permite ajustar la salida del modelo. 
- **Función de Activación**: Comúnmente, se utiliza una función escalonada que decide la activación del perceptrón.

### Ejemplo de Arquitectura

Piensa en un perceptrón diseñado para resolver un problema de clasificación binaria, como determinar si un correo electrónico es spam o no. Cada entrada podría representar una característica relevante del correo, como la frecuencia de ciertas palabras. Los pesos ajustados determinan la contribución de cada palabra a la clasificación final.

## 3. Funcionamiento del algoritmo de aprendizaje del perceptrón

El algoritmo de aprendizaje del perceptrón es un método iterativo que busca ajustar los pesos para minimizar el error en la salida. Puede resumirse en los siguientes pasos:

1. **Inicialización de Pesos**: Comienza asignando valores aleatorios a los pesos y el sesgo.
2. **Paso hacia adelante**: Calcula la salida ponderada mediante la suma de las entradas multiplicadas por sus pesos adjuntos, más el sesgo.
3. **Aplicación de la función de activación**: Determina la salida final comparando la suma ponderada con un umbral.
4. **Ajuste de Pesos**: Si la salida es incorrecta, la regla de actualización ajusta los pesos proporcionalmente al error (diferencia entre salida deseada y calculada).
5. **Iteración**: Los pasos 2 a 4 se repiten hasta que los errores se minimizan o se alcanza un número predeterminado de iteraciones.

### Ejemplo de Ajuste de Pesos

Supongamos que la salida deseada es 1, pero el perceptrón proporciona una salida de 0. El error es 1 y, basado en este error, los pesos se ajustan para aumentar la probabilidad de que el perceptrón produzca la salida correcta en la próxima iteración.

## 4. Limitaciones del perceptrón

Una de las limitaciones más conocidas del perceptrón es su incapacidad para resolver problemas no lineales. Esto fue formalmente discutido en 1969 por Marvin Minsky y Seymour Papert en su libro "Perceptrons". El ejemplo más conocido de un problema no lineal es el problema XOR (o exclusiva), donde la salida es 1 solo si exactamente una de las entradas es 1.

### Por qué el Perceptrón no Resuelve XOR

El perceptrón no puede separar las clases de un problema XOR usando un plano lineal único debido a la naturaleza del problema, que requiere una distinción lineal que no existe en su configuración original. Para manejar esto, las arquitecturas tuvieron que evolucionar a multi-capas o redes neuronales profundas donde múltiples perceptrones se combinan para formar capas ocultas que permiten resolver tales problemas no lineales.

## 5. Aplicaciones del perceptrón

A pesar de sus limitaciones, los perceptrones han encontrado muchas aplicaciones prácticas en tareas de clasificación y reconocimiento simple. Estos incluyen sistemas de reconocimiento óptico de caracteres, detección de spam, y clasificación básica de imágenes.

### Ejemplo de Aplicación

Un ejemplo práctico es un sistema rudimentario de reconocimiento de caracteres que utiliza perceptrones para distinguir entre letras o números en imágenes. Mientras que este sistema sería básico y requeriría perfeccionamientos adicionales para mejorar su precisión, proporciona una base sólida para aplicaciones iniciales de reconocimiento de patrones.

## Conclusión

El perceptrón representa un hito crucial en la historia de la inteligencia artificial y el aprendizaje automático. A pesar de sus limitaciones, sienta las bases para comprender las operaciones básicas de los modelos de aprendizaje y ayuda a construir intuiciones para arquitecturas más complejas como las redes neuronales profundas. Las limitaciones identificadas en el perceptrón inspiraron innovaciones que llevaron al desarrollo de técnicas de aprendizaje que ahora están en el corazón de las soluciones de inteligencia artificial modernas, demostrando que incluso las ideas simples pueden tener un impacto duradero en el progreso tecnológico.