Edad=int(input("INGRESE SU EDAD: "))
if Edad > 0 and Edad <=12:
    print("ES UN NIÑO")
elif Edad >= 13 and Edad <=17:
    print("ES UN ADOLESCENTE")
elif Edad >= 18 and Edad <= 64:
    print ("ES UN ADULTO")
elif Edad > 65:
    print("adulto mayor")