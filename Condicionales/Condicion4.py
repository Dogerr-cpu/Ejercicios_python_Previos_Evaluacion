Nota=int(input("Ingrese su nota: "))
if Nota > 100:
    print("Ingrese una nota valida")
elif Nota >= 90:
    print ("EXCELENTE")
elif Nota >= 61 and Nota <= 89:
    print("APROBADO")
elif Nota < 61:
    print("REPROBADO")