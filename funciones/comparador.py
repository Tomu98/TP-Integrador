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

        # Aplicar ambos algoritmos
        nombre1 = aplicar_algoritmo(alg1, copia1)
        print("Primer algoritmo finalizado.")
        nombre2 = aplicar_algoritmo(alg2, copia2)
        print("Segundo algoritmo finalizado.")

        print(f"\nAlgoritmos '{nombre1}' y '{nombre2}' ejecutados correctamente.\n")

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
