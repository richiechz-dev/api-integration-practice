# API Practica de Integración

Ejercicio práctico de integración con APIs REST en Python,
cubriendo patrones comunes en entornos productivos. 

## Ejercicio

**recipe_max_ingredient.py**  
Clase que consume la API de Spoonacular para encontrar
el ingrediente de mayor cantidad en una receta.  
Conceptos: autenticación con API Key en headers, 
parseo de JSON anidado, patrón de búsqueda de máximo en lista.

## Setup

1. Instala dependencias:
uv sync

2. Crea un archivo `.env` basado en `.env.example`:
SPOONACULAR_API_KEY=your_api_key_here

3. Ejecuta:
uv run recipe_max_ingredient.py

## Stack
- Python
- requests
- python-dotenv