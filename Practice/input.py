nombre = input("Ingrese nombre ")

if nombre[-1].lower() in "aeiou":
  nombre = nombre[:-1] + "ito"
else:
  nombre += "ito"
  
  
print(f"Hola {nombre}! primer print eh?")