def elegir_algoritmos():
    print("\nElige dos algoritmos diferentes:")
    print("1. Ordenamiento por selección")
    print("2. Ordenamiento por inserción")
    print("3. Ordenamiento burbuja")
    print("4. Ordenamiento rápido (quicksort)")

    # Elegir primer algoritmo
    while True:
        opcion1 = input("\nAlgoritmo 1: ").strip()
        if opcion1 in ["1", "2", "3", "4"]:
            break
        else:
            print("Opción no válida. Intente nuevamente.")

    # Elegir segundo algoritmo
    while True:
        opcion2 = input("Algoritmo 2: ").strip()
        if opcion2 not in ["1", "2", "3", "4"]:
            print("Opción no válida. Intente nuevamente.")
        elif opcion2 == opcion1:
            print("Debe elegir un algoritmo diferente al primero.")
        else:
            break

    return int(opcion1), int(opcion2)


def ordenamiento_seleccion(lista):
    n = len(lista)
    for i in range(n):
        indice_min = i
        for j in range(i+1, n):
            if lista[j] < lista[indice_min]:
                indice_min = j
        lista[i], lista[indice_min] = lista[indice_min], lista[i]
    return lista


def ordenamiento_insercion(lista):
    for i in range(1, len(lista)):
        temp = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > temp:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = temp
    return lista


def ordenamiento_burbuja(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista


def ordenamiento_rapido(lista):
    if len(lista) <= 1:
        return lista
    pivot = lista[len(lista) // 2]
    izq = [x for x in lista if x < pivot]
    medio = [x for x in lista if x == pivot]
    der = [x for x in lista if x > pivot]
    return ordenamiento_rapido(izq) + medio + ordenamiento_rapido(der)