# Programas Python

Ejemplos de programas Python con distintos usos.

## Enunciados

1. Números únicos en una lista
    Pide al usuario una serie de números separados por espacios y guarda solo los valores únicos (sin repeticiones). Muestra la lista ordenada de menor a mayor.

2. Análisis de texto
    Solicita al usuario el nombre de un fichero de texto y muestra:
    - Número total de líneas.
    - Número total de palabras.
    - Las 5 palabras más frecuentes.
    Usa el módulo collections (por ejemplo, Counter).

3. Promedios con tuplas
    Crea una función que reciba una lista de tuplas, donde cada tupla contiene (nombre, nota1, nota2, nota3), y devuelva un nuevo diccionario con el promedio de cada alumno. Muestra los nombres ordenados por nota media descendente.

4. Mezcla de listas
    Genera dos listas de números aleatorios (usa random.randint) y:
    - Combínalas alternando valores.
    - Elimina los duplicados.
    - Guarda el resultado en un fichero llamado resultado.txt.

5. Diccionario de frecuencias de caracteres
    Lee un fichero de texto y muestra la frecuencia de cada letra (ignorando mayúsculas, tildes y signos de puntuación). Usa un diccionario y ordena por frecuencia descendente.

6. Agenda simple
    Crea un pequeño programa de agenda de contactos que guarde en un fichero JSON (json):
    - Añadir contacto (nombre, teléfono, email).
    - Buscar contacto por nombre.
    - Listar todos los contactos.
    Practicarán lectura/escritura de ficheros y manipulación de diccionarios/listas.

7. Estadísticas de una lista numérica
    Pide una lista de números y calcula:
    - Media, mediana y desviación estándar.
    Usa la librería statistics y muestra los resultados con 2 decimales.

8. Procesamiento de registros
    Dado un fichero CSV con columnas nombre,edad,ciudad, crea un programa que:
    - Lea el fichero y almacene los datos en una lista de tuplas.
    - Pida una ciudad y muestre los nombres de las personas que viven en ella.
    Usa el módulo csv.

9. Conversor de temperaturas
    Implementa varias funciones para convertir entre Celsius, Fahrenheit y Kelvin.
    Pide los datos por teclado y guarda un historial de conversiones en un fichero de texto.

10. Estadísticas meteorológicas (librerías)
    Usando la librería datetime y random, genera una lista de 30 registros simulando temperaturas diarias de un mes.
    Cada elemento será una tupla (fecha, temperatura). Calcula la temperatura media, máxima y mínima, y guarda el resumen en un fichero CSV.

11. Gestión de una lista de tareas
    Crea un programa que mantenga una lista de tareas pendientes en memoria.
    Debe permitir: añadir tarea, marcar tarea como realizada, eliminar tarea y mostrar todas las tareas (pendientes y realizadas). Usa una lista de tuplas (descripcion, realizada) y un menú simple.

12. Fusionar y filtrar listas de productos
    Pide al usuario dos listas de productos, cada una con nombres separados por comas.
    Crea una lista única sin duplicados y luego pide una cadena de búsqueda para mostrar solo los productos que contengan dicho texto. Usa listas y comprensión de listas.

13. Notas por módulo desde fichero
    Diseña un programa que lea desde un fichero de texto líneas con el formato alumno;modulo;nota.
    Carga los datos en una lista de tuplas y muestra, para un módulo elegido por el usuario, la nota media, la nota máxima y la nota mínima de ese módulo.

14. Estadísticas de palabras con stopwords
    Pide al usuario el nombre de un fichero de texto.
    Cuenta las palabras más usadas, pero ignorando un conjunto de palabras vacías (por ejemplo: "y", "de", "la", "el", "en", "a"). Muestra las 10 palabras más frecuentes y su frecuencia. Usa un conjunto (set) para las stopwords.

15. Registro de sesiones de usuario
    Crea un programa que simule el inicio y cierre de sesión de usuarios.
    Cada vez que un usuario inicie o cierre sesión, registra el evento en un fichero de texto con el formato usuario;accion;fecha_hora. Usa la librería datetime para obtener la marca temporal.

