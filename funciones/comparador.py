import time
from funciones.algoritmos import *
from funciones.generador_listas import generar_lista


def comparar_algoritmos():
    """ Compara dos algoritmos de ordenamiento seleccionados por el usuario. """
    print("\n" + "="*65)
    print("========  COMPARACIÓN DE DOS ALGORITMOS DE ORDENAMIENTO  ========")
    print("" + "="*65)

    while True:
        # Elegir algoritmos
        alg1, alg2 = elegir_algoritmos()

        # Mostrar información de los algoritmos seleccionados
        mostrar_info_algoritmos(alg1, alg2)

        # Generar lista
        lista_original = generar_lista()

        # Crear copias de la lista para cada algoritmo
        copia1 = lista_original.copy()
        copia2 = lista_original.copy()

        print("Ejecutando algoritmos...\n")

        # Algoritmo 1
        inicio1 = time.time()
        nombre1 = aplicar_algoritmo(alg1, copia1)
        fin1 = time.time()
        tiempo1 = fin1 - inicio1
        print(f"• Algoritmo 1 ({nombre1}): Ejecutado en {tiempo1:.4f} segundos")

        # Algoritmo 2
        inicio2 = time.time()
        nombre2 = aplicar_algoritmo(alg2, copia2)
        fin2 = time.time()
        tiempo2 = fin2 - inicio2
        print(f"• Algoritmo 2 ({nombre2}): Ejecutado en {tiempo2:.4f} segundos")

        # Comparación
        if tiempo1 < tiempo2:
            diferencia = abs(tiempo1 - tiempo2)
            porcentaje = (diferencia / tiempo2) * 100 if tiempo2 != 0 else 0
            print(f"\nEl más rápido fue '{nombre1}' con {diferencia:.4f} segundos de diferencia.")
            print(f"Siendo un {porcentaje:.2f}% más rápido que '{nombre2}'.\n")
        elif tiempo2 < tiempo1:
            diferencia = abs(tiempo2 - tiempo1)
            porcentaje = (diferencia / tiempo1) * 100 if tiempo1 != 0 else 0
            print(f"\nEl más rápido fue '{nombre2}' con {diferencia:.4f} segundos de diferencia.")
            print(f"Siendo un {porcentaje:.2f}% más rápido que '{nombre1}'.\n")
        else:
            print("\nAmbos algoritmos tardaron el mismo tiempo.\n")

        # Preguntar si quiere seguir comparando
        while True:
            continuar = input("¿Deseás comparar otros algoritmos? (s/n): ").strip().lower()
            if continuar in ["s", "si"]:
                break
            elif continuar in ["n", "no"]:
                print("\nRegresando al menú principal...\n")
                return
            else:
                print("Opción no válida. Ingrese 's/si' o 'n/no'.")


def aplicar_algoritmo(opcion, lista):
    """ Aplica el algoritmo seleccionado a la lista y devuelve su nombre. """
    match opcion:
        case 1:
            selection_sort(lista)
            return "SelectionSort"
        case 2:
            insertion_sort(lista)
            return "InsertionSort"
        case 3:
            bubble_sort(lista)
            return "BubbleSort"
        case 4:
            resultado = quick_sort(lista)
            lista[:] = resultado
            return "QuickSort"
        case 5:
            resultado = merge_sort(lista)
            lista[:] = resultado
            return "MergeSort"
        case 6:
            resultado = tim_sort(lista)
            lista[:] = resultado
            return "TimSort"
