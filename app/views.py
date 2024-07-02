from flask import jsonify, request
from app.models import AdopcionMascota

# Ruta de inicio básica
def index():
    return '<h1>Hola mundo con flask 🐍</h1>'

# Obtener todas las adopciones de mascotas
def get_all_adoptions():
    adoptions = AdopcionMascota.get_all()
    list_adoptions = [adoption.serialize() for adoption in adoptions]
    return jsonify(list_adoptions)

# Crear una nueva adopción de mascota
def create_adopcion():
    # Recibe los datos enviados en la petición en formato JSON
    data = request.json
    new_adoption = AdopcionMascota(
        nombrePersona=data['nombrePersona'],
        correo=data['correo'],
        telefono=data['telefono'],
        animal_de_interes=data['animal_de_interes']
    )
    new_adoption.save()
    return jsonify({'message': 'Adopción de mascota creada con éxito'}), 201

# Actualizar una adopción de mascota existente por ID
def update_adopcion(adopcion_id):
    adoption = AdopcionMascota.get_by_id(adopcion_id)
    if not adoption:
        return jsonify({'message': 'Adopción de mascota no encontrada'}), 404
    data = request.json
    adoption.nombrePersona = data['nombrePersona']
    adoption.correo = data['correo']
    adoption.telefono = data['telefono']
    adoption.animal_de_interes = data['animal_de_interes']
    adoption.save()
    return jsonify({'message': 'Adopción de mascota actualizada exitosamente'})

# Obtener una adopción de mascota por ID
def get_adopcion(adopcion_id):
    adoption = AdopcionMascota.get_by_id(adopcion_id)
    if not adoption:
        return jsonify({'message': 'Adopción de mascota no encontrada'}), 404
    return jsonify(adoption.serialize())

# Eliminar una adopción de mascota por ID
def delete_adopcion(adopcion_id):
    adoption = AdopcionMascota.get_by_id(adopcion_id)
    if not adoption:
        return jsonify({'message': 'Adopción de mascota no encontrada'}), 404
    adoption.delete()
    return jsonify({'message': 'Adopción de mascota eliminada exitosamente'}), 200