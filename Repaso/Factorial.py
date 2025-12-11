def factorial (numero):
    if numero==0:
        return 1
    else:
        return numero*factorial(numero-1)

num=int(input("Introduce un numero para calcular su factorial: "))
print(factorial(num))