16. Conversor de monedas con fichero de tasas
    En un fichero de texto se almacenan tasas de conversión con el formato codigo_moneda;valor_en_euros (por ejemplo: USD;0.93).
    El programa debe: leer el fichero, pedir una cantidad en euros y una moneda destino, y mostrar la conversión. Si la moneda no existe en el fichero, avisar al usuario.

17. Generador y analizador de números aleatorios
    Haz un programa que genere N números aleatorios entre un mínimo y un máximo, usando la librería random, y los guarde en una lista.
    Después:
    - Muestra la lista ordenada.
    - Muestra cuántos son pares e impares.
    - Guarda la lista en un fichero de texto, un número por línea.

18. Buscador de líneas en un log
    Dado un fichero de log (por ejemplo, aplicacion.log), pide al usuario una palabra clave.
    El programa debe mostrar todas las líneas que contengan esa palabra, indicando también el número de línea. Usa lectura línea a línea y enumeración.

19. Gestión de alumnos con tuplas inmutables
    Crea una lista de tuplas inmutables que representen alumnos: (dni, nombre, apellidos, nota_media).
    Implementa un menú que permita:
    - Mostrar todos los alumnos ordenados por nota media.
    - Buscar un alumno por DNI.
    - Mostrar la nota media del grupo.

20. Pequeño “ranking” de puntuaciones
    Pide al usuario que introduzca varias puntuaciones de jugadores en el formato nombre;puntuacion, hasta que introduzca una cadena vacía.
    Guarda los datos en una lista de tuplas (nombre, puntuacion) y al final muestra un ranking con los 5 jugadores con mayor puntuación. Si hay menos de 5, muestra todos.

21. Clase Rectangulo con métodos geométricos
    Define una clase Rectangulo con atributos ancho y alto.
    La clase debe incluir:
    - Método para calcular área y perímetro.
    - Método que indique si es un cuadrado.
    - Método que permita escalar el rectángulo por un factor (multiplicar ancho y alto).
    Crea varios objetos y muestra sus datos por pantalla.

22. Clase CuentaBancaria con control de saldo
    Implementa una clase CuentaBancaria con atributos titular, iban y saldo.
    Debe tener métodos para:
    - Ingresar dinero.
    - Retirar dinero (no permitir saldo negativo).
    - Mostrar información de la cuenta.
    Crea un pequeño menú para operar con un objeto CuentaBancaria desde teclado.

23. Clase Fraccion con operaciones básicas
    Crea una clase Fraccion que represente una fracción con numerador y denominador.
    Debe permitir:
    - Sumar y restar fracciones (métodos que devuelvan nuevas fracciones).
    - Simplificar la fracción a su forma irreducible.
    - Mostrar la fracción en formato a/b.
    Usa, si quieres, math.gcd para simplificar.

24. Estadísticas con numpy (si está disponible)
    Diseña un programa que, usando la librería numpy si está instalada, cree un array con 100 números aleatorios en el rango [0, 100).
    Debe calcular:
    - Media, desviación estándar y valor máximo.
    - Número de valores mayores que la media.
    Si numpy no está disponible, muestra un mensaje indicando que no se puede ejecutar el ejercicio.

25. Lectura de datos CSV en clase Alumno
    Crea una clase Alumno con atributos nombre, edad y ciudad.
    Escribe un programa que lea un fichero CSV con esos campos y cree una lista de objetos Alumno.
    Después, implementa funciones para:
    - Mostrar todos los alumnos.
    - Mostrar solo los que viven en una ciudad dada.
    - Calcular la edad media del grupo.

26. Uso de pathlib para explorar un directorio
    Escribe un programa que use la librería pathlib para:
    - Pedir al usuario una ruta de directorio.
    - Listar todos los ficheros normales de ese directorio.
    - Mostrar, para cada fichero, su tamaño en bytes y su extensión.
    - Contar cuántos ficheros hay de cada extensión (por ejemplo: .txt, .py, etc.).

27. Clase Cronometro usando time
    Implementa una clase Cronometro que permita medir el tiempo transcurrido entre un inicio y un fin.
    Debe tener métodos:
    - iniciar(): guarda el tiempo de inicio.
    - detener(): guarda el tiempo de fin.
    - tiempo_transcurrido(): devuelve el tiempo en segundos entre inicio y fin.
    Crea un pequeño programa que lo use para medir cuánto tarda el usuario en escribir una frase.

