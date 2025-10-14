#BUCLE FOR
for contador in range(1,11,2):
    print(contador)

#tabla de multiplicar
tabla = int(input("ingrese la tabla de multiplicar que desea ver: "))
for contador in range(1,13):
    resultado = tabla * contador
    print(f"{tabla} x {contador} = {resultado}")