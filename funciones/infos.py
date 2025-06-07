def mostrar_instrucciones():
    """ Muestra las instrucciones de uso del programa """
    print("\n" + "="*40)
    print("========  INSTRUCCIONES DE USO  ========")
    print("="*40)
    print("\nEste programa te permite comparar el rendimiento de dos algoritmos de ordenamiento.")

    print("\nALGORTIMOS DISPONIBLES:")
    print("  1. Selection Sort (Ordenamiento por selección)")
    print("  2. Insertion Sort (Ordenamiento por inserción)")
    print("  3. Bubble Sort (Ordenamiento burbuja)")
    print("  4. Quick Sort (Ordenamiento rápido)")
    print("  5. Merge Sort (Ordenamiento por fusión)")
    print("  6. TimSort (Algoritmo de Python)")

    print("\nTIPOS DE LISTAS PARA PROBAR:")
    print("  - Lista aleatoria")
    print("  - Lista ya ordenada (de 1 a N)")
    print("  - Lista ordenada de forma inversa (de N a 1)")
    print("  (Podés elegir entre tamaños de 1.000, 10.000 o 30.000 elementos)")

    print("\nFUNCIONAMIENTO DEL PROGRAMA:")
    print("  • Cada algoritmo trabaja sobre una copia independiente de la lista.")
    print("  • Primero seleccionás los dos algoritmos a comparar.")
    print("  • Luego, el programa te muestra información resumida sobre cómo funciona cada uno.")
    print("  • A continuación, generás una lista de prueba.")
    print("  • Ambos algoritmos se ejecutan sobre la lista y se mide su tiempo de ejecución.")
    print("  • Finalmente, se muestra cuál fue más rápido y por cuánto.")

    print("\nPara comenzar, seleccioná la opción '1. Iniciar' desde el menú principal.")

    input("\nPresiona Enter para continuar...\n")


# Información de los algoritmos de ordenamiento
info_algoritmos = {
    1: {
        "nombre": "SelectionSort",
        "descripcion": "Recorre toda la lista buscando el mínimo y colocándolo en su posición correcta.",
        "ventajas": "Simple de implementar, sin estructura auxiliar.",
        "desventajas": "Ineficiente en listas grandes.",
        "complejidad": "O(n²) en todos los casos."
    },
    2: {
        "nombre": "InsertionSort",
        "descripcion": "Inserta cada elemento en la posición correcta en una lista ya ordenada.",
        "ventajas": "Bueno para listas pequeñas o casi ordenadas.",
        "desventajas": "Ineficiente en listas grandes y desordenadas.",
        "complejidad": "Mejor caso O(n), peor y promedio O(n²)."
    },
    3: {
        "nombre": "BubbleSort",
        "descripcion": "Intercambia elementos adyacentes si están en orden incorrecto.",
        "ventajas": "Fácil de entender e implementar.",
        "desventajas": "Muy ineficiente en la práctica.",
        "complejidad": "O(n²) en todos los casos."
    },
    4: {
        "nombre": "QuickSort",
        "descripcion": "Divide la lista usando un pivote, y ordena recursivamente las partes.",
        "ventajas": "Muy rápido en promedio, uso eficiente de memoria.",
        "desventajas": "Puede degradarse a O(n²) si el pivote es malo.",
        "complejidad": "Mejor/promedio O(n log n), peor caso O(n²)."
    },
    5: {
        "nombre": "MergeSort",
        "descripcion": "Divide la lista a la mitad, ordena cada parte y luego las combina.",
        "ventajas": "Muy estable y predecible en rendimiento.",
        "desventajas": "Uso adicional de memoria.",
        "complejidad": "Siempre O(n log n)."
    },
    6: {
        "nombre": "TimSort",
        "descripcion": "Algoritmo híbrido basado en mergesort e insertion sort, usado en Python.",
        "ventajas": "Altísimo rendimiento en la práctica, adaptativo.",
        "desventajas": "Complejo de implementar desde cero.",
        "complejidad": "Promedio y peor O(n log n)."
    }
}
