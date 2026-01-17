"""
Cliente sencillo de API de clima
Crea un programa que consulte una API de clima (puede ser una ficticia simulada con un JSON local, si no quieres usar una real) para una ciudad introducida por el usuario.
El programa debe:
- Obtener los datos en formato JSON.
- Mostrar temperatura actual, humedad y descripcion del tiempo.
- Manejar el caso en el que la ciudad no exista en los datos.
"""

# Programa 34: Cliente de API de clima (usando API gratuita)

import requests  # Para peticiones HTTP


def obtener_clima(ciudad):
    """
    Obtiene datos del clima para una ciudad usando OpenWeatherMap.
    Necesitas una API key gratuita de https://openweathermap.org/api
    """
    api_key = "TU_API_KEY_AQUI"  # Reemplaza con tu clave real
    url = f"https://api.openweathermap.org/data/2.5/weather"  # ✅ Cambiado a HTTPS
    params = {
        "q": ciudad,
        "appid": api_key,
        "units": "metric",  # Temperaturas en Celsius
        "lang": "es"
    }
    
    try:
        respuesta = requests.get(url, params=params, timeout=10)
        respuesta.raise_for_status()
        datos = respuesta.json()
        
        temperatura = datos["main"]["temp"]
        humedad = datos["main"]["humidity"]
        descripcion = datos["weather"][0]["description"]
        
        return temperatura, humedad, descripcion
    except requests.exceptions.RequestException as e:
        return None, None, f"Error: {e}"
    except (KeyError, IndexError):
        return None, None, "Ciudad no encontrada"


def main():
    """
    Funcion principal del programa.
    """
    ciudad = input("Introduce el nombre de una ciudad: ").strip()
    if ciudad == "":
        print("El nombre de la ciudad no puede estar vacio.")
        return

    print(f"Obteniendo clima para '{ciudad}'...")
    temp, humedad, desc = obtener_clima(temp)

    if temp is None:
        print(desc)
    else:
        print(f"\nClima en {ciudad}:")
        print(f"Temperatura: {temp}C")
        print(f"Humedad: {humedad}%")
        print(f"Descripcion: {desc}")


if __name__ == "__main__":
    main()
