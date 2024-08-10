# Crear un arreglo con 7 números
numeros = [27, 35, 10, 12, 53, 97 , 99]
# Inicializar una variable para almacenar el valor minimo
minimo = numeros[0]
# Recorrer el arreglo para encontrar el minimo
for numero in numeros:
 if numero < minimo:
  minimo = numero
# Mostrar el valor minimo
print("El valor minimo es:", minimo)
