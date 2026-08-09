# Tienda de Videojuegos

## Datos del estudiante

* **Nombre:** Yoselin Elena Honorato Perez
* **Matrícula:** 2330080
* **Variante:** 11

## Descripción

Este proyecto es un mini sistema de gestión para una tienda de videojuegos desarrollado en Python.

Permite registrar, consultar, actualizar y eliminar videojuegos, además de realizar cálculos y filtros relacionados con el inventario.

La información se mantiene en memoria utilizando estructuras de datos de Python durante la ejecución del programa.

## Funcionalidades

El sistema permite:

* Registrar videojuegos.
* Mostrar todos los videojuegos registrados.
* Buscar un videojuego mediante su ID.
* Actualizar la información de un videojuego.
* Eliminar un videojuego.
* Evitar IDs duplicados.
* Validar los datos introducidos.
* Calcular el valor total del inventario.
* Filtrar videojuegos por plataforma.
* Encontrar el videojuego más caro.
* Mostrar un resumen general del inventario.
* Manejar entradas incorrectas razonables.

### Funciones particulares de la variante 11

La variante corresponde a **Tienda de videojuegos**.

La entidad principal es **Videojuego**, con los siguientes datos:

* ID.
* Título.
* Plataforma.
* Precio.
* Stock.

Las funciones particulares implementadas son:

1. Calcular el valor total del inventario.
2. Filtrar videojuegos por plataforma.
3. Encontrar el videojuego más caro.

## Estructura del proyecto

```text
recuperacion-python-2330080/
│
├── .gitignore
├── .python-version
├── README.md
├── pyproject.toml
├── uv.lock
│
├── src/
│   └── recuperacion_python_2330080/
│       ├── __init__.py
│       ├── main.py
│       ├── models.py
│       └── services.py
│
└── tests/
    ├── __init__.py
    └── test_services.py
```

### Archivos principales

* `main.py`: contiene el menú y la interacción con el usuario.
* `models.py`: contiene el modelo `Videojuego`.
* `services.py`: contiene las operaciones, validaciones, búsquedas, cálculos y filtros.
* `tests/test_services.py`: contiene las pruebas automatizadas.
* `pyproject.toml`: contiene la configuración y dependencias del proyecto.
* `uv.lock`: registra las versiones de las dependencias.
* `.python-version`: indica la versión de Python utilizada.
* `.gitignore`: evita incluir archivos temporales y el ambiente virtual en Git.

## Requisitos

Para ejecutar el proyecto se necesita:

* Python 3.14 o superior.
* Git.
* `uv`.

El proyecto utiliza `pytest` y `ruff` como dependencias de desarrollo.

## Instalación

Clonar el repositorio:

```bash
git clone https://github.com/Elena-Honorato/recuperacion-python-2330080.git
```

Entrar al directorio:

```bash
cd recuperacion-python-2330080
```

## Sincronización

El proyecto utiliza `uv` para administrar el ambiente y las dependencias.

Para sincronizar el proyecto:

```bash
uv sync
```

Este comando permite crear o actualizar el ambiente virtual y descargar las dependencias necesarias.

El directorio `.venv/` es generado localmente y no forma parte del repositorio.

## Ejecución

La aplicación puede ejecutarse mediante:

```bash
uv run recuperacion-python-2330080
```

Al iniciar se muestra un menú con las diferentes operaciones disponibles.

## Pruebas

El proyecto utiliza `pytest` para realizar pruebas automatizadas.

Para ejecutar las pruebas:

```bash
uv run pytest
```

Actualmente el proyecto cuenta con **15 pruebas automatizadas**.

Las pruebas verifican diferentes comportamientos del sistema, incluyendo:

* Registro de videojuegos.
* Listado de videojuegos.
* Búsqueda de videojuegos existentes.
* Búsqueda de videojuegos inexistentes.
* Prevención de IDs duplicados.
* Validación de precios negativos.
* Validación de stock negativo.
* Cálculo del valor del inventario.
* Filtrado por plataforma.
* Filtrado sin resultados.
* Obtención del videojuego más caro.
* Manejo de una colección vacía.
* Actualización de videojuegos.
* Eliminación de videojuegos.
* Generación del resumen del inventario.

## Ruff

El proyecto utiliza Ruff para revisar y formatear el código.

Para revisar posibles problemas:

```bash
uv run ruff check .
```

Para aplicar el formato:

```bash
uv run ruff format .
```

Para comprobar que todos los archivos están correctamente formateados:

```bash
uv run ruff format --check .
```

Las comprobaciones actuales de Ruff se encuentran sin errores.

## Pruebas implementadas

Las pruebas fueron diseñadas para comprobar directamente las funciones principales de `services.py`.

Se incluyen pruebas de funcionamiento normal, casos límite, datos inválidos y búsquedas sin resultados.

También se comprueban los cálculos y operaciones particulares de la variante, como el valor del inventario, el filtrado por plataforma y la búsqueda del videojuego más caro.

## Decisiones de diseño

El programa fue dividido en diferentes módulos para separar responsabilidades.

El archivo `models.py` representa la entidad principal del sistema mediante la clase `Videojuego`.

El archivo `services.py` contiene la lógica del sistema, incluyendo registros, búsquedas, actualizaciones, eliminaciones, validaciones, filtros y cálculos.

El archivo `main.py` se encarga principalmente de la interacción con el usuario y del menú principal.

La información se almacena en una lista de objetos `Videojuego` durante la ejecución, ya que el proyecto no requiere una base de datos.

También se utilizaron funciones independientes para facilitar las pruebas automatizadas y mantener organizada la lógica del programa.

## Problemas encontrados

Durante el desarrollo se encontraron problemas relacionados con código no utilizado y formato del código.

Ruff detectó imports que no estaban siendo utilizados y varios archivos que necesitaban ser formateados. Estos problemas fueron corregidos utilizando las herramientas de Ruff.

También se implementaron validaciones para evitar IDs duplicados y valores negativos en precio o stock.

Después de realizar las correcciones se verificó nuevamente el proyecto mediante:

```bash
uv run pytest
```

```bash
uv run ruff check .
```

```bash
uv run ruff format --check .
```

Las pruebas y comprobaciones se ejecutan correctamente.

## Herramientas utilizadas

* Python
* Git
* GitHub
* uv
* pytest
* Ruff
* Markdown

## Estado del proyecto

El proyecto cumple con los requisitos principales de la variante 11 y cuenta con:

* Estructura basada en `src/`.
* Ambiente administrado mediante `uv`.
* Pruebas automatizadas con `pytest`.
* Revisión y formato mediante `ruff`.
* Historial de commits significativo.
* Documentación mediante Markdown.
