"""RETO 1 : CREAR UN PROGRAMA USANDO COMO EJEMPLO EL CODIGO DE LA CALCULADORA
QUE PERMITA CONVERTIR EL VALOR DE UNA MONEDA DE SOLES A DOLARES Y VICEVERSA,
POR EJEMPLO SI INGRESO CONVERTIR SOLES A DOLARES E INGRESO 3000 SOLES DEBERIA
MOSTRARME SU VALOR EN DOALRES QUE SERIA 1000 DOLARES CONSIDERANDO QUE EL TIPO 
DE CAMBIO ES 3"""
import os
from time import sleep
#datos de entrada
tipo_cambio = 3
moneda_origen = "soles"
moneda_destino = "dolares"
while True:
    os.system("clear")
    print("""
            =============================================
                        CONVERTIDOR DE MONEDAS
            =============================================
                    [1] CONVERTIR SOLES A DOLARES
                    [2] CONVERTIR DOLARES A SOLES
                    [3] SALIR
            =============================================
                """)

    opcion = int(input("Ingrese la opcion que desea (1-2-3): "))
    if(opcion == 1):
        moneda_origen = "soles"
        moneda_destino = "dolares"
        monto_origen = float(input(f"Ingrese el monto a convertir: "))
        #proceso
        monto_destino = monto_origen / tipo_cambio
    elif(opcion == 2):
        moneda_origen = "dolares"
        moneda_destino = "soles"
        monto_origen = float(input(f"Ingrese el monto a convertir: "))
        #proceso
        monto_destino = monto_origen * tipo_cambio
    elif(opcion == 3):
        print("Gracias por usar el covertidor de monedas")
        exit()
    else:
        print("Opcion no valida")
        continue
    #datos de salida
    print(f"El monto de {monto_origen} {moneda_origen} es igual a {monto_destino} {moneda_destino}")
    sleep(5)