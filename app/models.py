from app.database import get_db

class AdopcionMascota:

    # Constructor
    def __init__(self, id_adopcion=None, nombrePersona=None, correo=None, telefono=None, animal_de_interes=None):
        self.id_adopcion = id_adopcion
        self.nombrePersona = nombrePersona
        self.correo = correo
        self.telefono = telefono
        self.animal_de_interes = animal_de_interes

    def serialize(self):
        return {
            'id_adopcion': self.id_adopcion,
            'nombrePersona': self.nombrePersona,
            'correo': self.correo,
            'telefono': self.telefono,
            'animal_de_interes': self.animal_de_interes
        }
    
    @staticmethod
    def get_all():
        db = get_db()
        cursor = db.cursor()
        query = "SELECT * FROM adopcion_mascotas"
        cursor.execute(query)
        rows = cursor.fetchall()

        adopciones = [AdopcionMascota(id_adopcion=row[0], nombrePersona=row[1], correo=row[2], telefono=row[3], animal_de_interes=row[4]) for row in rows]

        cursor.close()
        return adopciones

    @staticmethod
    def get_by_id(adopcion_id):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM adopcion_mascotas WHERE id_adopcion = %s", (adopcion_id,))
        row = cursor.fetchone()
        cursor.close()
        if row:
            return AdopcionMascota(id_adopcion=row[0], nombrePersona=row[1], correo=row[2], telefono=row[3], animal_de_interes=row[4])
        return None
    
    def save(self):
        db = get_db()
        cursor = db.cursor()
        if self.id_adopcion:
            cursor.execute("""
                UPDATE adopcion_mascotas SET nombrePersona = %s, correo = %s, telefono = %s, animal_de_interes = %s
                WHERE id_adopcion = %s
            """, (self.nombrePersona, self.correo, self.telefono, self.animal_de_interes, self.id_adopcion))
        else:
            cursor.execute("""
                INSERT INTO adopcion_mascotas (nombrePersona, correo, telefono, animal_de_interes) VALUES (%s, %s, %s, %s)
            """, (self.nombrePersona, self.correo, self.telefono, self.animal_de_interes))
            self.id_adopcion = cursor.lastrowid
        db.commit()
        cursor.close()

    def delete(self):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("DELETE FROM adopcion_mascotas WHERE id_adopcion = %s", (self.id_adopcion,))
        db.commit()
        cursor.close()