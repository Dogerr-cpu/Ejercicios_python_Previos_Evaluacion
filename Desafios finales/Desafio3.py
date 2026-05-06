Altura=float(input("Ingrese su altura: "))
Peso=float(input("Ingrese su peso: "))
IMC=Altura/(Peso*Peso)
if IMC < float(18.5):
    print("TIENE UN IMC BAJO")
else:
    if IMC >=float(18.5) and IMC < float(24.9):
        print("TIENE UN IMC NORMAL")
        if IMC > float(25):
            print("TIENE SOBRE PESO")