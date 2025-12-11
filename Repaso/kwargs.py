def imprimir(**kwargs):
    if "nombre" in kwargs:
        for clave, valor in kwargs.items():
            print(f"{clave}: {valor}")
    else:
        print("No se proporcionó un nombre.")

nombre = input("Introduce tu nombre: ")
edad = input("Introduce tu edad: ")

if nombre == "":
    print("El nombre está vacío")
    imprimir(edad=edad)
else:
    print("El usuario escribió algo")
    imprimir(nombre=nombre, edad=edad)
