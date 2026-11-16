# BPS-DsciAinara
Proyecto de Data Science: Un análisis inteligente de vulnerabilidades 

## Parte 2 - Análisis y predicción de vulnerabilidades

En esta segunda parte de mi proyecto he trabajado con una base de datos de vulnerabilidades informáticas de la NVD.

Lo que quiero conseguir es comprobar si la inteligencia artificial puede ayudar a saber qué vulnerabilidades son más graves y cuáles deberían revisarse primero en una empresa.

Al principio tenía 45.373 registros, pero después de revisar y limpiar los datos me he quedado con 43.160 vulnerabilidades.

Primero he analizado los datos para entender mejor la información que tenía. Después he probado diferentes modelos de Machine Learning para ver cuál conseguía mejores resultados.

He utilizado un modelo sencillo de referencia llamado DummyClassifier, Regresión Logística y Random Forest.

Al comparar los resultados, he decidido utilizar una Regresión Logística mejorada, porque conseguía identificar más vulnerabilidades críticas.

### Resultados finales

Estos son los resultados que he conseguido con los datos de prueba:

| Métrica | Resultado |
|---|---|
| Accuracy | 60,78 % |
| F1-macro | 0,5070 |
| Recall de vulnerabilidades críticas | 58,43 % |

Aunque he conseguido mejorar los resultados del modelo inicial, todavía hay vulnerabilidades críticas que no detecta correctamente.

Por eso, creo que este modelo puede servir para ayudar a los equipos de ciberseguridad, pero no para sustituir el trabajo de una persona.

### Archivos de mi proyecto

He guardado los archivos que he utilizado para que se pueda revisar mi trabajo:

- `project/project-brief.md`: la primera parte de mi proyecto.
- `project/project-model.ipynb`: donde he realizado el análisis de datos, los gráficos y los modelos.
- `project/data/cve_2025_procesado.parquet`: los datos que he preparado después de la limpieza.
- `project/model.joblib`: el modelo final que he guardado.
- `project/reproducir_modelo.py`: un programa para comprobar los resultados.
- `project/requirements.txt`: las librerías que se necesitan para ejecutar el programa.

### Cómo comprobar mis resultados

Para que se puedan comprobar mis resultados sin tener que repetir todo el trabajo, he creado un archivo de Python.

Primero hay que instalar las librerías necesarias. Desde la carpeta principal del repositorio se ejecuta:

```bash
python -m pip install -r project/requirements.txt
```

Después se ejecuta:

```bash
python project/reproducir_modelo.py
```

Con esto se pueden ver los resultados finales que he conseguido, sin necesidad de descargar el archivo JSON original.

### Cosas que todavía puedo mejorar

Aunque mi modelo ha conseguido aprender algunos patrones de las vulnerabilidades, todavía comete errores.

Por ejemplo, algunas vulnerabilidades que realmente son críticas aparecen clasificadas como bajas o medias.

Por eso, considero que todavía tendría que seguir mejorándolo antes de utilizarlo en una empresa real.

También hay que tener en cuenta que el archivo Parquet permite comprobar la evaluación final, pero para repetir todo el análisis inicial necesitaría el JSON original de la NVD.

Mi idea es que este proyecto sirva como una primera ayuda para organizar las vulnerabilidades, pero que las decisiones importantes siempre las revise un profesional de ciberseguridad.
