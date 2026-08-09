from .models import Videojuego
from .services import registrar_videojuego


def main():
    videojuegos = []

    videojuego = Videojuego(
        id=1,
        titulo="Minecraft",
        plataforma="PC",
        precio=599.99,
        stock=10,
    )

    registrar_videojuego(videojuegos, videojuego)

    print("Videojuego registrado correctamente.")
    print(videojuegos)


if __name__ == "__main__":
    main()