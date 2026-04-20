# The Library's Lost Books

## Description

A library recently digitized its collection, but the digital catalog became corrupted. Some book records are missing crucial information or contain errors. This script reads a CSV file, cleans the data, removes duplicates, and presents an organized catalog.

## Input Format

The script reads `books.csv`, a comma-separated file with three columns:

```
Title,Author,Publication Year
```

## Data Issues Handled

| Issue | Fix Applied |
|---|---|
| Missing title | Row is discarded entirely |
| Missing author | Replaced with `"Author Unknown"` |
| Missing year | Replaced with `0` |
| Non-numeric year (e.g. `"unknown"`) | Replaced with `0` |
| Negative or far-future year | Replaced with `0` |
| Duplicate entries | Deduplicated, keeping one record |

Valid year range: `-3000` to the current year.

## Output

Books are displayed in two groups:

1. **Books with known author** — grouped alphabetically by author, then sorted by year within each author.
2. **Books with unknown author** — grouped by publication year.

## Usage

```bash
python biblioteca.py
```

Make sure `books.csv` is in the same directory as the script.

## File Structure

```
.
├── biblioteca.py   # Main script
├── books.csv       # Input catalog (may contain dirty data)
└── README.md
```

---

# Los Libros Perdidos de la Biblioteca

## Descripcion

Una biblioteca digitalizo recientemente su coleccion, pero el catalogo digital resulto corrompido. Algunos registros tienen informacion faltante o con errores. Este script lee un CSV, limpia los datos, elimina duplicados y presenta un catalogo organizado.

## Formato de entrada

El script lee `books.csv`, un archivo separado por comas con tres columnas:

```
Title,Author,Publication Year
```

## Problemas de datos manejados

| Problema | Solucion aplicada |
|---|---|
| Titulo faltante | La fila se descarta por completo |
| Autor faltante | Se reemplaza por `"Author Unknown"` |
| Anio faltante | Se reemplaza por `0` |
| Anio no numerico (ej. `"unknown"`) | Se reemplaza por `0` |
| Anio negativo o demasiado futuro | Se reemplaza por `0` |
| Registros duplicados | Se deduplican, conservando uno |

Rango de anio valido: `-3000` hasta el anio actual.

## Salida

Los libros se muestran en dos grupos:

1. **Libros con autor conocido** — agrupados alfabeticamente por autor, luego ordenados por anio.
2. **Libros sin autor** — agrupados por anio de publicacion.

## Uso

```bash
python biblioteca.py
```

Asegurarse de que `books.csv` este en el mismo directorio que el script.

## Estructura de archivos

```
.
├── biblioteca.py   # Script principal
├── books.csv       # Catalogo de entrada (puede contener datos sucios)
└── README.md
```
