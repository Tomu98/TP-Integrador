from funciones.infos import info_algoritmos


def elegir_algoritmos():
    """ Permite al usuario seleccionar dos algoritmos de ordenamiento para comparar. """
    print("\n----- Algoritmos para seleccionar -----")
    print("  1. SelectionSort (Selección)")
    print("  2. InsertionSort (Inserción)")
    print("  3. BubbleSort (Burbuja)")
    print("  4. QuickSort (Rápido)")
    print("  5. MergeSort (Fusión)")
    print("  6. TimSort (Python)")

    # Elegir primer algoritmo
    while True:
        opcion1 = input("\nAlgoritmo 1: ").strip()
        if opcion1 in ["1", "2", "3", "4", "5", "6"]:
            break
        else:
            print("Opción no válida. Intente nuevamente.")

    # Elegir segundo algoritmo
    while True:
        opcion2 = input("Algoritmo 2: ").strip()
        if opcion2 not in ["1", "2", "3", "4", "5", "6"]:
            print("Opción no válida. Intente nuevamente.")
        elif opcion2 == opcion1:
            print("Debe elegir un algoritmo diferente al primero.")
        else:
            break

    return int(opcion1), int(opcion2)


def mostrar_info_algoritmos(alg1, alg2):
    """ Muestra información detallada sobre los algoritmos seleccionados. """
    print("\n----- Información de los algoritmos seleccionados -----\n")

    for idx, i in enumerate([alg1, alg2], start=1):
        info = info_algoritmos[i]
        print(f"• Algoritmo {idx}: {info['nombre']}")
        print(f"  - Descripción: {info['descripcion']}")
        print(f"  - Ventajas: {info['ventajas']}")
        print(f"  - Desventajas: {info['desventajas']}")
        print(f"  - Complejidad: {info['complejidad']}\n")

    input("Presiona Enter para continuar con la comparación...")


# Algoritmos de ordenamiento
def selection_sort(lista):
    n = len(lista)
    for i in range(n):
        indice_min = i
        for j in range(i+1, n):
            if lista[j] < lista[indice_min]:
                indice_min = j
        lista[i], lista[indice_min] = lista[indice_min], lista[i]
    return lista


def insertion_sort(lista):
    for i in range(1, len(lista)):
        temp = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > temp:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = temp
    return lista


def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista


def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    pivot = lista[len(lista) // 2]
    izq = [x for x in lista if x < pivot]
    medio = [x for x in lista if x == pivot]
    der = [x for x in lista if x > pivot]
    return quick_sort(izq) + medio + quick_sort(der)


def merge_sort(lista):
    if len(lista) <= 1:
        return lista
    mid = len(lista) // 2
    izq = merge_sort(lista[:mid])
    der = merge_sort(lista[mid:])
    return merge(izq, der)

def merge(izq, der):
    resultado = []
    i = j = 0
    while i < len(izq) and j < len(der):
        if izq[i] < der[j]:
            resultado.append(izq[i])
            i += 1
        else:
            resultado.append(der[j])
            j += 1
    resultado.extend(izq[i:])
    resultado.extend(der[j:])
    return resultado


def tim_sort(lista):
    return sorted(lista)
