"""
Este programa debe darle al usuario la opción de elegir una comida de una lista.
El código asegura que lo ingresado sea legible (en minúsculas) y lo compara con una lista usando lógica if/else.
Al final, muestra un mensaje explicando de dónde es originaria esa comida.
"""

# TODO #1:
# Imprime un mensaje de bienvenida al programa de comidas de Latinoamérica.
print("Bienvenido al programa de comidas de Latinoamérica.")

# TODO #2:
# Muestra al usuario una lista de al menos 5 opciones de comidas para elegir.

print("Opciones: tacos, gorditas, baho, pupusas, enchiladas")
    
# TODO #3:
# Guarda lo que el usuario escribió en una variable llamada `comida`.
comida = input("¿Qué comida quieres conocer? ")

# TODO #4:
# Convierte lo ingresado a minúsculas para asegurar la comparación correcta.
comida = comida.lower()

# TODO #5:
# Usa una estructura if / elif / else para verificar la comida elegida.
# Imprime un mensaje con el país de origen para cada comida.
if comida == "tacos":
    print("Los tacos son típicos de México.")
elif comida == "gorditas":
    print("Las gorditas son típicas de Guatemala.")
elif comida == "baho":
    print("El baho es típico de El Salvador.")
elif comida == "pupusas":
    print("Las pupusas son típicas de El Salvador.")
elif comida == "enchiladas":
    print("Las enchiladas son típicas de México.")
else:
    print("No tenemos información sobre esa comida.")

## Ejemplo de salida esperada:
"""
Bienvenido al programa de comidas de Latinoamérica.
Opciones: tacos, arepas, ceviche, pupusas, empanadas
¿Qué comida quieres conocer? Tacos
Los tacos son típicos de México.
"""
