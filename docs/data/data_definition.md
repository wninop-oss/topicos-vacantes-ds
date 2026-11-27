# Definición de los datos

## Origen de los datos

Los textos son ofertas laborales publicadas en LinkedIn, distribuidas públicamente en Kaggle
como "Data Science Job Postings & Skills (2024)" (Asaniczka, 2024):
https://www.kaggle.com/datasets/asaniczka/data-science-job-postings-and-skills

Cubre 12.217 vacantes de roles de datos y tecnología, capturadas entre el 12 y el 17 de enero
de 2024, en cuatro países (Estados Unidos ~84%, Reino Unido, Canadá y Australia). El scraping lo
hizo el autor del dataset; nuestro proceso es de carga, no de extracción web. Los archivos se
descargan con la librería `kagglehub`.

## Especificación de los scripts para la carga de datos

- `src/topicos_vacantes/database/carga.py`: funciones `descargar_datos`, `cargar_tablas` y
  `construir_corpus`.
- `scripts/data_acquisition/main.py`: ejecuta la descarga, la carga y la construcción del corpus.

## Referencias a rutas o bases de datos origen y destino

### Rutas de origen de datos

- Ubicación: dataset `asaniczka/data-science-job-postings-and-skills` en Kaggle, copiado a `data/raw/`.
- Estructura: tres archivos CSV de 12.217 filas cada uno, relacionados por la columna `job_link`
  (URL única de la vacante):
  - `job_postings.csv` (15 columnas): metadatos de la vacante (cargo, empresa, ubicación, nivel, modalidad).
  - `job_skills.csv`: habilidades de cada vacante, extraídas con NER y separadas por comas.
  - `job_summary.csv`: texto completo de la descripción de la vacante, en inglés.
- Transformación y limpieza en la carga:
  1. Unión de `job_postings` con `job_summary` (inner join) y luego con `job_skills` (left join) por `job_link`.
  2. Eliminación de vacantes sin descripción.
  3. Eliminación de descripciones repetidas: 2.556 vacantes eran la misma oferta republicada
     por distintas agencias. Quedan 9.661 documentos.

  La limpieza del texto (boilerplate de LinkedIn, tokenización, lematización) se hace en la etapa
  de preprocesamiento.

### Base de datos de destino

- Destino: archivo `data/processed/corpus.parquet` (generado con el script; los datos también se incluyen en el repositorio).
- Estructura: una fila por vacante única (9.661), con las 15 columnas de `job_postings` más
  `job_summary` y `job_skills`.
- Carga: se escribe con `pandas.DataFrame.to_parquet`, que conserva los tipos de dato.
