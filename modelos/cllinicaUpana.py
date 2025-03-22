import sys
sys.path.append('E:/Proyectos/webdev/BaseDatos2/intro/BD2')
from controlador.crudMongo import MongoDB
from bson import ObjectId



_URIMONGO = "mongodb://admin:upana123@localhost:27017/?authSource=admin"
_NOMBREBDD = "clinicaUpana"

col ="clinica"
colEspecialidad = "especialidad"
colDoctores = "doctores"


class clinica:
    def __init__(self):
        self.db = MongoDB(_URIMONGO, _NOMBREBDD)

    def reservarCita(self):
        #todo crear la cita
        return "no implementado"

# Especialidades

    def insertarCatalogoEsecialidades(self, especialidad):
        if especialidad == '':
            return "", "Falta la especialiad"

        especialidadReg = {
            "especialidad":str(especialidad).upper(),

            "activo":True
        }

        msg, id = self.db.insertarRegistro(colEspecialidad,especialidadReg,"")
        return msg,id


    def obtenerEspecialista(self):
        query = [
            {
                "$match": {
                    "activo": True
            }
            },
            {
                "$project":{
                    "especialidad":1,
                    "_id":{"$toString":"$_id"}
                }
            }
        ]
        msg, reg = self.db.obtenerRegistro(colEspecialidad,query)
        return msg,reg

# Fin de Especialidades

    def insertarDoctores(self, nombre, apellido, especialidad, otrosDatos):

        if nombre == "":
            return "", "El doctor debe de tener un nombre"
        if apellido == "":
            return "", "El doctor debe de tener un apellido"
        if especialidad == "":
            return "", "Debe de tener al menos una especialidad"


        nombreDoctor ={
            'nombre': nombre,
            "activo":True
        }

        apellidoDoctor ={
            'apellido': apellido,
            "activo":True
        }

        especialidad ={
            "id":especialidad,
            "activo":True
        }

        nombres =[]
        apellidos =[]
        especialidades = []

        nombres.append(nombreDoctor)
        apellidos.append(apellidoDoctor)
        especialidades.append(especialidad)


        datos = []

        datos.append(otrosDatos)

        doctor = {
            "activo":True,
            "especialidades":especialidades,
            "nombre":nombres,
            "apellido":apellidos,
            "datos":datos
        }
        msg, id = self.db.insertarRegistro(colDoctores,doctor,"")
        return msg

    def obtenerDoctores(self):
        query = [
            {"$match": {"activo": True}},
            {"$project": {"_id": {"$toString": "$_id"}, "nombre": 1, "apellido": 1, "especialidades": 1}}
        ]
        msg, reg = self.db.obtenerRegistro(colDoctores, query)
        return msg, reg

    def actualizarEspecialidadDoctores(self, doctor, nuevaEspecialidad):
        filtro= {"_id": ObjectId(doctor)}

        if nuevaEspecialidad == "":
            return "", "Falta la especialidad"
        else:

            datosNuevos = {
                "especialidades": {
                    "id": str(nuevaEspecialidad).upper(),
                    "activo": True
                }}
        return self.db.actualizarRegistro(colDoctores,filtro,datosNuevos,2)