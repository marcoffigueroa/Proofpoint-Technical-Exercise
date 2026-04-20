import re
import sys
from collections import Counter
from pathlib import Path

TOP_N = 10

# Para que el script funcione, se necesita un archivo .txt en el mismo directorio,
# o se puede pasar la ruta como argumento: python frecuencia_palabras.py mi_texto.txt


def cargar_texto(ruta):
    """Lee el archivo y devuelve su contenido, o termina con mensaje de error."""
    try:
        with open(ruta, encoding="utf-8") as archivo:
            return archivo.read()
    except FileNotFoundError:
        print(f"[ERROR] No se encontro el archivo: '{ruta}'")
        sys.exit(1)


def limpiar_texto(texto):
    """Convierte a minusculas y elimina puntuacion y caracteres especiales."""
    return re.sub(r"[^a-z0-9áéíóúüñ\s]", " ", texto.lower())


def mostrar_resultados(contador):
    """Muestra las TOP_N palabras mas frecuentes con frecuencia y porcentaje."""
    total = sum(contador.values())

    print("=" * 50)
    print("TOP 10 PALABRAS MAS FRECUENTES")
    print("=" * 50)
    print(f"{'#':<5} {'PALABRA':<20} {'VECES':>6}   {'%':>6}")
    print("-" * 50)

    for pos, (palabra, freq) in enumerate(contador.most_common(TOP_N), start=1):
        print(f"{pos:<5} {palabra:<20} {freq:>6}   {freq/total*100:>5.1f}%")

    print("=" * 50)
    print(f"Total palabras: {total}  |  Unicas: {len(contador)}")


def main():
    ruta = sys.argv[1] if len(sys.argv) > 1 else Path(__file__).parent / "texto_prueba.txt"

    contenido = cargar_texto(ruta)
    palabras = limpiar_texto(contenido).split()
    contador = Counter(palabras)
    mostrar_resultados(contador)


if __name__ == "__main__":
    main()
