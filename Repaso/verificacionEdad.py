

try:
    edad = int(input("Introduzca su edad: "))

    if edad>=18:
        print("Mayor de edad con: "+str(edad))
    elif edad<18:
        print("Menor de edad con: "+str(edad))
    else:
        print("Introduce un valor válido")
except:
    print("Error")