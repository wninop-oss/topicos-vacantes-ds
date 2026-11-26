"""Descarga los datos de Kaggle, los carga y guarda el corpus integrado.

Uso: python scripts/data_acquisition/main.py
"""
from pathlib import Path

from topicos_vacantes.database.carga import cargar_tablas, construir_corpus, descargar_datos

RAIZ = Path(__file__).resolve().parents[2]
RUTA_RAW = RAIZ / "data" / "raw"
RUTA_PROCESSED = RAIZ / "data" / "processed"


def main():
    print("Descargando datos de Kaggle...")
    descargar_datos(RUTA_RAW)

    tablas = cargar_tablas(RUTA_RAW)
    for nombre, df in tablas.items():
        print(f"{nombre}: {df.shape[0]:,} filas x {df.shape[1]} columnas")

    corpus = construir_corpus(tablas)
    print(f"Duplicados removidos: {len(tablas['postings']) - len(corpus):,}")
    print(f"Documentos finales en el corpus: {len(corpus):,}")

    RUTA_PROCESSED.mkdir(parents=True, exist_ok=True)
    corpus.to_parquet(RUTA_PROCESSED / "corpus.parquet", index=False)
    print("Corpus guardado en data/processed/corpus.parquet")


if __name__ == "__main__":
    main()