28. Clase GestorNotas con persistencia en JSON
    Crea una clase GestorNotas que gestione un diccionario de alumnos y sus notas.
    La clase debe:
    - Cargar las notas desde un fichero JSON al iniciar (si existe).
    - Permitir añadir o modificar la nota de un alumno.
    - Permitir eliminar un alumno.
    - Guardar los cambios en el fichero JSON al finalizar el programa.
    Implementa un menú de texto para manejar el gestor.

29. Uso de re para validar datos con clases
    Define una clase Validador que agrupe métodos estáticos para validar:
    - Un correo electrónico.
    - Un número de teléfono español sencillo (por ejemplo, 9 dígitos).
    - Un DNI con formato básico (8 dígitos y una letra).
    Usa la librería re (expresiones regulares).
    Crea un programa que pida esos datos al usuario y muestre si cada uno es válido o no.

30. Conversor de formatos de fecha con datetime
    Escribe un programa que use la librería datetime para:
    - Pedir al usuario una fecha en formato dd/mm/aaaa.
    - Convertirla a un objeto date.
    - Mostrar la misma fecha en diferentes formatos: aaaa-mm-dd, nombre del día de la semana en castellano, y el número de día del año (1–365/366).
    Opcional: encapsular la lógica en una clase FechaUtil.

31. Consumir una API pública de chistes
    Crea un programa que haga una petición HTTP a una API pública de chistes (por ejemplo, chistes en formato JSON) y muestre en pantalla el texto del chiste.
    Debe:
    - Usar la librería requests.
    - Comprobar el código de estado HTTP.
    - Manejar errores de conexión mostrando un mensaje adecuado.

32. Descargador simple de imágenes
    Escribe un programa que reciba por teclado una URL de imagen y un nombre de fichero local.
    El programa debe:
    - Descargar la imagen usando requests.
    - Guardarla en disco en un fichero con el nombre indicado.
    - Comprobar el tamaño de la respuesta y mostrarlo por pantalla.

33. Comprobador de estado de páginas web
    Diseña un programa que lea desde un fichero de texto una lista de URLs (una por línea).
    Para cada URL:
    - Realiza una petición GET con requests.
    - Muestra el código de estado (200, 404, etc.).
    - Guarda en un fichero de salida las URLs que no respondan o devuelvan un código de error (400 o superior).

34. Cliente sencillo de API de clima
    Crea un programa que consulte una API de clima (puede ser una ficticia simulada con un JSON local, si no quieres usar una real) para una ciudad introducida por el usuario.
    El programa debe:
    - Obtener los datos en formato JSON.
    - Mostrar temperatura actual, humedad y descripción del tiempo.
    - Manejar el caso en el que la ciudad no exista en los datos.

35. Web mínima con Flask: contador de visitas
    Implementa una pequeña aplicación web con Flask que tenga una única ruta /.
    En esa ruta se debe:
    - Mostrar un mensaje de bienvenida.
    - Llevar un contador de visitas en memoria (que se incremente cada vez que se carga la página).
    - Mostrar el número de visitas junto con el mensaje.

36. API REST muy simple con Flask
    Crea una API REST básica con Flask para gestionar una lista de tareas (similar a TODO list), pero ahora vía HTTP.
    Debe tener al menos:
    - Ruta GET /tareas que devuelva en JSON la lista de tareas.
    - Ruta POST /tareas que reciba una tarea en JSON y la añada.
    - Ruta DELETE /tareas/<id> que elimine una tarea por su identificador.

37. Conversor de divisas con API externa
    Haz un programa de consola que:
    - Pregunte una cantidad en euros y una moneda de destino (por ejemplo, USD, GBP, JPY).
    - Consulte una API de tipos de cambio (o use un JSON local que simule esa API) para obtener el tipo de cambio actual.
    - Muestre el resultado de la conversión junto con la fecha de la tasa de cambio.

