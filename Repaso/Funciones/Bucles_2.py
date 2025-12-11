def tablaMultiplicar (num, hasta=10):
    for i in range(1, hasta+1):
        resultado = num * i
        print(f"{num} * {i} = {resultado}")


numero=int(input("Introduce el numero en cuestión: "))
rango = int(input("Introduce el numero de multiplicaciones a imprimir: "))
tablaMultiplicar(numero, rango)

