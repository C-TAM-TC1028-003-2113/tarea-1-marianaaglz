def main():
    # escribe tu código abajo de esta línea

"""
Se requieren 50 gramos de levadura para 1 kg.
de harina si se utiliza para la base de una
pizza. Realiza el cálculo de la levadura necesitada
a partir de los gramos de harina que indique el usuario.

Dame la harina en gramos: 1500
Necesitas estos gramos de levadura: 75.0
"""

    gramos_de_harina = float(input("Dame la harina en gramos: "))

    gramos_de_levadura = (gramos_de_harina*50)/1000
    print("Necesitas estos gramos de levadura:", gramos_de_levadura)

if __name__ == '__main__':
    main()