38. Analizador de cabeceras HTTP
    Escribe un programa que pida una URL al usuario y realice una petición HEAD con requests.
    Debe:
    - Mostrar algunas cabeceras de respuesta importantes: Content-Type, Content-Length, Server, etc.
    - Avisar si alguna de esas cabeceras no está presente.
    - Guardar todas las cabeceras completas en un fichero de texto.

39. Monitor de latencia de servidores
    Diseña un programa que reciba una lista de URLs y mida el tiempo de respuesta de cada una.
    Debe:
    - Usar time para medir el tiempo antes y después de la petición HTTP.
    - Repetir varias veces la petición y calcular la media de tiempo de respuesta.
    - Mostrar un pequeño “ranking” de servidores ordenados de menor a mayor latencia media.

40. Lector de RSS con feedparser (u otra librería similar)
    Crea un programa que lea un feed RSS (por ejemplo, de noticias tecnológicas) usando una librería especializada como feedparser (si está instalada; si no, plantearlo como opcional).
    El programa debe:
    - Obtener la lista de entradas del feed.
    - Mostrar por pantalla los títulos y URLs de las 5 últimas noticias.
    - Guardar los títulos en un fichero de texto para leerlos más tarde sin conexión.

41. Sistema de logging configurable
    Crea un programa que use el módulo logging para registrar eventos en diferentes niveles (DEBUG, INFO, WARNING, ERROR).
    Debe permitir:
    - Configurar el nivel de logging desde un fichero de configuración (config.ini).
    - Registrar mensajes en fichero y consola simultáneamente.
    - Formatear las entradas con timestamp, nivel y nombre del módulo.

42. Generador de números primos infinitos
    Implementa un generador infinito que produzca números primos consecutivos usando yield.
    El programa debe:
    - Permitir al usuario pedir los primeros N primos.
    - Mostrar el tiempo que tarda en generar los primeros 1000 primos.
    - Guardar los primos generados en una lista limitada para no consumir memoria.

43. Decorador con caché para funciones costosas
    Crea un decorador @cache que almacene en memoria los resultados de funciones "costosas" (por ejemplo, cálculos Fibonacci).
    El decorador debe:
    - Usar un diccionario como caché con los argumentos como clave.
    - Mostrar cuántas veces se ha usado el caché vs. recalculado.
    - Limpiar el caché cuando supere 100 entradas.

44. Context Manager personalizado para archivos temporales
    Define un context manager ArchivoTemporal usando @contextmanager que:
    - Cree un fichero temporal al entrar en el bloque with.
    - Permita escribir/leer datos durante su uso.
    - Elimine automáticamente el fichero al salir del bloque, incluso si hay errores.

45. Procesador paralelo de números con multiprocessing
    Crea un programa que divida una lista de 1.000.000 números aleatorios entre 4 procesos paralelos.
    Cada proceso debe:
    - Calcular la suma parcial de su sublista.
    - Usar multiprocessing.Queue para enviar su resultado al proceso principal.
    - Mostrar el tiempo total y compararlo con la versión secuencial.

46. Framework de testing unitario casero
    Implementa un mini framework de tests con las siguientes características:
    - Función assert_equals(valor_real, valor_esperado) que lance AssertionError descriptivo.
    - Función assert_raises(Exception, funcion, *args) para comprobar excepciones.
    - Función run_tests(lista_tests) que ejecute tests y muestre % de éxito.

47. Gestor de configuración con configparser
    Crea un programa que lea configuración desde config.ini con secciones [DATABASE], [LOGGING], [API].
    Debe:
    - Validar que existan todas las secciones y claves obligatorias.
    - Permitir sobrescribir configuración desde variables de entorno.
    - Mostrar la configuración final cargada.

48. Pipeline de procesamiento de datos con generadores
    Crea un pipeline de datos usando generadores encadenados:
    text
    numeros → pares → cuadrados → filtrar > 1000 → suma
    Cada paso debe ser un generador independiente que reciba datos del anterior.

49. Singleton para conexión a base de datos
    Implementa el patrón Singleton para una clase ConexionBD que:
    - Garantice que solo exista una instancia en toda la aplicación.
    - Simule conexión/desconexión a base de datos.
    - Incluya método get_instancia() estático para obtener la única instancia.

