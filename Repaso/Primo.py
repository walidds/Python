numero = int(input("Introduce un numero: "))

if numero<=1:
    print("No primo")
else:
    primo = True
    for i in range(2, numero):
        if numero % i == 0:
            primo=False
            break

    if primo:
        print("Es primo")
    else:
        print("No es primo")
        
        