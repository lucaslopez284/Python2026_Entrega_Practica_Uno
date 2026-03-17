import random

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

# Validar elección, repitiendo hasta que sea valida
while True: 
  # Elegir categoría
  option = input("Elegí una categoría: ").lower()
  if option in categories:
    word = random.choice(categories[option])
    # Cortar el loop cuando la categoria seleccionada es correcta
    break 
  else:
    print("Categoría inválida")
    


guessed = []
attempts = 6
points = 6

print("¡Bienvenido al Ahorcado!")
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
      points -= 1
      print("Esa letra no está en la palabra.")
    print()
else:
  print(f"¡Perdiste! La palabra era: {word}")

print(f"Tu puntaje fue: {points}")