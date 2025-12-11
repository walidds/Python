from Areas import areaCirculo, areaCuadrado, areaTriangulo

rad= int(input("introduce el radio para calcular el area de un circulo: "))

lad= int(input("introduce la longitud de un lado del cuadrado para calcular su area: "))

bas= int(input("introduce la base del triangulo: "))

alt= int(input("introduce la altura del triangulo: "))

print("Area del circulo: ",areaCirculo(rad))
print("Area cuadrado: ",areaCuadrado(lad))
print("Area triangulo: ",areaTriangulo(bas, alt))