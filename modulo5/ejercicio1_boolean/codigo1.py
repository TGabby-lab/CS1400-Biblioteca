# Practicando lógica booleana en Python aprendiendo a usar "and", "or" y "not"

# Declaracion de valores o inicialización de Valores para probar diferentes combinaciones
edad = 16
tiene_permiso = True
es_finde = False

# TODO 1: Usa una expresión booleana con "and"
# Por ejemplo: ¿Puede salir hoy solo si tiene 18 años o más Y si tiene permiso?
edad = input("¿Cuántos años tienes? ")
edad = int(edad)
print("¿Puede salir solo si tiene 18 años o más y tiene permiso?")
puede_salir = (edad >= 18) and tiene_permiso
print("puedes salir")





# TODO 2: Usa una expresión booleana con "or" para permitir salir si es fin de semana o tiene permiso
# Por ejemplo: ¿Puede salir si es fin de semana O si tiene permiso?
print("¿Puede salir si es fin de semana o si tiene permiso?")
puede_salir_finde = es_finde or tiene_permiso
print(puede_salir_finde)



# TODO 3: Usa una expresión booleana con "not" para negar una condición
# Por ejemplo: De ninguna manera tiene permiso
print("¿Tiene permiso?")
print(not tiene_permiso)    



# TODO 5: Escribe tu propia condición con and, or o not e imprimelo a la pantalla.
# Ejemplo: ¿Puede conducir si tiene 18 o más y tiene permiso? u cualquier otra idea. 
print("¿Puede conducir si tiene 18 o más y tiene permiso?")
puede_conducir = (edad >= 18) and tiene_permiso



