def quick_sort(lista):
    if len(lista) <= 1:
        return lista

    pivote = lista.keys[0]
    menores = [x for x in lista.keys[1:] if x < pivote]
    iguales = [x for x in lista.keys if x == pivote]
    mayores = [x for x in lista.keys[1:] if x > pivote]

    return quick_sort(menores) + iguales + quick_sort(mayores)
nombres = {}
print("Cuantos nombres desea ingresar?")
cont =int(input())
for a in range(cont):
    codigo = int(input("Codigo:"))
    nombres[codigo] = {
        codigo: codigo + 1,
    }
resultado = quick_sort(nombres)
print(resultado)