def secuencia(numero):
    a=0
    b=1

    for i in range (numero+1):
        a=b
        b=a+b



num=int(input("Introduce la cantidad de numeros a imprimir"))
print(secuencia(num))
