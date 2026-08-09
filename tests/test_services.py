import pytest

from recuperacion_python_2330080.models import Videojuego
from recuperacion_python_2330080.services import (
    actualizar_videojuego,
    buscar_videojuego,
    calcular_valor_inventario,
    eliminar_videojuego,
    filtrar_por_plataforma,
    listar_videojuegos,
    obtener_resumen,
    obtener_videojuego_mas_caro,
    registrar_videojuego,
)


@pytest.fixture
def videojuegos():
    return [
        Videojuego(
            id=1,
            titulo="Minecraft",
            plataforma="PC",
            precio=599.99,
            stock=10,
        ),
        Videojuego(
            id=2,
            titulo="Mario Kart 8",
            plataforma="Nintendo Switch",
            precio=899.99,
            stock=5,
        ),
        Videojuego(
            id=3,
            titulo="Halo Infinite",
            plataforma="Xbox",
            precio=799.99,
            stock=3,
        ),
    ]


def test_registrar_videojuego():
    videojuegos = []

    videojuego = Videojuego(
        id=1,
        titulo="Minecraft",
        plataforma="PC",
        precio=599.99,
        stock=10,
    )

    registrar_videojuego(videojuegos, videojuego)

    assert len(videojuegos) == 1
    assert videojuegos[0].titulo == "Minecraft"


def test_listar_videojuegos(videojuegos):
    resultado = listar_videojuegos(videojuegos)

    assert len(resultado) == 3
    assert resultado[0].id == 1


def test_buscar_videojuego_existente(videojuegos):
    resultado = buscar_videojuego(videojuegos, 2)

    assert resultado is not None
    assert resultado.titulo == "Mario Kart 8"


def test_buscar_videojuego_no_existente(videojuegos):
    resultado = buscar_videojuego(videojuegos, 999)

    assert resultado is None


def test_no_permitir_id_duplicado(videojuegos):
    videojuego = Videojuego(
        id=1,
        titulo="Otro juego",
        plataforma="PC",
        precio=300,
        stock=2,
    )

    with pytest.raises(ValueError, match="ID del videojuego ya existe"):
        registrar_videojuego(videojuegos, videojuego)


def test_rechazar_precio_negativo():
    videojuegos = []

    videojuego = Videojuego(
        id=1,
        titulo="Juego inválido",
        plataforma="PC",
        precio=-100,
        stock=5,
    )

    with pytest.raises(ValueError, match="precio no puede ser negativo"):
        registrar_videojuego(videojuegos, videojuego)


def test_rechazar_stock_negativo():
    videojuegos = []

    videojuego = Videojuego(
        id=1,
        titulo="Juego inválido",
        plataforma="PC",
        precio=500,
        stock=-1,
    )

    with pytest.raises(ValueError, match="stock no puede ser negativo"):
        registrar_videojuego(videojuegos, videojuego)


def test_calcular_valor_inventario(videojuegos):
    resultado = calcular_valor_inventario(videojuegos)

    esperado = (599.99 * 10) + (899.99 * 5) + (799.99 * 3)

    assert resultado == pytest.approx(esperado)


def test_filtrar_por_plataforma(videojuegos):
    resultado = filtrar_por_plataforma(videojuegos, "PC")

    assert len(resultado) == 1
    assert resultado[0].titulo == "Minecraft"


def test_filtrar_por_plataforma_sin_resultados(videojuegos):
    resultado = filtrar_por_plataforma(videojuegos, "PlayStation")

    assert resultado == []


def test_obtener_videojuego_mas_caro(videojuegos):
    resultado = obtener_videojuego_mas_caro(videojuegos)

    assert resultado is not None
    assert resultado.titulo == "Mario Kart 8"
    assert resultado.precio == 899.99


def test_obtener_videojuego_mas_caro_sin_videojuegos():
    resultado = obtener_videojuego_mas_caro([])

    assert resultado is None


def test_actualizar_videojuego(videojuegos):
    actualizar_videojuego(
        videojuegos,
        1,
        "Minecraft Java Edition",
        "PC",
        699.99,
        15,
    )

    videojuego = buscar_videojuego(videojuegos, 1)

    assert videojuego.titulo == "Minecraft Java Edition"
    assert videojuego.precio == 699.99
    assert videojuego.stock == 15


def test_eliminar_videojuego(videojuegos):
    eliminar_videojuego(videojuegos, 2)

    assert len(videojuegos) == 2
    assert buscar_videojuego(videojuegos, 2) is None


def test_obtener_resumen(videojuegos):
    resultado = obtener_resumen(videojuegos)

    assert resultado["cantidad_videojuegos"] == 3
    assert resultado["unidades_stock"] == 18
    assert resultado["valor_inventario"] == pytest.approx(
        (599.99 * 10) + (899.99 * 5) + (799.99 * 3)
    )
