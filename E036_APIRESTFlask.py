"""
API REST muy simple con Flask
Crea una API REST básica con Flask para gestionar una lista de tareas (similar a TODO list), pero ahora vía HTTP.
Debe tener al menos:
- Ruta GET /tareas que devuelva en JSON la lista de tareas.
- Ruta POST /tareas que reciba una tarea en JSON y la añada.
- Ruta DELETE /tareas/<id> que elimine una tarea por su identificador.
"""

# Programa 36: API REST simple con Flask
# Para ejecutar: pip install flask
# Luego: python E036_APIRESTFlask.py
# Probar con curl o Postman:
# GET http://127.0.0.1:5000/tareas
# POST http://127.0.0.1:5000/tareas con JSON {"tarea": "Comprar leche"}
# DELETE http://127.0.0.1:5000/tareas/0

from flask import Flask, jsonify, request  # Para API JSON
import uuid  # Para generar IDs únicos

app = Flask(__name__)

# Lista de tareas en memoria (en una aplicación real estaría en BD)
tareas = []


@app.route("/tareas", methods=["GET"])
def listar_tareas():
    """
    Devuelve todas las tareas en formato JSON.
    """
    return jsonify([{
        "id": tarea["id"],
        "descripcion": tarea["descripcion"],
        "completada": tarea["completada"]
    } for tarea in tareas])


@app.route("/tareas", methods=["POST"])
def anadir_tarea():
    """
    Añade una nueva tarea desde JSON.
    """
    datos = request.get_json()
    if not datos or "tarea" not in datos:
        return jsonify({"error": "Se necesita campo 'tarea'"}), 400

    nueva_tarea = {
        "id": str(uuid.uuid4()),  # ID único
        "descripcion": datos["tarea"],
        "completada": False
    }
    tareas.append(nueva_tarea)
    return jsonify(nueva_tarea), 201


@app.route("/tareas/<id_tarea>", methods=["DELETE"])
def eliminar_tarea(id_tarea):
    """
    Elimina una tarea por su ID.
    """
    for i, tarea in enumerate(tareas):
        if tarea["id"] == id_tarea:
            tarea_eliminada = tareas.pop(i)
            return jsonify({"eliminada": tarea_eliminada})
    return jsonify({"error": "Tarea no encontrada"}), 404


def main():
    """
    Función principal que ejecuta la API.
    """
    print("API REST iniciada en http://127.0.0.1:5000")
    print("Rutas disponibles:")
    print("  GET    /tareas")
    print("  POST   /tareas")
    print("  DELETE /tareas/<id>")
    app.run(debug=True, host="127.0.0.1", port=5000)


if __name__ == "__main__":
    main()
