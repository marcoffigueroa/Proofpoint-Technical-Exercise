import csv
from collections import defaultdict
from datetime import datetime

AUTOR_DESCONOCIDO = "Author Unknown"
ANIO_INVALIDO = 0
ANIO_MINIMO = -3000
ANIO_MAXIMO = datetime.now().year

#Para que el script funcione, se necesita un archivo "books.csv" con las columnas: Title, Author, Publication Year.
#En el mismo directorio que este script, o ajustar la ruta en la variable ruta_csv del main().

def limpiar_titulo(titulo):
    """Devuelve el titulo limpio, o None si esta vacio (registro invalido)."""
    if not titulo or not titulo.strip():
        return None
    return titulo.strip()


def limpiar_autor(autor):
    """Si no hay autor, devuelve 'Author Unknown'."""
    if not autor or not autor.strip():
        return AUTOR_DESCONOCIDO
    return autor.strip()


def limpiar_anio(anio):
    """
    Valida el anio de publicacion.
    Devuelve 0 si el anio es invalido (no es numero, negativo muy grande, o futuro lejano).
    """
    if not anio or not anio.strip():
        return ANIO_INVALIDO

    try:
        anio_num = int(anio.strip())
    except ValueError:
        return ANIO_INVALIDO

    if anio_num < ANIO_MINIMO or anio_num > ANIO_MAXIMO:
        return ANIO_INVALIDO

    return anio_num


def cargar_libros(ruta_csv):
    """
    Lee el CSV, limpia cada registro y elimina duplicados usando un set.
    Devuelve una lista de tuplas (titulo, autor, anio).
    """
    libros_unicos = set()
    descartados = 0

    with open(ruta_csv, mode="r", encoding="utf-8", newline="") as archivo:
        lector = csv.DictReader(archivo)

        for nro_fila, fila in enumerate(lector, start=2): 
            titulo = limpiar_titulo(fila.get("Title", ""))

            if titulo is None:
                descartados += 1
                print(f"[AVISO] Fila {nro_fila} descartada: falta el titulo.")
                continue

            autor = limpiar_autor(fila.get("Author", ""))
            anio = limpiar_anio(fila.get("Publication Year", ""))

            libros_unicos.add((titulo, autor, anio))

    print(f"\n[INFO] Libros unicos cargados: {len(libros_unicos)}")
    print(f"[INFO] Registros descartados: {descartados}\n")

    return sorted(libros_unicos, key=lambda libro: (libro[1], libro[2], libro[0]))


def mostrar_catalogo(libros):
    """
    Muestra los libros agrupados por autor.
    Los libros con autor desconocido se agrupan por anio de publicacion.
    """
    con_autor = defaultdict(list)
    sin_autor = defaultdict(list)

    for titulo, autor, anio in libros:
        if autor == AUTOR_DESCONOCIDO:
            sin_autor[anio].append(titulo)
        else:
            con_autor[autor].append((titulo, anio))

    print("=" * 60)
    print("CATALOGO - Libros con autor conocido")
    print("=" * 60)

    for autor in sorted(con_autor.keys()):
        print(f"\n{autor}")
        for titulo, anio in sorted(con_autor[autor], key=lambda x: x[1]):
            anio_mostrado = anio if anio != ANIO_INVALIDO else "Anio desconocido"
            print(f"   - {titulo} ({anio_mostrado})")

    if sin_autor:
        print("\n" + "=" * 60)
        print(f"CATALOGO - {AUTOR_DESCONOCIDO}")
        print("=" * 60)

        for anio in sorted(sin_autor.keys()):
            anio_mostrado = anio if anio != ANIO_INVALIDO else "Anio desconocido"
            print(f"\nAnio: {anio_mostrado}")
            for titulo in sorted(sin_autor[anio]):
                print(f"   - {titulo}")

    print("\n" + "=" * 60)
    print(f"TOTAL DE LIBROS EN EL CATALOGO: {len(libros)}")
    print("=" * 60)


def main():
    ruta_csv = "books.csv"
    libros = cargar_libros(ruta_csv)
    mostrar_catalogo(libros)


if __name__ == "__main__":
    main()
