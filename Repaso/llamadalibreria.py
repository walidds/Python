import libreria as lib

numero1 = int(input("Introduce el primer numero:"))
numero2 = int(input("Introduce el segundo numero:"))

resultadosuma= lib.suma(numero1, numero2)
print("La suma da: ",resultadosuma)

resultadoresta= lib.resta(numero1, numero2)
print("La resta da: ",resultadoresta)

resultadomultiplicacion = lib.multiplicacion(numero1, numero2)
print("La multiplicaión da: ",resultadomultiplicacion)

resultadodivision = lib.division(numero1, numero2)
print("La división da: ",resultadodivision)