# Mini-GoogleBot - Crawler inteligente estilo Google

## Enunciado

### Objetivo

Desarrollar un web crawler completo que simule el funcionamiento básico de Googlebot, indexando páginas web y creando un motor de búsqueda interno.

### Requisitos funcionales

- Indexacion inicial: Partir de una semilla (ej: wikipedia.org) y seguir TODOS los enlaces internos del mismo dominio
- Indexacion distribuida: Guardar en base de datos MySQL cada pagina con:

| Campo            | Descripcion                                      |
|------------------|--------------------------------------------------|
| url              | URL canonica                                    |
| titulo           | <title> de la pagina                            |
| contenido        | Texto limpio (sin HTML, sin scripts)            |
| palabras_clave   | TOP 50 palabras mas frecuentes                  |
| enlaces          | JSON con lista de URLs salientes                |
| timestamp        | Fecha indexacion                                |
| profundidad      | Nivel de recursion desde semilla               |

- Motor de busqueda: Consulta por palabras que devuelva TOP 10 resultados ordenados por relevancia (frecuencia de palabras + posicion en titulo)

### Requisitos tecnicos

- Librerias: requests, beautifulsoup4, mysql-connector-python, whoosh (indexacion), celery (tareas asincronas)
- Base datos: Tabla principal (paginas)
- Limite: maximo 1000 paginas, profundidad <= 4
- Respeto robots.txt + User-Agent rotativo
- Multihilo: 5 workers simultaneos
- Guardado: JSON backup + MySQL persistente

### Funcionalidades avanzadas (10 puntos extra cada una)

- Deteccion actualizaciones: Re-crawling paginas modificadas
- Scoring PageRank basico: Ponderar importancia por enlaces entrantes
- API REST: /buscar?query=python devuelve JSON
- Dashboard Flask: Visualizar estadisticas indexacion
- Cola de prioridades: Priorizar paginas con mas enlaces entrantes

### Ejemplo de uso esperado

```bash
$ python googlebot.py --semilla https://es.wikipedia.org --limite 500
Indexando: https://es.wikipedia.org/wiki/Python (profundidad 1)
Descubiertas 23 paginas nuevas
[ 2h 15m ] 487/500 paginas indexadas
$ python buscador.py "programacion web"
1. Programacion web - Wikipedia (relevancia: 89%)
2. Desarrollo web - Wikipedia (relevancia: 76%)
...
```

### Entregable: 

Código completo + demo con 100 páginas indexadas + informe PDF explicando arquitectura y decisiones técnicas.

### SQL inicial proporcionado:

´´´
sql
CREATE DATABASE googlebot;
CREATE TABLE paginas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    url VARCHAR(500) UNIQUE,
    titulo VARCHAR(200),
    contenido_texto LONGTEXT,
    palabras_clave JSON,
    enlaces JSON,
    timestamp DATETIME,
    profundidad INT,
    INDEX idx_palabras (palabras_clave(50))
);
´´´

### Evaluación

Funcionamiento + código limpio + documentación + base datos funcional + demo en vivo (no copiar Google directamente).

## Uso completo
    bash
    # 1. Crear BD (ejecutar SQL)
    # 2. Indexar
    python googlebot_indexador.py --semilla https://es.wikipedia.org/wiki/Programaci%C3%B3n --limite 200

    # 3. Buscar
    python buscador.py "desarrollo web"

## Características implementadas:
    - Multihilo (5 workers)
    - Robots.txt + User-Agent rotativo
    - Limpieza texto + palabras clave
    - Base MySQL FULLTEXT
    - Profundidad limitada
    - Logging profesional
    - Argumentos CLI



