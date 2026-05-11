d1=0.15
d2=0.5
compra=int(input("INGRESE LA CANTIDAD DE ARTICULOS COMPRADOS: "))
if compra > 12:
    c=compra*d1
    print("OCN LA COMPRA DE MAS DE 12 ARTICULOS TIENE UN DESCUENTO DE:",c,"BS")
elif compra >=6 and compra <= 12:
    e=compra*0.5
    print("CON LA COMPRA DE 6 A 12 ARTICULOS TIENE UN DESCUENTO DE:",e,"BS")
else:
    print("NO TIENE DESCUENTO")

    