from .models import Videojuego
from .services import (
    actualizar_videojuego,
    buscar_videojuego,
    calcular_valor_inventario,
    eliminar_videojuego,
    filtrar_por_plataforma,
    obtener_resumen,
    obtener_videojuego_mas_caro,
    registrar_videojuego,
)


def mostrar_menu():
    """Muestra las opciones principales del programa."""
    print("\n===== TIENDA DE VIDEOJUEGOS =====")
    print("1. Registrar videojuego")
    print("2. Mostrar videojuegos")
    print("3. Buscar videojuego")
    print("4. Actualizar videojuego")
    print("5. Eliminar videojuego")
    print("6. Calcular valor del inventario")
    print("7. Filtrar por plataforma")
    print("8. Mostrar videojuego más caro")
    print("9. Mostrar resumen")
    print("0. Salir")


def solicitar_entero(mensaje):
    """Solicita un número entero al usuario."""
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Error: introduce un número entero.")


def solicitar_float(mensaje):
    """Solicita un número decimal al usuario."""
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Error: introduce un número válido.")


def mostrar_videojuego(videojuego):
    """Muestra la información de un videojuego."""
    print(
        f"ID: {videojuego.id} | "
        f"Título: {videojuego.titulo} | "
        f"Plataforma: {videojuego.plataforma} | "
        f"Precio: ${videojuego.precio:.2f} | "
        f"Stock: {videojuego.stock}"
    )


def registrar(videojuegos):
    """Solicita datos y registra un videojuego."""
    try:
        videojuego = Videojuego(
            id=solicitar_entero("ID: "),
            titulo=input("Título: "),
            plataforma=input("Plataforma: "),
            precio=solicitar_float("Precio: "),
            stock=solicitar_entero("Stock: "),
        )

        registrar_videojuego(videojuegos, videojuego)
        print("Videojuego registrado correctamente.")

    except ValueError as error:
        print(f"Error: {error}")


def mostrar_todos(videojuegos):
    """Muestra todos los videojuegos."""
    if not videojuegos:
        print("No hay videojuegos registrados.")
        return

    for videojuego in videojuegos:
        mostrar_videojuego(videojuego)


def buscar(videojuegos):
    """Busca un videojuego mediante su ID."""
    videojuego_id = solicitar_entero("ID a buscar: ")
    videojuego = buscar_videojuego(videojuegos, videojuego_id)

    if videojuego is None:
        print("No se encontró ningún videojuego.")
    else:
        mostrar_videojuego(videojuego)


def actualizar(videojuegos):
    """Actualiza un videojuego existente."""
    videojuego_id = solicitar_entero("ID del videojuego: ")

    if buscar_videojuego(videojuegos, videojuego_id) is None:
        print("No se encontró ningún videojuego.")
        return

    try:
        actualizar_videojuego(
            videojuegos,
            videojuego_id,
            input("Nuevo título: "),
            input("Nueva plataforma: "),
            solicitar_float("Nuevo precio: "),
            solicitar_entero("Nuevo stock: "),
        )
        print("Videojuego actualizado correctamente.")

    except ValueError as error:
        print(f"Error: {error}")


def eliminar(videojuegos):
    """Elimina un videojuego."""
    videojuego_id = solicitar_entero("ID del videojuego: ")

    try:
        eliminar_videojuego(videojuegos, videojuego_id)
        print("Videojuego eliminado correctamente.")
    except ValueError as error:
        print(f"Error: {error}")


def mostrar_valor_inventario(videojuegos):
    """Muestra el valor total del inventario."""
    valor = calcular_valor_inventario(videojuegos)
    print(f"Valor total del inventario: ${valor:.2f}")


def mostrar_por_plataforma(videojuegos):
    """Muestra videojuegos filtrados por plataforma."""
    plataforma = input("Plataforma: ")
    resultados = filtrar_por_plataforma(videojuegos, plataforma)

    if not resultados:
        print("No se encontraron videojuegos para esa plataforma.")
        return

    for videojuego in resultados:
        mostrar_videojuego(videojuego)


def mostrar_mas_caro(videojuegos):
    """Muestra el videojuego más caro."""
    videojuego = obtener_videojuego_mas_caro(videojuegos)

    if videojuego is None:
        print("No hay videojuegos registrados.")
    else:
        mostrar_videojuego(videojuego)


def mostrar_resumen(videojuegos):
    """Muestra un resumen general."""
    resumen = obtener_resumen(videojuegos)

    print("\n===== RESUMEN =====")
    print(f"Videojuegos registrados: {resumen['cantidad_videojuegos']}")
    print(f"Unidades en stock: {resumen['unidades_stock']}")
    print(f"Valor del inventario: ${resumen['valor_inventario']:.2f}")


def main():
    """Ejecuta la aplicación."""
    videojuegos = []

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            registrar(videojuegos)
        elif opcion == "2":
            mostrar_todos(videojuegos)
        elif opcion == "3":
            buscar(videojuegos)
        elif opcion == "4":
            actualizar(videojuegos)
        elif opcion == "5":
            eliminar(videojuegos)
        elif opcion == "6":
            mostrar_valor_inventario(videojuegos)
        elif opcion == "7":
            mostrar_por_plataforma(videojuegos)
        elif opcion == "8":
            mostrar_mas_caro(videojuegos)
        elif opcion == "9":
            mostrar_resumen(videojuegos)
        elif opcion == "0":
            print("Programa finalizado.")
            break
        else:
            print("Opción no válida. Intenta nuevamente.")


if __name__ == "__main__":
    main()
