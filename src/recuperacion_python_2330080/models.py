from dataclasses import dataclass


@dataclass
class Videojuego:
    id: int
    titulo: str
    plataforma: str
    precio: float
    stock: int