50. Descriptor para validación de propiedades
    Define un descriptor EnteroPositivo que:
    - Solo permita asignar valores enteros positivos a una propiedad.
    - Lance ValueError si se asigna un valor inválido.
    - Se use en una clase Producto para validar stock y precio.

51. CRUD completo con sqlite3
    Crea un programa que gestione una base de datos SQLite tienda.db con tabla productos (id, nombre, precio, stock).
    Implementa un menú completo con:
    - CREATE: Insertar nuevo producto.
    - READ: Listar todos o buscar por nombre.
    - UPDATE: Modificar precio/stock.
    - DELETE: Eliminar producto.
    - Backup de la BD completa a backup.db.

52. Validador de formularios con expresiones regulares
    Implementa una clase ValidadorFormulario que valide todos los campos de un formulario web:
    text
    - Nombre completo (solo letras + espacios)
    - Email (formato estándar)
    - Teléfono español (9 dígitos)
    - DNI (8 dígitos + letra)
    - Código postal (5 dígitos)
    - Fecha dd/mm/aaaa válida
    Muestra errores específicos por campo.

53. Servidor TCP concurrente con threading
    Crea un servidor TCP en puerto 8888 que acepte múltiples clientes simultáneos usando threading.
    Cada cliente puede:
    - Enviar mensajes que se broadcast a todos los conectados.
    - Comando /salir para desconectarse.
    - Mostrar lista de clientes conectados con /lista.

54. Serialización de objetos complejos con pickle
    Crea clases Pedido y Cliente con relaciones anidadas.
    Implementa funciones para:
    - Serializar objetos complejos a pedidos.pkl.
    - Deserializar y validar integridad.
    - Migrar de pickle v1 a v2 cambiando estructura.
    - Comparar objetos original vs deserializado.

55. CLI profesional con argparse
    Desarrolla una aplicación CLI gestor-archivos con subcomandos:
    text
    gestor-archivos listar --directorio /ruta
    gestor-archivos limpiar --extension .tmp --dias 7
    gestor-archivos comparar dir1 dir2
    gestor-archivos --verbose --config config.json
    Con ayuda contextual, auto-completado y validación de argumentos.

56. Consumidor de colas con queue y threading
    Simula un sistema de colas de tareas con 3 tipos de trabajadores en hilos:
    text
    - Productor: genera tareas aleatorias
    - Procesador CPU: tareas de cálculo
    - Procesador I/O: simula lecturas de ficheros
    Muestra estadísticas de velocidad de procesamiento por tipo.

57. Parser de logs estructurados con json y re
    Analiza un fichero de logs con formato JSON por línea:
    text
    {"timestamp": "...", "nivel": "ERROR", "mensaje": "...", "usuario": "..."}
    El programa debe:
    - Filtrar por nivel de error y usuario.
    - Generar reporte estadístico por hora/día.
    - Exportar errores críticos a CSV.

58. Watcher de ficheros con watchdog
    Implementa un monitor de ficheros que:
    - Vigile un directorio por creaciones/modificaciones/eliminaciones.
    - Reaccione automáticamente (ej: comprimir nuevos .txt).
    - Pause/reanude vigilancia con señales del sistema.
    - Genere reporte de actividad.

59. Cliente OAuth2 con requests-oauthlib
    Crea un cliente que autentique contra una API OAuth2:
    text
    - Obtener código de autorización (URL)
    - Intercambiar código por token
    - Usar token Bearer para llamadas API
    - Refrescar token automáticamente
    Maneja todos los códigos de error HTTP OAuth2.

60. Generador de documentación automática con inspect
    Crea un sistema que genere documentación HTML automáticamente:
    text
    - Inspecciona módulos/clases/funciones con inspect
    - Extrae docstrings y firmas
    - Genera plantillas HTML con estilos
    - Incluye ejemplos de uso ejecutables
    Procesa un directorio completo de .py.

## MySQL

61. Conexión básica y consulta simple
    Diseña un programa que se conecte a un servidor MySQL, seleccione una base de datos existente y muestre por pantalla todos los registros de una tabla clientes (campos: id, nombre, email). 
    El programa debe manejar posibles errores de conexión y cerrar correctamente la conexión al finalizar.
