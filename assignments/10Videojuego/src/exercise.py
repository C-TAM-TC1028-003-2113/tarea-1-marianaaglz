def main():
    # escribe tu código abajo de esta línea

"""
Dame la cantidad de juegos nuevos: 2
Dame la cantidad de juegos usados: 3
El total de la compra es: 3050
"""

    juegos_nuevos = int(input("Dame la cantidad de juegos nuevos: "))
    juegos_usados = int(input("Dame la cantidad de juegos usados: "))

    total = ((juegos_nuevos*1000) + (juegos_usados*350))
    print("El total de la compra es:", total)

if __name__ == '__main__':
    main()
