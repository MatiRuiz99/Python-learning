import random

rps = ["piedra","papel","tijera"]
state = False

while True:
    user = input("piedra papel o tijera? ")
    if user in rps:
        break

pc = random.choice(rps)

print(f"elegiste {user}")
print(f"PC eligio {pc}")

if user == pc: print("Empate!")
elif (user == "piedra" and pc == "tijera") or \
     (user == "papel" and pc == "piedra") or \
     (user == "tijera" and pc == "papel"):
    print("Ganaste!")
else: print("Perdiste!")