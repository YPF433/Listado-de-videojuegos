Listado de Videojuegos 

Este proyecto es una aplicación web que permite de videojuegos en distintas tiendas online. Fue creado utilizando FastAPI como backend, herramientas de web scraping para obtener la información, y un frontend HTML y CSS simple para visualizar los resultados de forma clara y directa.

----------------------------------------
¿Qué hace esta app?

- Permite buscar un videojuego por nombre
- Hace scraping en varias tiendas (simulado inicialmente)
- Muestra los precios disponibles por tienda
- Resalta el precio más bajo
- Interfaz básica y fácil de usar

----------------------------------------
Tecnologías utilizadas

- FastAPI
- Requests
- BeautifulSoup (bs4)
- HTML / CSS
- Python 3.10+

----------------------------------------
Cómo usar esta app en tu PC


1. Crear entorno virtual

  python -m venv venv


2. Activar entorno virtual

   En Windows:
   .\venv\Scripts\activate
   -(Si el terminal te bloquea la activación del entorno virtual utilizar el siguiente comando:(Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass)

   En Linux/macOS:
   source venv/bin/activate

3. Instalar dependencias

   pip install -r requirements.txt

4. Ejecutar FastAPI

   uvicorn main:app --reload

   Esto levantará el servidor en http://127.0.0.1:8000

5. Ver resultados

   Abrí el archivo frontend/index.html directamente con tu navegador.

----------------------------------------
Estructura del proyecto

videojuegos-precios/
 main.py           ← Archivo principal con FastAPI y endpoints
 scraper.py        ← Funciones de scraping por tienda
 models.py         ← Estructuras y clases de datos (Pydantic)
 requirements.txt  ← Lista de dependencias
 frontend/
    index.html    ← Página web básica para mostrar resultados

----------------------------------------
Explicación del código

main.py

Este archivo inicia FastAPI y define los endpoints:

- @app.get("/")  
  Devuelve un mensaje de bienvenida para confirmar que la API está activa.

- @app.get("/buscar")  
  Recibe un parámetro query (nombre del juego).  
  Llama a buscar_precios() desde scraper.py y devuelve un listado con resultados en formato JSON.


scraper.py

Contiene la lógica de búsqueda de precios (simulada por ahora).

- buscar_precios(juego: str) -> List[PrecioJuego]  
  Retorna una lista de objetos con tienda, precio y URL.


models.py

Define las estructuras de datos con Pydantic:

- PrecioJuego(BaseModel)  
  Tiene los siguientes campos:
  - tienda: str
  - precio: float
  - url: str


frontend/index.html

Archivo HTML simple que muestra una interfaz con un campo de búsqueda y espacio para resultados. No se utiliza JavaScript. El usuario puede escribir el nombre del juego y hacer clic en "Buscar" para mostrar los resultados mediante el backend.

----------------------------------------
Recursos y fuentes consultadas

Para construir esta app me basé en documentación oficial y algunos ejemplos sencillos de código abierto que encontré en Internet.

- Documentación de FastAPI: https://fastapi.tiangolo.com/
- BeautifulSoup: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
- Requests para trabajar con HTTP: https://docs.python-requests.org/en/latest/user/quickstart/
- Referencias de HTML y CSS: https://developer.mozilla.org/es/

----------------------------------------
Ideas futuras

- Implementar scraping real de sitios como Steam, Epic, etc.
- Conectar una base de datos para almacenar los resultados
- Agregar filtros por consola, género o idioma
- Crear cuentas de usuario para guardar listas de seguimiento


