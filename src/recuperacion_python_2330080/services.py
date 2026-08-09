def validar_videojuego(videojuego):
    """Valida los datos de un videojuego."""
    if videojuego.id <= 0:
        raise ValueError("El ID debe ser mayor que cero.")

    if not videojuego.titulo.strip():
        raise ValueError("El título no puede estar vacío.")

    if not videojuego.plataforma.strip():
        raise ValueError("La plataforma no puede estar vacía.")

    if videojuego.precio < 0:
        raise ValueError("El precio no puede ser negativo.")

    if videojuego.stock < 0:
        raise ValueError("El stock no puede ser negativo.")


def registrar_videojuego(videojuegos, videojuego):
    """Registra un videojuego si sus datos son válidos y el ID no existe."""
    validar_videojuego(videojuego)

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

    validar_videojuego(videojuego)


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


def obtener_resumen(videojuegos):
    """Devuelve un resumen general del inventario."""
    cantidad_videojuegos = len(videojuegos)
    unidades_stock = sum(videojuego.stock for videojuego in videojuegos)
    valor_inventario = calcular_valor_inventario(videojuegos)

    return {
        "cantidad_videojuegos": cantidad_videojuegos,
        "unidades_stock": unidades_stock,
        "valor_inventario": valor_inventario,
    }
