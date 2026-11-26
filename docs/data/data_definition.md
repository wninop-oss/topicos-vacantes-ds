\# Definición de los datos



\## Origen de los datos



Los textos son ofertas laborales publicadas en LinkedIn, distribuidas públicamente en Kaggle

como "Data Science Job Postings \& Skills (2024)" (Asaniczka, 2024):

https://www.kaggle.com/datasets/asaniczka/data-science-job-postings-and-skills



Cubre 12.217 vacantes de roles de datos y tecnología, capturadas entre el 12 y el 17 de enero

de 2024, en cuatro países (Estados Unidos \~84%, Reino Unido, Canadá y Australia). El scraping lo

hizo el autor del dataset; nuestro proceso es de carga, no de extracción web. Los archivos se

descargan con la librería `kagglehub`.



\## Especificación de los scripts para la carga de datos



\- `src/topicos\_vacantes/database/carga.py`: funciones `descargar\_datos`, `cargar\_tablas` y

&#x20; `construir\_corpus`.

\- `scripts/data\_acquisition/main.py`: ejecuta la descarga, la carga y la construcción del corpus.



\## Referencias a rutas o bases de datos origen y destino



\### Rutas de origen de datos



\- Ubicación: dataset `asaniczka/data-science-job-postings-and-skills` en Kaggle, copiado a `data/raw/`.

\- Estructura: tres archivos CSV de 12.217 filas cada uno, relacionados por la columna `job\_link`

&#x20; (URL única de la vacante):

&#x20; - `job\_postings.csv` (15 columnas): metadatos de la vacante (cargo, empresa, ubicación, nivel, modalidad).

&#x20; - `job\_skills.csv`: habilidades de cada vacante, extraídas con NER y separadas por comas.

&#x20; - `job\_summary.csv`: texto completo de la descripción de la vacante, en inglés.

\- Transformación y limpieza en la carga:

&#x20; 1. Unión de `job\_postings` con `job\_summary` (inner join) y luego con `job\_skills` (left join) por `job\_link`.

&#x20; 2. Eliminación de vacantes sin descripción.

&#x20; 3. Eliminación de descripciones repetidas: 2.556 vacantes eran la misma oferta republicada

&#x20;    por distintas agencias. Quedan 9.661 documentos.



&#x20; La limpieza del texto (boilerplate de LinkedIn, tokenización, lematización) se hace en la etapa

&#x20; de preprocesamiento.



\### Base de datos de destino



\- Destino: archivo `data/processed/corpus.parquet` (no se sube al repositorio; se genera con el script).

\- Estructura: una fila por vacante única (9.661), con las 15 columnas de `job\_postings` más

&#x20; `job\_summary` y `job\_skills`.

\- Carga: se escribe con `pandas.DataFrame.to\_parquet`, que conserva los tipos de dato.



