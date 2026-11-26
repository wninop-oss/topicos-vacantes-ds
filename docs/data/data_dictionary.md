# Diccionario de datos

El proyecto usa tres tablas del dataset de Kaggle "Data Science Job Postings & Skills (2024)",
cada una con 12.217 filas. Se relacionan por la columna `job_link`, que identifica cada vacante.
Al unirlas y quitar descripciones repetidas queda un corpus de 9.661 vacantes.

## Base de datos 1: job_postings.csv

Metadatos de cada vacante de ciencia de datos publicada en LinkedIn. Una fila por vacante (15 columnas).

| Variable | Descripción | Tipo de dato | Rango/Valores posibles | Fuente de datos |
| --- | --- | --- | --- | --- |
| job_link | URL de la vacante en LinkedIn; llave que une las tres tablas | Texto | Único por vacante | Kaggle - job_postings.csv |
| last_processed_time | Fecha y hora en que el recolector procesó la vacante por última vez | Fecha-hora | Enero de 2024 | Kaggle - job_postings.csv |
| last_status | Estado del procesamiento de la vacante en la recolección | Categórica | Completar con perfil_datos.py | Kaggle - job_postings.csv |
| got_summary | Indica si se descargó la descripción de la vacante | Booleana | t, f | Kaggle - job_postings.csv |
| got_ner | Indica si se extrajeron las habilidades con NER | Booleana | t, f | Kaggle - job_postings.csv |
| is_being_worked | Indicador interno del proceso de recolección | Booleana | t, f | Kaggle - job_postings.csv |
| job_title | Título del cargo publicado; de él se derivan el nivel (seniority) y la familia de rol | Texto | Texto libre | Kaggle - job_postings.csv |
| company | Empresa u organización que publica la vacante | Categórica nominal | Texto libre (miles de empresas) | Kaggle - job_postings.csv |
| job_location | Ciudad de la vacante | Categórica nominal | 1.816 ubicaciones distintas en el corpus | Kaggle - job_postings.csv |
| first_seen | Fecha en que la vacante se vio por primera vez | Fecha | 12 al 17 de enero de 2024 | Kaggle - job_postings.csv |
| search_city | Ciudad usada en la búsqueda que encontró la vacante | Texto | Texto libre | Kaggle - job_postings.csv |
| search_country | País usado en la búsqueda | Categórica nominal | United States (84,1%), United Kingdom (8,8%), Canada (4,4%), Australia (2,6%) | Kaggle - job_postings.csv |
| search_position | Cargo usado como término de búsqueda | Texto | Texto libre | Kaggle - job_postings.csv |
| job_level | Nivel del cargo según LinkedIn | Categórica | Mid senior, Associate | Kaggle - job_postings.csv |
| job_type | Modalidad de trabajo | Categórica | Onsite (99,7%), Remote, Hybrid | Kaggle - job_postings.csv |

Los porcentajes de `search_country` y `job_type` están calculados sobre el corpus de 9.661 vacantes.

## Base de datos 2: job_skills.csv

Habilidades de cada vacante, extraídas de la descripción con reconocimiento de entidades (NER). Una fila por vacante.

| Variable | Descripción | Tipo de dato | Rango/Valores posibles | Fuente de datos |
| --- | --- | --- | --- | --- |
| job_link | URL de la vacante; llave para unir con job_postings | Texto | Único por vacante | Kaggle - job_skills.csv |
| job_skills | Lista de habilidades pedidas en la vacante, separadas por comas | Texto (lista) | Texto libre | Kaggle - job_skills.csv |

## Base de datos 3: job_summary.csv

Texto completo de la descripción de cada vacante, en inglés. Es el corpus principal del modelado de tópicos.

| Variable | Descripción | Tipo de dato | Rango/Valores posibles | Fuente de datos |
| --- | --- | --- | --- | --- |
| job_link | URL de la vacante; llave para unir con job_postings | Texto | Único por vacante | Kaggle - job_summary.csv |
| job_summary | Descripción de la vacante (funciones, requisitos, beneficios) | Texto | ~600 palabras en promedio; desde textos casi vacíos hasta ~2.850 palabras | Kaggle - job_summary.csv |
