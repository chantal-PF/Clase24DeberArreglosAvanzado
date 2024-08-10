# Crear un arreglo con palabras, incluyendo duplicados
palabra = ["Gato" , "Perro" , "Gato" , "Araña" , "Perro" , "Gato" , "Gallina" , "Pavo" , "Pavo"]
# Crear un nuevo arreglo para almacenar las plabras sin duplicados
palbra_sin_duplicados = []
# Recorrer el arreglo y agregar las oalbras no duplicados al nuevo arreglo
for letra in palabra:
 if letra not in palbra_sin_duplicados:
  palbra_sin_duplicados.append(letra)
# Mostrar el nuevo arreglo sin duplicados
print("Arreglo sin duplicados:", palbra_sin_duplicados)
