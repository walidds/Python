def sumanumeros (a, b):
    resultado= a+b
    return resultado

def restanumeros (a, b):
    resultado= a-b
    return resultado

def multiplicacionnumeros (a, b):
    resultado= a*b
    return resultado

def divisionnumeros (a, b):
    if a!=0:
        resultado= a/b
        return resultado
    else:
        print("No se puede dividir entre 0")


salida = False

while not salida:
    print("\n1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

    opcion = int(input("Introduce tu  eleccion: "))

    if opcion==5:
        print("Saliendo... ")
        salida=True
    else:
        num1= float(input("Introduce el primer numero: "))
        num2= float(input("Introduce el segundo numero: "))

        if opcion==1:
            print(sumanumeros(num1, num2))
        elif opcion==2:
            print(restanumeros(num1, num2))
        elif opcion==3:
            print(multiplicacionnumeros(num1,num2))
        elif opcion==4:
            print(divisionnumeros(num1, num2))
        else:
            print("Opción inválida")