​
62. Inserción de datos desde teclado
    Implementa un script que pida por teclado los datos de un nuevo producto (nombre, precio, stock) y los inserte en la tabla productos de una base de datos MySQL. 
    Tras la inserción, el programa debe mostrar el id autogenerado del producto y confirmar si la operación se ha realizado correctamente usando commit y control de excepciones.
​
63. Actualización y borrado con menú
    Crea una aplicación de consola que muestre un menú con las opciones:
    - Listar todos los artículos de la tabla articulos
    - Actualizar el precio de un artículo dado su id
    - Eliminar un artículo dado su id
    - Salir
    Cada opción debe ejecutar la consulta SQL correspondiente sobre MySQL y mostrar mensajes claros de éxito o error.
​
64. Búsqueda parametrizada y prevención de inyección
    Desarrolla un programa que solicite al usuario una cadena de búsqueda y muestre todos los empleados cuya columna apellido contenga ese texto (usando LIKE) en la tabla empleados. 
    Debes usar consultas parametrizadas para evitar inyección SQL y mostrar los resultados formateados (por ejemplo, id - nombre apellido - salario).
​
65. Mini CRUD completo sobre una tabla
    Programa un pequeño sistema CRUD para la tabla alumnos(id, nombre, edad, nota_media) en una base de datos MySQL. Debe permitir:
    - Crear un nuevo alumno
    - Listar todos los alumnos
    - Modificar la nota_media de un alumno por id
    - Eliminar un alumno por id
    Estructura el código en funciones (conectar, insertar, listar, actualizar, borrar) y asegúrate de cerrar cursores y conexiones correctamente.

## Web crawlers

66. Recopilador de noticias
    Desarrolla un programa que:
    - Reciba por parámetro una URL de inicio (ej: sección noticias de un periódico)
    - Extraiga todos los titulares (etiqueta <h2> o <h3> con clase específica)
    - Guarde en un archivo CSV: título, URL del artículo, fecha publicación
    - Limite la extracción a máximo 50 artículos
    - Respete el robots.txt del sitio (consulta antes de scrapear)
    - Muestre progreso en consola y tiempo total de ejecución

67. Rastreador de ofertas e-commerce
    Crea un crawler que:
    - Parta de la página principal de ofertas de una tienda online
    - Siga todos los enlaces de productos encontrados (clase product-link)
    - Para cada producto extraiga: nombre, precio actual, precio rebajado, % descuento
    - Detecte "novedades" (productos con menos de 7 días)
    - Guarde datos en JSON con timestamp y notifique ofertas >50% descuento
    - Implemente pausas aleatorias (2-5 seg) entre peticiones
    - Maneje paginación automática hasta 10 páginas
    - Extra: Compara precios con scraping anterior (fichero histórico)

68. Monitorizador de eventos culturales
    Implementa un sistema que:
    - Extraiga eventos culturales de varias webs (teatros, conciertos, etc.)
    - Para cada evento capture: título, fecha, lugar, precio entrada, URL
    - Use cola de prioridades para procesar primero eventos próximos
    - Filtre por ciudad (parámetro configurable: "Madrid", "Barcelona")
    - Exporte calendario en formato iCal (.ics) válido
    - Implemente reintentos (3 intentos) para páginas lentas
    - Cree log detallado con errores HTTP y páginas bloqueadas
    Código modular (funciones: conectar, extraer, validar, exportar), manejo de User-Agent rotativo, límite de 200 eventos totales.
    Incluir shebang, docstrings en español, try/except completos y validación de robots.txt. Probar con sitios públicos como ayuntamientos o medios de comunicación.

