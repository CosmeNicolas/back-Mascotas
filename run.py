from flask import Flask, request, jsonify
from flask_cors import CORS
from app.views import *

app = Flask(__name__)
CORS(app)


# Rutas
app.route('/', methods=['GET'])(index)
app.route('/api/adopciones/', methods=['GET'])(get_all_adoptions)
app.route('/api/adopciones/<int:adopcion_id>', methods=['GET'])(get_adopcion)
app.route('/api/adopciones/', methods=['POST'])(create_adopcion)
app.route('/api/adopciones/<int:adopcion_id>', methods=['PUT'])(update_adopcion)
app.route('/api/adopciones/<int:adopcion_id>', methods=['DELETE'])(delete_adopcion)

if __name__ == '__main__':
    app.run(debug=True)