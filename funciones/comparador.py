import time
from funciones.algoritmos import *
from funciones.generador_listas import generar_lista


def comparar_algoritmos():
    print("\n" + "="*65)
    print("========  COMPARACIÓN DE DOS ALGORITMOS DE ORDENAMIENTO  ========")
    print("" + "="*65)

    while True:
        # Elegir algoritmos
        alg1, alg2 = elegir_algoritmos()

        # Generar lista
        lista_original = generar_lista()

        # Crear copias de la lista para cada algoritmo
        copia1 = lista_original.copy()
        copia2 = lista_original.copy()

        print("Ejecutando algoritmos...")

        # Algoritmo 1
        inicio1 = time.time()
        nombre1 = aplicar_algoritmo(alg1, copia1)
        fin1 = time.time()
        tiempo1 = fin1 - inicio1
        print(f"Algoritmo 1 ({nombre1}): Ejecutado en {tiempo1:.4f} segundos")

        # Algoritmo 2
        inicio2 = time.time()
        nombre2 = aplicar_algoritmo(alg2, copia2)
        fin2 = time.time()
        tiempo2 = fin2 - inicio2
        print(f"Algoritmo 2 ({nombre2}): Ejecutado en {tiempo2:.4f} segundos")

        # Comparación
        if tiempo1 < tiempo2:
            print(f"\nEl más rápido fue {nombre1} con {abs(tiempo1 - tiempo2):.4f} segundos de diferencia.\n")
        elif tiempo2 < tiempo1:
            print(f"\nEl más rápido fue {nombre2} con {abs(tiempo2 - tiempo1):.4f} segundos de diferencia.\n")
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
    match opcion:
        case 1:
            ordenamiento_seleccion(lista)
            return "Selección"
        case 2:
            ordenamiento_insercion(lista)
            return "Inserción"
        case 3:
            ordenamiento_burbuja(lista)
            return "Burbuja"
        case 4:
            resultado = ordenamiento_rapido(lista)
            lista[:] = resultado
            return "Quicksort"
