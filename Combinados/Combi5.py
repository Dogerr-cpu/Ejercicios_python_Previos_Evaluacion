import random
secreto=random.randint(1,10)
while True:
    NUM=int(input("INGRESA UN NUMERO PARA VER SI LOGRAS ADIVINAR: "))
    if NUM==secreto:
        print("¡haz acertado!")
        break
    elif NUM < secreto:
        print("MAS ALTO")
    elif NUM > secreto:
        print("MAS BAJO")
    elif NUM==secreto:
        print("¡HAZ ACERTADO!")
   