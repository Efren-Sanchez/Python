"""
Web minima con Flask: contador de visitas
Implementa una pequena aplicacion web con Flask que tenga una unica ruta /.
En esa ruta se debe:
- Mostrar un mensaje de bienvenida.
- Llevar un contador de visitas en memoria (que se incremente cada vez que se carga la pagina).
- Mostrar el numero de visitas junto con el mensaje.
"""

# Programa 35: Aplicacion web Flask con contador de visitas
# Para ejecutar: pip install flask
# Luego: python E035_WebFlaskContador.py
# Abrir http://127.0.0.1:5000 en el navegador

from flask import Flask  # Framework web ligero

app = Flask(__name__)

# Variable global para el contador (en memoria)
contador_visitas = 0


@app.route("/")
def pagina_principal():
    """
    Ruta principal que muestra mensaje y contador de visitas.
    """
    global contador_visitas
    contador_visitas += 1
    return f"""
    <html>
        <head><title>Contador de Visitas</title></head>
        <body style="font-family: Arial; text-align: center; padding: 50px;">
            <h1>¡Bienvenido a mi pagina web!</h1>
            <p>Esta es una aplicacion web simple con <strong>Flask</strong>.</p>
            <h2>Contador de visitas: <span style="color: blue;">{contador_visitas}</span></h2>
            <p><a href="/">Actualizar pagina</a></p>
        </body>
    </html>
    """


def main():
    """
    Funcion principal que ejecuta el servidor Flask.
    """
    print("Servidor Flask iniciado en http://127.0.0.1:5000")
    print("Pulsa Ctrl+C para detener el servidor.")
    app.run(debug=True, host="127.0.0.1", port=5000)


if __name__ == "__main__":
    main()
