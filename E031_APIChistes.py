"""
Consumir una API pública de chistes
Crea un programa que haga una petición HTTP a una API pública de chistes (por ejemplo, chistes en formato JSON) y muestre en pantalla el texto del chiste.
Debe:
- Usar la librería requests.
- Comprobar el código de estado HTTP.
- Manejar errores de conexión mostrando un mensaje adecuado.
"""

# Programa 31: Consumidor de API de chistes

import requests  # Librería para peticiones HTTP


def obtener_chiste():
    """
    Realiza una petición a una API pública de chistes y devuelve el texto.
    """
    url = "https://api.chucknorris.io/jokes/random"  # API pública gratuita
    try:
        respuesta = requests.get(url, timeout=5)
        respuesta.raise_for_status()  # Lanza excepción si no es 200 OK
        datos = respuesta.json()
        return datos["value"]  # El chiste está en el campo 'value'
    except requests.exceptions.RequestException as e:
        return f"Error al obtener el chiste: {e}"


def main():
    """
    Función principal del programa.
    """
    print("Obteniendo un chiste de Chuck Norris...")
    chiste = obtener_chiste()
    print("\n¡Aquí tienes tu chiste!")
    print("-" * 50)
    print(chiste)
    print("-" * 50)


if __name__ == "__main__":
    main()
