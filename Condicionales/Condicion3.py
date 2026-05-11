j1=int(input("Ingresa el nivel de experiencia: "))
j2=int(input("Ingresa otro nivel de experiencia: "))
if j1 > j2:
    print("El jugador 1 tiene mayor experiencia")
elif j2 > j1:
    print("El jugador 2 tiene mayor experiencia")
elif j2==j1:
    print("Ambos jugadores tienen el mismo nivel de experiencia")
