import random
# Lista de palabras posibles
words = ["python", "programación", "computadora", "código", "desarrollo",
"inteligencia"]
# Elegir una palabra al azar
secret_word = random.choice(words)
# Número máximo de intentos permitidos
max_fails = 5
i = 0
# Lista para almacenar las letras adivinadas
guessed_letters = []
print("¡Bienvenido al juego de adivinanzas!")
print ("Elige la dificultad del juego (FACIL-MEDIA-DIFICIL)")
# Se ingresa el modo elegido 
dificultad = input("Ingresar:")

# Mostrarla palabra parcialmente adivinada segun su dificultad
if dificultad == "FACIL" :
   revealed_letters = ['a','e','i','o','u']
elif dificultad == "MEDIA":
   revealed_letters = [secret_word[0],secret_word[-1]]
else:
  revealed_letters = []

print("Estoy pensando en una palabra. ¿Puedes adivinar cuál es?")
word_displayed = "" 
for letter in secret_word:
  if letter in revealed_letters:
    word_displayed += letter
  else:
     word_displayed += "_"

#Mostrar la palbra parcialmente adivinada
print(f"Palabra: {word_displayed}")


while i < max_fails:
 # Pedir al jugador que ingrese una letra
 letter = input("Ingresa una letra: ").lower()

#Verifico si se ingreso o no una letra
 if not letter:
   print ("Error!! no has ingresado una letra.")
   continue

 # Verificar si la letra ya ha sido adivinada
 if letter in guessed_letters:
   print("Ya has intentado con esa letra. Intenta con otra.")
   continue
 
 # Verificar si la letra está en la palabra secreta
 if letter in secret_word:
   # Agregar la letra a la lista de letras adivinadas
   guessed_letters.append(letter)
   print("¡Bien hecho! La letra está en la palabra.")
 else:
   print("Lo siento, la letra no está en la palabra.")
   # Incrementar el numero de fallos
   i += 1

 # Mostrar la palabra parcialmente adivinada
 letters = []
 for letter in secret_word:
   if letter in guessed_letters or letter in revealed_letters:
     letters.append(letter)
   else:
     letters.append("_")
 word_displayed = "".join(letters)
 print(f"Palabra: {word_displayed}")
 # Verificar si se ha adivinado la palabra completa
 if word_displayed == secret_word:
   print(f"¡Felicidades! Has adivinado la palabra secreta: {secret_word}")
   break
else:
  print(f"¡Oh no! Has fallado {max_fails} veces. Has perdido, lo siento!")
  print(f"La palabra secreta era: {secret_word}")
 