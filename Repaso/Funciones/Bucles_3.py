def filtrar_pares(num):
    return 0




listaNums = [0]*10
for i in range (len(listaNums)):
    val=input(f"Introduce el número #{i + 1}: ")
    if(val.isdigit()):
        listaNums[i]=int(val)
    else:
        print("Debes introducir un numero válido. ")