Año=int(input("INGRESE EL AÑO ACTUAL: "))
carrera=int(input("EN QUE AÑO TERMINARAS TU CARRERA: "))
Final=carrera-Año
if Final==1:
    print("¡CASI TERMINAS!")
else:
    print("te faltan",Final,"años")