# Descubrimiento de tópicos en vacantes de ciencia de datos

Proyecto aplicado del Programa de Formación en Machine Learning y Data Science (UNAL),
desarrollado con la metodología TDSP.

Identificamos los temas y habilidades más demandados en ofertas de empleo de ciencia de
datos publicadas en LinkedIn en 2024, usando modelado de tópicos (LDA, BERTopic).

## Integrantes
- Wolffang David Niño Pacheco
- Nicolle Stefania Quintero
- Sergio Eliecer Guecha León

## Cómo ejecutar

    python -m venv .venv
    source .venv/bin/activate        # Windows: .venv\Scripts\activate
    pip install -e .
    python scripts/data_acquisition/main.py

## Estructura
- `docs/`: documentos de la metodología TDSP.
- `scripts/`: scripts que se ejecutan en cada etapa.
- `src/topicos_vacantes/`: código del proyecto como paquete de Python.
