
# VulnerabilidadesIAdata
# Hacer los resultados del modelo final

from pathlib import Path
import pandas as pd
import joblib

from sklearn.metrics import (
    accuracy_score,
    f1_score,
    recall_score
)

# Ubicar los archivos del proyecto
carpeta = Path(__file__).resolve().parent

ruta_datos = carpeta / "data" / "cve_2025_procesado.parquet"
ruta_modelo = carpeta / "model.joblib"

# Cargar el dataset preparado
df = pd.read_parquet(ruta_datos)

df["fecha"] = pd.to_datetime(df["fecha"])

# Ordenar las vulnerabilidades por fecha
df = df.sort_values(
    ["fecha", "cve_id"]
).reset_index(drop=True)

# Recuperar los datos de prueba
fin_val = int(len(df) * 0.85)
test = df.iloc[fin_val:].copy()

# Cargar el modelo guardado
modelo = joblib.load(ruta_modelo)

# Realizar predicciones
predicciones = modelo.predict(
    test["descripcion_limpia"]
)

# Calcular métricas
accuracy = accuracy_score(
    test["gravedad"], predicciones
)

f1 = f1_score(
    test["gravedad"],
    predicciones,
    average="macro",
    zero_division=0
)

recall_criticas = recall_score(
    test["gravedad"] == "CRITICAL",
    predicciones == "CRITICAL",
    zero_division=0
)

# Mostrar resultados
print("PROYECTO: VulnerabilidadesIAdata")
print("Registros de prueba:", len(test))
print("Accuracy:", round(accuracy, 4))
print("F1-macro:", round(f1, 4))
print("Recall de críticas:", round(recall_criticas, 4))
