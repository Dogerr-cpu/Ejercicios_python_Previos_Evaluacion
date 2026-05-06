num1=int(input("ingrese un numero: "))
num2=int(input("Ingrese otro numero: "))
if num1==num2:
    print("Son iguales")
else:
    if num1 > num2:
        print(num1,"es mayor que",num2)
    else:
        if num2 > num1:
            print(num2,"es mayor que",num1)
