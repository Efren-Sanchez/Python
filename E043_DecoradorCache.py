"""
Decorador con cache para funciones costosas
Crea un decorador @cache que almacene en memoria los resultados de funciones "costosas" (por ejemplo, calculos Fibonacci).
El decorador debe:
- Usar un diccionario como cache con los argumentos como clave.
- Mostrar cuantas veces se ha usado el cache vs. recalculado.
- Limpiar el cache cuando supere 100 entradas.
"""

# Programa 43: Decorador con cache

def cache(maximo_tamano=100):
    """
    Decorador que implementa cache LRU (Least Recently Used).
    """
    def decorador(funcion):
        cache_dict = {}
        orden_usado = []
        hits = 0
        misses = 0
        
        def wrapper(*args, **kwargs):
            nonlocal hits, misses
            clave = (args, frozenset(kwargs.items()))
            
            if clave in cache_dict:
                # Cache HIT - mover al final (mas reciente)
                orden_usado.remove(clave)
                orden_usado.append(clave)
                hits += 1
                print(f"Cache HIT para {funcion.__name__}")
                return cache_dict[clave]
            
            # Cache MISS - calcular resultado
            resultado = funcion(*args, **kwargs)
            cache_dict[clave] = resultado
            orden_usado.append(clave)
            misses += 1
            print(f"Cache MISS para {funcion.__name__}")
            
            # Limpiar cache si es necesario (LRU)
            if len(cache_dict) > maximo_tamano:
                clave_vieja = orden_usado.pop(0)
                del cache_dict[clave_vieja]
            
            return resultado
        
        def cache_info():
            """Devuelve informacion sobre el estado del cache."""
            return {
                "tamano": len(cache_dict),
                "maximo": maximo_tamano,
                "hits": hits,
                "misses": misses
            }
        
        wrapper.cache_info = cache_info
        return wrapper
    return decorador


@cache(maximo_tamano=10)
def fibonacci(n):
    """
    Funcion Fibonacci "costosa" para demostrar el cache.
    """
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


def main():
    """
    Funcion principal que prueba el decorador.
    """
    print("Calculando Fibonacci con cache:")
    for i in range(15):
        print(f"Fibonacci({i}) = {fibonacci(i)}")
    
    print("\nInfo del cache:")
    info = fibonacci.cache_info()
    print(info)


if __name__ == "__main__":
    main()
