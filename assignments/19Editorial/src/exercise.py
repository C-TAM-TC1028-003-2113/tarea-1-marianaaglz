def main():
    # escribe tu código abajo de esta línea

"""
Una editorial cobra 60 dólares por página
publicada y hace un descuento de 10% a los autores.
Además, la editorial tiene una política que indica que
475 palabras es una página. Realiza un programa que
indique cuál es el costo de una publicación a partir
de las palabras de la misma. Considera que se necesita
una página completa aunque el número de palabras sea menor a 475.

Ejemplo:
Dame el número de palabras: 500
El costo de la publicación es: 108.0
"""

    numero_de_palabras = int(input("Dame el numero de palabras: "))

    numero_de_paginas = round(numero_de_palabras / 475)
    descuento = (((numero_de_paginas * 60) * 10) / 100)
    costo_de_publicacion = ((numero_de_paginas * 60) - descuento)

    print("El costo de la publicacion es de:", costo_de_publicacion)

if __name__ == '__main__':
    main()
