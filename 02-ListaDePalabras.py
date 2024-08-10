# Crear un arreglo con algunas palabras
palabras = ["Lindo", "Chanty", "Miedo", "Chanty", "Gato", "Chanty", "Amigos", "Parejas"]
# Elegir el número que queremos contar
palb_a_contar = palabras[1]
# Inicializar una variable para contar las ocurrencias
contador = 0
# Recorrer el arreglo y contar las veces que aparece la palabra
for letra in palabras:
 if letra == palb_a_contar:
  contador += 1
# Mostrar la palabra de veces que aparece la palabra
print(f"La palabra {palb_a_contar} aparece {contador} vez en el arreglo.")
