def quick_sort(lista):
    if len(lista) <= 1:
        return lista

    pivote = lista.value[0]
    menores = [x for x in lista.value[1:] if x < pivote]
    iguales = [x for x in lista.value if x == pivote]
    mayores = [x for x in lista.value[1:] if x > pivote]

    return quick_sort(menores) + iguales + quick_sort(mayores)
nombres = {}
nombres[1] = {
    "nombres": {}
}
print("Cuantos nombres desea ingresar?")
cont =int(input())
for a in range(cont):
    codigo = input("")
    nombres[1]["nombres"]=

resultado = quick_sort(nombres)
print(resultado)