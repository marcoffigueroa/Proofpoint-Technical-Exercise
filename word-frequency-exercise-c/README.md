# Analisis de Frecuencia de Palabras

## Descripcion

Este script lee un archivo de texto plano, limpia el contenido (ignorando mayusculas, puntuacion y caracteres especiales) y muestra las 10 palabras mas frecuentes junto con su cantidad de apariciones y porcentaje sobre el total.

## Procesamiento aplicado

| Paso | Que se hace |
|---|---|
| Normalizacion | Todo el texto se convierte a minusculas |
| Limpieza | Se eliminan signos de puntuacion y caracteres especiales |
| Tokenizacion | El texto se divide en palabras individuales |
| Conteo | Se cuenta cuantas veces aparece cada palabra |
| Resultado | Se muestran las 10 palabras con mayor frecuencia |

## Salida

```
==================================================
TOP 10 PALABRAS MAS FRECUENTES
==================================================
#     PALABRA              VECES      %
--------------------------------------------------
1     de                      18   5.7%
2     la                      15   4.7%
...
==================================================
Total palabras: 318  |  Unicas: 163
```

## Uso

### Forma basica (usa `texto_prueba.txt` por defecto)

```bash
python frecuencia_palabras.py
```

### Pasando un archivo propio como argumento

```bash
python frecuencia_palabras.py mi_archivo.txt
```

El archivo debe estar en formato `.txt` con codificacion UTF-8.

## Estructura del proyecto

```
.
├── frecuencia_palabras.py   # Script principal
├── texto_prueba.txt         # Archivo de texto de prueba
└── README.md
```

---

# Word Frequency Analysis

## Description

This script reads a plain text file, cleans the content (ignoring uppercase, punctuation and special characters) and displays the 10 most frequent words along with their count and percentage of the total.

## Processing steps

| Step | What it does |
|---|---|
| Normalization | All text is converted to lowercase |
| Cleaning | Punctuation and special characters are removed |
| Tokenization | The text is split into individual words |
| Counting | Each word occurrence is counted |
| Result | The 10 most frequent words are displayed |

## Output

```
==================================================
TOP 10 PALABRAS MAS FRECUENTES
==================================================
#     PALABRA              VECES      %
--------------------------------------------------
1     de                      18   5.7%
2     la                      15   4.7%
...
==================================================
Total palabras: 318  |  Unicas: 163
```

## Usage

### Basic usage (defaults to `texto_prueba.txt`)

```bash
python frecuencia_palabras.py
```

### Passing a custom file as argument

```bash
python frecuencia_palabras.py my_file.txt
```

The file must be in `.txt` format with UTF-8 encoding.

## File Structure

```
.
├── frecuencia_palabras.py   # Main script
├── texto_prueba.txt         # Sample text file
└── README.md
```
