nota=int(input("INGRESE SU NOTA: "))
if nota >= 90 and nota <= 100:
    print("A")
else:
    if nota >= 80 and nota <= 89:
        print("B")
    else:
        if nota >= 70 and nota <= 79:
            print("C")
        else:
            if nota >= 60 and nota <= 69:
                print("D")
            else:
                if nota >= 0 and nota <= 59:
                    print("F")