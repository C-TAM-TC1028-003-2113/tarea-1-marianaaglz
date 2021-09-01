def main():
    # escribe tu código abajo de esta línea

"""
Dame el saldo del mes anterior: 100.1
Dame los ingresos: 57.38
Dame los egresos: 5.23
Dame el número de cheques: 2
El saldo final de la cuenta es: 116.78125

Un banco cobra el 7.5% de interés mensual sobre
el saldo final de una cuenta. Además, cada cheque
expedido tiene un costo de 13 pesos. Realiza un programa
para obtener el saldo mensual de una cuenta en este banco
tomando en cuenta el saldo del mes anterior, los ingresos,
los egresos y el número de cheques expedidos.
"""

    saldo_mes_anterior = float(input("Dame el saldo del mes anterior: "))
    ingresos = float(input("Dame los ingresos: "))
    egresos = float(input("Dame los egresos: "))
    cheques = int(input("Dame el número de cheques: "))

    saldo_final = ((cheques*13) + saldo_mes_anterior + ingresos - egresos)
    interes_mensual = ((saldo_final*7.5)/100)
    print("El saldo final de la cuenta es:", saldo_final-interes_mensual)

if __name__ == '__main__':
    main()
