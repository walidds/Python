import make_pizza as pizza

tam = int(input("Introduce el tamaño de la pizza en porciones: "))
ingredientes = input("Introduce los ingredientes separados por espacios: ").split()

pizza.make_pizza(tam, *ingredientes)