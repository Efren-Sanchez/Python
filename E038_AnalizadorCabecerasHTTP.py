"""
Analizador de cabeceras HTTP
Escribe un programa que pida una URL al usuario y realice una petición HEAD con requests.
Debe:
- Mostrar algunas cabeceras de respuesta importantes: Content-Type, Content-Length, Server, etc.
- Avisar si alguna de esas cabeceras no está presente.
- Guardar todas las cabeceras completas en un fichero de texto.
"""

# Programa 38: Analizador de cabeceras HTTP

import requests  # Para peticiones HTTP


def analizar_cabeceras(url):
    """
    Realiza petición HEAD y analiza las cabeceras de respuesta.
    """
    try:
        respuesta = requests.head(url, timeout=10, allow_redirects=True)
        print(f"\nCódigo de estado: {respuesta.status_code}")
        
        cabeceras_importantes = {
            "Content-Type": "Tipo de contenido",
            "Content-Length": "Tamaño del contenido",
            "Server": "Servidor web"
        }
        
        print("\nCabeceras importantes:")
        for cabecera, descripcion in cabeceras_importantes.items():
            valor = respuesta.headers.get(cabecera)
            if valor:
                print(f"{descripcion}: {valor}")
            else:
                print(f"{descripcion}: NO disponible")
        
        # Guardar todas las cabeceras
        nombre_fichero = "cabeceras.txt"
        try:
            with open(nombre_fichero, "w", encoding="utf-8") as f:
                f.write(f"URL: {url}\n")
                f.write(f"Status: {respuesta.status_code}\n\n")
                for nombre, valor in respuesta.headers.items():
                    f.write(f"{nombre}: {valor}\n")
            print(f"\nTodas las cabeceras guardadas en '{nombre_fichero}'.")
        except OSError as e:
            print(f"Error al guardar cabeceras: {e}")
            
    except requests.exceptions.RequestException as e:
        print(f"Error en la petición: {e}")


def main():
    """
    Función principal del programa.
    """
    url = input("Introduce la URL a analizar: ").strip()
    if url.startswith("http"):
        analizar_cabeceras(url)
    else:
        print("La URL debe comenzar con http:// o https://")


if __name__ == "__main__":
    main()
