from .models import Videojuego


def registrar_videojuego(videojuegos, videojuego):
    """Registra un videojuego si su ID no está duplicado."""
    if buscar_videojuego(videojuegos, videojuego.id) is not None:
        raise ValueError("El ID del videojuego ya existe.")

    videojuegos.append(videojuego)


def listar_videojuegos(videojuegos):
    """Devuelve todos los videojuegos registrados."""
    return videojuegos.copy()


def buscar_videojuego(videojuegos, videojuego_id):
    """Busca un videojuego mediante su ID."""
    for videojuego in videojuegos:
        if videojuego.id == videojuego_id:
            return videojuego

    return None


def actualizar_videojuego(
    videojuegos,
    videojuego_id,
    titulo,
    plataforma,
    precio,
    stock,
):
    """Actualiza los datos de un videojuego."""
    videojuego = buscar_videojuego(videojuegos, videojuego_id)

    if videojuego is None:
        raise ValueError("El videojuego no existe.")

    videojuego.titulo = titulo
    videojuego.plataforma = plataforma
    videojuego.precio = precio
    videojuego.stock = stock


def eliminar_videojuego(videojuegos, videojuego_id):
    """Elimina un videojuego mediante su ID."""
    videojuego = buscar_videojuego(videojuegos, videojuego_id)

    if videojuego is None:
        raise ValueError("El videojuego no existe.")

    videojuegos.remove(videojuego)


def calcular_valor_inventario(videojuegos):
    """Calcula el valor total del inventario."""
    return sum(videojuego.precio * videojuego.stock for videojuego in videojuegos)


def filtrar_por_plataforma(videojuegos, plataforma):
    """Devuelve los videojuegos de una plataforma determinada."""
    return [
        videojuego
        for videojuego in videojuegos
        if videojuego.plataforma.lower() == plataforma.lower()
    ]


def obtener_videojuego_mas_caro(videojuegos):
    """Devuelve el videojuego con mayor precio."""
    if not videojuegos:
        return None

    return max(videojuegos, key=lambda videojuego: videojuego.precio)