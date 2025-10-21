#FUNCIONES EN PYTHON
# Una función es un bloque de código reutilizable que realiza una tarea específica.
# Se define utilizando la palabra clave def seguida del nombre de la función y paréntesis ().

def saludar(nombre):
    """Función que saluda a una persona por su nombre."""
    return f"Hola, {nombre}!"

nombre_usuario = input("Hola como te llamas? ")
print(saludar(nombre_usuario))

def sumar(a, b):
    """Función que suma dos números."""
    resultado = a + b
    return resultado

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
resultado_suma = sumar(num1, num2)
print(f"La suma de {num1} + {num2} es: {resultado_suma}")