from random import randint


def generar_lista_aleatoria(n):
    return [randint(1, n) for _ in range(n)]

def generar_lista_ordenada(n):
    return list(range(1, n + 1))

def generar_lista_ordenada_inver(n):
    return list(range(n, 0, -1))


def generar_lista():
    """ Genera una lista de prueba según las opciones del usuario """
    print("\n----- Tamaño de la lista -----")
    print("  1. Pequeña (1.000 elementos)")
    print("  2. Mediana (10.000 elementos)")
    print("  3. Grande (30.000 elementos)")

    while True:
        tam_op = input("\nSeleccione el tamaño: ").strip()
        if tam_op == "1":
            n = 1000
            break
        elif tam_op == "2":
            n = 10000
            break
        elif tam_op == "3":
            n = 30000
            break
        else:
            print("Opción no válida. Intente nuevamente.")

    print("\n----- Tipo de lista -----")
    print("  1. Aleatoria")
    print("  2. Ordenada")
    print("  3. Ordenada invertida")

    while True:
        tipo_op = input("\nSeleccione el tipo: ").strip()
        if tipo_op in ["1", "2", "3"]:
            match tipo_op:
                case "1":
                    lista = generar_lista_aleatoria(n)
                case "2":
                    lista = generar_lista_ordenada(n)
                case "3":
                    lista = generar_lista_ordenada_inver(n)

            print(f"\nLista generada con {n} elementos.")
            print(f"Inicio: {lista[:5]} ... {lista[-5:]} Fin.\n")
            return lista
        else:
            print("Opción no válida. Intente nuevamente.")
