compra=int(input("Ingrese el precio total de su compra: "))
if compra > 100:
    Descuento=compra*0.10
    Precio_final=compra-Descuento
    print("con compras mayores a 100 se aplica un descuento del 10%:",Precio_final)
else:
    print("El precio final es: ",compra)