def main():
    # escribe tu código abajo de esta línea
    """
    Dame el número de mensajes: 38
    Dame el número de megas: 3.1
    Dame el número de minutos: 78
    El costo mensual es: 95.28
    """

    num_mensajes = int(input("Dame el número de mensajes: "))
    num_megas = float(input("Dame el número de megas: "))
    num_minutos = int(input("Dame el número de minutos: "))

    costo_mensual = ((num_mensajes*0.8) + (num_megas*0.8) + (num_minutos*0.8))
    print("El costo mensual es:", costo_mensual)

if __name__ == '__main__':
    main()
