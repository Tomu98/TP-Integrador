from funciones.algoritmos import *
from funciones.generador_listas import generar_lista


def comparar_algoritmos():
    print("\n=== COMPARACIÓN DE DOS ALGORITMOS DE ORDENAMIENTO ===")

    alg1, alg2 = elegir_algoritmos()

    lista_original = generar_lista()

    copia1 = lista_original.copy()
    copia2 = lista_original.copy()

    print("Ejecutando algoritmos...")

    nombre1 = aplicar_algoritmo(alg1, copia1)
    print("Primer algoritmo finalizado.")
    nombre2 = aplicar_algoritmo(alg2, copia2)
    print("Segundo algoritmo finalizado.")

    print(f"\nAlgoritmos '{nombre1}' y '{nombre2}' ejecutados correctamente.\n")


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
