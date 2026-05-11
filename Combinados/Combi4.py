Contra= input("Cree su contraseña: ")
if len(Contra) > 10:
    print("CONTRASEÑA CREADA")
else:
    Fallo=10-len(Contra)
    print("A LA CONTRASEÑA LE FALTAN",Fallo,"CARACTERES")
