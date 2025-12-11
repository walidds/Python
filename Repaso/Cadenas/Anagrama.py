analizar = input("Introduce que crees que es un anagrama")
analizar = analizar.replace(" ", "")

inversa = analizar[::-1]

if (analizar == inversa):
    print("El anagrama es correcto")
else:
    print("El anagrama no es correcto")
