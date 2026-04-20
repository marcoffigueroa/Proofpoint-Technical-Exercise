# Análisis de Frecuencia de Palabras

## Descripción

Este script lee un archivo de texto plano, limpia el contenido (ignorando mayúsculas, puntuación y caracteres especiales) y muestra las 10 palabras más frecuentes junto con su cantidad de apariciones y porcentaje sobre el total.

## Procesamiento aplicado

| Paso | Qué se hace |
|---|---|
| Normalización | Todo el texto se convierte a minúsculas |
| Limpieza | Se eliminan signos de puntuación y caracteres especiales |
| Tokenización | El texto se divide en palabras individuales |
| Conteo | Se cuenta cuántas veces aparece cada palabra |
| Resultado | Se muestran las 10 palabras con mayor frecuencia |

## Salida

```
==================================================
ANALISIS DE FRECUENCIA DE PALABRAS
==================================================
Total de palabras procesadas : 312
Total de palabras unicas     : 148
==================================================
TOP 10 PALABRAS MAS FRECUENTES
==================================================
#     PALABRA              FRECUENCIA    % DEL TEXTO
--------------------------------------------------
1     la                           28         8.97%
2     de                           27         8.65%
...
==================================================
```

## Uso

### Forma básica (usa `texto_prueba.txt` por defecto)

```bash
python frecuencia_palabras.py
```

### Pasando un archivo propio como argumento

```bash
python frecuencia_palabras.py mi_archivo.txt
```

El archivo debe estar en formato `.txt` con codificación UTF-8.

## Estructura del proyecto

```
.
├── frecuencia_palabras.py   # Script principal
├── texto_prueba.txt         # Archivo de texto de prueba
└── README.md
```