69. Desarrollar un web crawler completo que simule el funcionamiento básico de Googlebot, indexando páginas web y creando un motor de búsqueda interno.
    Requisitos funcionales:
    - Indexación inicial: Partir de una semilla (ej: wikipedia.org) y seguir TODOS los enlaces internos del mismo dominio
    - Indexación distribuida: Guardar en base de datos MySQL cada página con:
        Campo	            Descripción
        url	                URL canónica
        titulo	            <title> de la página
        contenido	        Texto limpio (sin HTML, sin scripts)
        palabras_clave	    TOP 50 palabras más frecuentes
        enlaces	            JSON con lista de URLs salientes
        timestamp	        Fecha indexación
        profundidad	        Nivel de recursión desde semilla
    - Motor de búsqueda: Consulta por palabras que devuelva TOP 10 resultados ordenados por relevancia (frecuencia de palabras + posición en título)

    Requisitos técnicos:
    - Librerías: requests, beautifulsoup4, mysql-connector-python, whoosh (indexación), celery (tareas asíncronas)
    - Base datos: 3 tablas (paginas, palabras, indices)
    - Límite: máximo 1000 páginas, profundidad ≤ 4
    - Respeto robots.txt + User-Agent rotativo
    - Multihilo: 5 workers simultáneos
    - Guardado: JSON backup + MySQL persistente
    Funcionalidades avanzadas (10 puntos extra cada una):
    - Detección actualizaciones: Re-crawling páginas modificadas
    - Scoring PageRank básico: Ponderar importancia por enlaces entrantes
    - API REST: /buscar?query=python devuelve JSON
    - Dashboard Flask: Visualizar estadísticas indexación
    - Cola de prioridades: Priorizar páginas con más enlaces entrantes

    Ejemplo de uso esperado:

    $ python googlebot.py --semilla https://es.wikipedia.org --limite 500
    Indexando: https://es.wikipedia.org/wiki/Python (profundidad 1)
    Descubiertas 23 páginas nuevas
    [ 2h 15m ] 487/500 páginas indexadas
    $ python buscador.py "programacion web"
    1. Programación web - Wikipedia (relevancia: 89%)
    2. Desarrollo web - Wikipedia (relevancia: 76%)
    ...

    Entregable: Código completo + demo con 100 páginas indexadas + informe PDF explicando arquitectura y decisiones técnicas.

    SQL inicial proporcionado:

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

    Evaluación: Funcionamiento + código limpio + documentación + base datos funcional + demo en vivo (no copiar Google directamente).

## Interfaces gráficas con Tkinter

### Ejercicios Básicos

1. Crea una ventana con Tkinter que muestre un botón; al pulsarlo, cambie el color de fondo de la ventana entre rojo, verde y azul.
​
2. Desarrolla un programa que solicite al usuario su nombre y edad mediante Entry y Entry, y muestre un mensaje con messagebox: "¡Hola [nombre]! Eres mayor de edad" si la edad >=18, o "¡Eres menor!" en caso contrario.
​
3. Diseña una interfaz que pida un número entero N en un Entry y calcule su factorial con un Button, mostrando el resultado en un Label.
​
### Ejercicios Intermedios

4. Implementa un editor de texto simple con un área Text grande, un menú con opciones "Nuevo", "Abrir" y "Guardar" para manejar ficheros .txt.
​
5. Crea una aplicación con dos LabelFrame: el primero con dos Label, dos Entry (para nombre y contraseña) y un Button de login; el segundo con tres botones (Aceptar, Cancelar, Salir).
​
6. Construye una calculadora gráfica básica con botones numéricos (0-9), operaciones (+, -, *, /) y un área de texto para mostrar resultados.
​
### Ejercicios Avanzados

7. Desarrolla un catálogo de películas persistente usando Tkinter para añadir/eliminar items, guardando datos en un fichero con pickle.
​
8. Crea un gestor de menú de restaurante con Listbox para categorías y platos, conectado a una base de datos SQLite para listar y añadir elementos.
​
9. Implementa un formulario de login con validación: Entry para usuario/contraseña, Button que verifique credenciales y cambie a una ventana principal si son correctas.

## Generación de gráficos

1. Curva de Koch
    Implementa un programa en Python que dibuje la curva de Koch de orden n (por ejemplo, n=4) usando el módulo turtle. Divide cada segmento en tres partes iguales, sustituye el segmento central por los dos lados de un triángulo equilátero (rotando 60°), y repite recursivamente. Muestra el copo de nieve completo uniendo cuatro curvas.

2. Triángulo de Sierpinski
    Crea una función recursiva que genere el triángulo de Sierpinski de nivel n (por ejemplo, n=6) con turtle o matplotlib. Parte de un triángulo equilátero inicial y en cada iteración, divide cada lado en dos y conecta los puntos medios, eliminando el triángulo central. Colorea las áreas para resaltar la estructura fractal.
