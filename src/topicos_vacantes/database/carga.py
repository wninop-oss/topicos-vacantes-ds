"""Funciones para descargar y cargar el dataset de vacantes de ciencia de datos."""
import shutil
from pathlib import Path

import kagglehub
import pandas as pd

DATASET_ID = "asaniczka/data-science-job-postings-and-skills"
ARCHIVOS = {
    "postings": "job_postings.csv",  # metadatos de cada vacante
    "skills": "job_skills.csv",      # habilidades por vacante
    "summary": "job_summary.csv",    # texto de la descripción
}


def descargar_datos(destino: Path) -> Path:
    """Descarga el dataset de Kaggle y copia los CSV a la carpeta destino."""
    destino.mkdir(parents=True, exist_ok=True)
    ruta_cache = Path(kagglehub.dataset_download(DATASET_ID))
    for nombre in ARCHIVOS.values():
        origen = next(ruta_cache.rglob(nombre))
        shutil.copy(origen, destino / nombre)
    return destino


def cargar_tablas(ruta: Path) -> dict[str, pd.DataFrame]:
    """Lee los tres CSV y los devuelve en un diccionario."""
    return {clave: pd.read_csv(ruta / archivo) for clave, archivo in ARCHIVOS.items()}


def construir_corpus(tablas: dict[str, pd.DataFrame]) -> pd.DataFrame:
    """Une las tablas por job_link y deja una fila por descripción única.

    Es el mismo proceso de la Fase 1 del proyecto de PLN: solo se conservan
    vacantes con descripción y se eliminan las descripciones repetidas
    (agencias que republican la misma oferta).
    """
    corpus = (
        tablas["postings"]
        .merge(tablas["summary"], on="job_link", how="inner")
        .merge(tablas["skills"], on="job_link", how="left")
    )
    corpus = corpus.dropna(subset=["job_summary"])
    corpus = corpus.drop_duplicates(subset=["job_summary"])
    return corpus.reset_index(drop=True)