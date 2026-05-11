Saldo=int(input("INGRESE SU SALDO: "))
RETIRO=int(input("INGRESE EL MONTO DESEADO A RETIRAR: "))
resta=Saldo-RETIRO
if Saldo > RETIRO:
    print("MONTO RETIRADO.LE QUEDA",resta,"DE SALDO")
else:
    print("SALDO INSUFICIENTE")