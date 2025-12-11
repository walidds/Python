salida = False

while not salida:
    print("\n1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

    opcion = int(input("Escoge una opción: "))

    if opcion == 5:
        print("Saliendo del programa...")
        salida = True
    else:
        num1 = float(input("Introduce el primer número: "))
        num2 = float(input("Introduce el segundo número: "))

        if opcion == 1:
            print("Suma:", num1 + num2)
        elif opcion == 2:
            print("Resta:", num1 - num2)
        elif opcion == 3:
            print("Multiplicación:", num1 * num2)
        elif opcion == 4:
            if num2 != 0:
                print("División:", num1 / num2)
            else:
                print("Error: No se puede dividir entre 0.")
        else:
            print("Opción no válida.")
