horas=input("Introduce las horas trabajadas: ")

try:
    horas=int(horas)
except:
    print("Valor incorrecto")
    exit()

int(horas)
if horas>40:
    horasnormales=40
    horastrabajadas=horas-40
    salario=(horasnormales*10)+(horastrabajadas*15)
else:
    salario=horas*10


print(salario)