​
3. Curva del Dragón
    Desarrolla un script que trace la curva del Dragón (o "Dragon Curve") de orden n usando recursión con turtle. Comienza con una línea recta, aplica giros alternos de 90° (derecha e izquierda) en cada iteración doblando la curva sobre sí misma, y visualiza el resultado para n=10. Experimenta con colores por nivel de recursión.
​
4. Helecho de Barnsley
    Escribe un programa que simule el helecho de Barnsley aplicando cuatro transformaciones afines probabilísticas (probabilidades: 0.85, 0.07, 0.07, 0.01) a un punto inicial (0,0) durante 50,000 iteraciones con matplotlib. Usa random para seleccionar cada regla y plotea los puntos resultantes en verde para simular hojas.
​
5. Curva de Hilbert
    Implementa la curva de Hilbert de orden n (por ejemplo, n=5) con una función recursiva en turtle. Esta curva rellena un cuadrado dividiendo recursivamente en cuatro subcuadrados, girando 90° y conectando con pasos hacia adelante. Asegúrate de que sea continua y sin autointersecciones, ideal para mostrar espacio-filling.

6. Árbol Fractal
    Crea un programa con turtle que dibuje un árbol fractal recursivo. Comienza con un tronco vertical y en cada rama aplica un ángulo aleatorio entre 25°-35° con longitud reducida al 70%. Añade hojas verdes en las ramas finales usando círculos pequeños.
​
7. Espiral Logarítmica
    Implementa con turtle una espiral logarítmica (espiral de oro) donde cada segmento crece un factor φ=(1+√5)/2 respecto al anterior. Dibuja 100 vueltas alternando colores azul/rojo y grosor creciente. Marca el centro con un círculo.

8. Conjunto de Mandelbrot
    Desarrolla con matplotlib el conjunto de Mandelbrot usando 500x500 píxeles. Colorea píxeles según iteraciones hasta |z|>2 para c en -2.5..1 (real) y -1.5..1.5 (imaginario). Usa mapa de colores 'hot' con zoom interactivo opcional.

9. Estrella de David
    Dibuja con turtle dos triángulos equiláteros superpuestos rotados 180° formando la estrella de David. Rellena uno en azul y otro en amarillo con contornos negros. Añade animación rotando lentamente toda la figura 360°.

10. Curva de Lissajous
    Genera con matplotlib figuras de Lissajous variando frecuencias f_x y f_y (ej: 3:4, 5:3). Usa ecuaciones x=sin(2πft+a), y=sin(2πft*b) para t∈. Prueba fases a=0°,90°,180° con colores distintos por fase.

11. Copo de Nieve Variante
    Modifica la curva de Koch con matplotlib para crear un copo de nieve con picos alternos hacia arriba/abajo. Usa 6 lados en lugar de 3 y ángulos variables (60°,120°). Experimenta con orden 5 y colores degradé por profundidad recursiva.
​
12. Espiral de Arquímedes
    Con turtle, dibuja una espiral de Arquímedes r=aθ donde θ va de 0 a 10π. Incrementa el radio linealmente con el ángulo. Usa circle con radio variable y colorea por sectores (rojo,verde,azul repitiendo cada 120°).
​
13. Triángulo de Koch con Colores
    Implementa con turtle la curva de Koch pero colorea cada nivel recursivo diferente (nivel 0: negro, 1: rojo, 2: azul, etc.). Dibuja el copo completo rotando 60° entre lados y usa pencolor en la función recursiva.
​
14. Flor de Petalos Móviles
    Crea con turtle una flor de 12 pétalos usando círculos superpuestos con radio decreciente. Haz animación donde los pétalos "respiran" expandiéndose/contrayéndose con circle y delays. Centro amarillo, pétalos rosas con contorno verde.
​
15. Fractal de Julia
    Con matplotlib genera el conjunto de Julia para c=-0.8+0.156i. Itera z_{n+1}=z_n²+c desde z_0=-0.5+0.5i en rejilla 800x800. Colorea por velocidad de escape con mapa 'plasma' y compara con Mandelbrot.
​