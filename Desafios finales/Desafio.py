num1=float(input("INGRESE UN NUMERO: "))
num2=float(input("INGRESE OTRO NUMERO: "))
op=input("INGRESE SU OPERADOR: ")
if op=="+":
    print("LA SUMA ES:",num1+num2)
else:
    if op=="-":
     print("LA RESTA ES:",num1-num2)
    else:
       if op=="*":
          print("LA MULTIPLICACIÓN ES:",num1*num2)
       else:
          if op=="/":
             print("LA DIVISIÓN ES:",float(num1-num2))