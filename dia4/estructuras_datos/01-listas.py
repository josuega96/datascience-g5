#LISTAS
# Una lista es una estructura de datos que permite almacenar una colección ordenada de elementos.
# Se definen utilizando corchetes [] y los elementos se separan por comas.
dias = ["lunes", "martes", "miércoles", "jueves", "viernes",]

#imprimir uno o varios dias
print(dias[0])
print(dias[4])
print(dias[1:4])

#agregar valores
dias.append("sábado")
dias.append("domingo")  
print(dias)

#eliminar valores
dias.pop() #elimina el último valor
dias.pop(3) #elimina el valor en la posición 3
print(dias)

#modificar valores
dias[3] = "Jueves"
dias[4] = "Viernes"
print(dias)

#recorrer la lista
for dia in dias:
    print(f"Hoy es {dia}")
    

