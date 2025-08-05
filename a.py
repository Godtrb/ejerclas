def quick_sort(lista):
    if len(lista) <= 1:
        return lista

    pivote = lista[0]
    menores = [x for x in lista[1:] if x < pivote]
    iguales = [x for x in lista if x == pivote]
    mayores = [x for x in lista[1:] if x > pivote]

    return quick_sort(menores) + iguales + quick_sort(mayores)
nombres = []
print("Cuantos nombres desea ingresar?")
cont =int(input())
for a in range(cont):
    nombre= input("Ingrese el nombre: ")
    nombres.append(nombre)
resultado = quick_sort(nombres)
print(resultado)