frase = input("Introduce una frase: ")

letra = input("Introduce una letra: ").lower()

contador = frase.lower().count(letra)

frase_modificada = ""
for caracter in frase:
    if caracter.lower() == letra:
        frase_modificada += "*"
    else:
        frase_modificada += caracter

print("\n--- RESULTADOS ---")
print("Frase original:", frase)
print("Letra buscada:", letra)
print("Número de apariciones:", contador)
print("Frase modificada:", frase_modificada)
