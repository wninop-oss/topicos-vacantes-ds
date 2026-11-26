# Project Charter - Entendimiento del Negocio

## Nombre del Proyecto

Descubrimiento de tópicos en vacantes de ciencia de datos de LinkedIn (2024)

## Objetivo del Proyecto

Identificar los perfiles temáticos dominantes en las ofertas laborales de ciencia de datos y
las habilidades asociadas a cada uno, aplicando modelado de tópicos sobre las descripciones de
las vacantes.

Es importante porque las ofertas expresan sus requisitos en lenguaje natural no estructurado y
los cargos del sector no tienen fronteras claras: una misma vacante puede mezclar Data Analytics,
Machine Learning, Data Engineering y Business Intelligence. Con miles de ofertas, identificar
estos perfiles de forma manual no es viable.

## Alcance del Proyecto

### Incluye:

- Datos: dataset público de Kaggle "Data Science Job Postings & Skills (2024)" con 12.217
  vacantes de LinkedIn en tres archivos (metadatos, descripción y habilidades). Tras quitar
  descripciones repetidas quedan 9.661 documentos. El corpus principal es `job_summary`.
- Resultados esperados:
  - Integración de los tres archivos por `job_link` y depuración del corpus (duplicados,
    documentos muy cortos y texto repetitivo de LinkedIn).
  - Tópicos obtenidos con LDA y BERTopic, nombrados a partir de sus términos y documentos
    representativos.
  - Cruce de los tópicos con las habilidades (`job_skills`), el nivel del cargo (derivado de
    `job_title`) y el país.
- Criterios de éxito: comparar ambos modelos por coherencia, diversidad y cobertura de los
  tópicos, y obtener perfiles que el equipo pueda interpretar y explicar.

### Excluye:

- Recolección de vacantes nuevas (el scraping lo hizo el autor del dataset).
- Recomendación de candidatos o automatización de procesos de contratación.
- Conclusiones de tendencia anual o para Latinoamérica: los datos son una instantánea del 12 al
  17 de enero de 2024, concentrada en el mercado angloparlante (~84% Estados Unidos, además de
  Reino Unido, Canadá y Australia).

## Metodología

Se sigue la metodología TDSP (Team Data Science Process): entendimiento del negocio, adquisición
y entendimiento de los datos, modelamiento, despliegue y aceptación del cliente.

Para el modelamiento se comparan dos enfoques complementarios de modelado de tópicos:

- **LDA** (Latent Dirichlet Allocation; Blei et al., 2003): trabaja sobre bolsa de palabras y
  encuentra tópicos por coocurrencia de términos.
- **BERTopic** (Grootendorst, 2022): trabaja sobre embeddings de transformers y agrupa las
  vacantes por similitud de significado.

Como extensión se puede incluir NMF sobre la matriz TF-IDF.

## Cronograma

| Etapa | Duración Estimada | Fechas |
|------|---------|-------|
| Entendimiento del negocio y carga de datos | 2 semanas | FECHA a FECHA |
| Preprocesamiento, análisis exploratorio | 2 semanas | FECHA a FECHA |
| Modelamiento y extracción de características | 3 semanas | FECHA a FECHA |
| Despliegue | 1 semana | FECHA a FECHA |
| Evaluación y entrega final | 1 semana | FECHA a FECHA |

## Equipo del Proyecto

- Wolffang David Niño Pacheco – Líder del proyecto e ingeniería de datos
- Sergio Eliecer Guecha León – Entendimiento del negocio y modelamiento
- Nicolle Stefania Quintero – Análisis y calidad de datos

## Presupuesto

Proyecto académico sin presupuesto monetario. Se usan recursos gratuitos: dataset público de
Kaggle, Google Colab (GPU para los embeddings y BERTopic), GitHub y librerías de código abierto
en Python.

## Stakeholders

- Instituciones educativas (bootcamps y academias de tecnología): usan los perfiles temáticos y
  sus habilidades asociadas para priorizar contenido curricular.
- Estudiantes y profesionales interesados en ciencia de datos: quieren saber qué perfiles y
  habilidades pide el mercado.
- Docentes del curso: esperan un proyecto que aplique correctamente la metodología TDSP.
