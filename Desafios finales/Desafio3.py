Altura=float(input("Ingrese su altura: "))
Peso=float(input("Ingrese su peso: "))
IMC=float(Peso/(Altura*Altura))
if IMC < float(18.5):
    print("TIENE UN IMC BAJO",IMC)
elif IMC >=float(18.5) and IMC < float(24.9):
        print("TIENE UN IMC NORMAL",IMC)
elif IMC > float(25):
    print("TIENE SOBRE PESO",IMC)