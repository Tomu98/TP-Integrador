from funciones.comparador import comparar_algoritmos
from funciones.infos import mostrar_instrucciones


def mostrar_menu():
    """ Muestra el menú inicial del programa """
    print("\n" + "="*60)
    print("========  COMPARADOR DE ALGORITMOS DE ORDENAMIENTO  ========")
    print("" + "="*60)
    print("\n----- Menú principal -----")
    print("  1. Iniciar")
    print("  2. Como usar el programa")
    print("  3. Salir")


def main():
    while True:
        mostrar_menu()
        opcion = input("\nIngrese una opción (1-3): ").strip()

        match opcion:
            case "1":
                comparar_algoritmos()
            case "2":
                mostrar_instrucciones()
            case "3":
                print("\nSaliendo...")
                print("Gracias por usar el programa. ¡Hasta luego!\n")
                break
            case _:
                print("Opción no válida, por favor intente de nuevo.\n")


if __name__ == "__main__":
    main()
 