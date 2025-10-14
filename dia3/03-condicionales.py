#CALCULADORA
#ENTRADA
numero1 = int(input("ingrese el primer numero: "))
numero2 = int(input("ingrese el segundo numero: "))
operacion = input("ingrese la operacion (+, -, *, /): ")
#PROCESO
if operacion == "+":
    resultado = numero1 + numero2
elif operacion == "-":
    resultado = numero1 - numero2
elif operacion == "*":
    resultado = numero1 * numero2
elif operacion == "/":
    if numero2 != 0:
        resultado = numero1 / numero2
    else:
        resultado = "Error: Division por cero"
else:
    print("Operacion no valida")
    exit()
#SALIDA
print(f"el resultado de la operacion {operacion} entre {numero1} y {numero2} es: {resultado}")
