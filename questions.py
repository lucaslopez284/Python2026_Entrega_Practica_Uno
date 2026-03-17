import random
from random import sample 

# Diccionario de categorías
categories = {
    "lenguajes": ["python"],
    "conceptos": ["programa", "variable", "funcion", "bucle"],
    "tipos de datos": ["cadena", "entero", "lista"]
}

# Mostrar categorías disponibles
print("Categorías disponibles:")
for category in categories:
    print("-", category)

candidates_by_category = {}
# Armar las listas de palabras ordenadas por categoria, de manera que no se puedan repetir
for cat, words in categories.items():
    candidates_by_category[cat] = random.sample(words, len(words))

# Validar elección, repitiendo hasta que sea valida
while True: 
  # Elegir categoría
  option = input("Elegí una categoría: ").lower()
  if option in categories:
    print("¡Bienvenido al Ahorcado!")
    print()
    round = 1
    total_points = 0
    while candidates_by_category[option]:
      word = candidates_by_category[option].pop()
      guessed = []
      attempts = 6
      print(f"¡Comienza la ronda {round}!")
      print()
      while attempts > 0:
      # Mostrar progreso: letras adivinadas y guiones para las que faltan
        progress = ""
        for letter in word:
          if letter in guessed:
            progress += letter + " "
          else:
            progress += "_ "
        print(progress)
        # Verificar si el jugador ya adivinó la palabra completa
        if "_" not in progress:
          print("¡Ganaste!")
          break
        print(f"Intentos restantes: {attempts}")
        print(f"Letras usadas: {', '.join(guessed)}")
    
        letter = input("Ingresá una letra: ")
        # Validar que el caracter ingresado sea valido
        if len(letter) > 1 or not letter.isalpha(): 
          print(f"{letter} no es una letra o ingresó más de un carácter.")
        else:
          if letter in guessed:
            print("Ya usaste esa letra.")
          elif letter in word:
            guessed.append(letter)
            print("¡Bien! Esa letra está en la palabra.")
          else:
            guessed.append(letter)
            attempts -= 1
            print("Esa letra no está en la palabra.")
          print()
      else:
        print(f"¡Perdiste! La palabra era: {word}")

      print(f"Tu puntaje en la ronda {round} fue: {attempts}")
      total_points = total_points + attempts
      round = round + 1
      print()
    print("No hay mas palabras para la categoria seleccionada")
    print("La partida ha finalizado")
    print(f"Tu puntaje total fue: {total_points}")
    break
  else:
    print("Categoría inválida")
    