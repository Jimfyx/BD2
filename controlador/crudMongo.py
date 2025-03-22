from importlib.metadata import metadata

from pymongo import MongoClient
from bson import ObjectId
from datetime import datetime


class MongoDB:
    def __init__(self,uri, nombreDb):
        self.cliente = MongoClient(uri)
        self.bdd = self.cliente[nombreDb]

    def insertarRegistro(self,coleccion,registro,usuario="Anon"):
        col = self.bdd[coleccion]
        try:
            metadata ={
                "usuario":usuario,
                "fechaCreacion":datetime.utcnow(),
                "bitacora":[
                    {
                        "operacion":"REGISTRO CREADO",
                        "fecha":datetime.utcnow(),
                        "observacion":"Creacion del documento"
                    }
                ]
            }
            if isinstance(registro,list):
                #si es una lsita
                for r in registro:
                    r["metadata"] = metadata

                resultado = col.insert_many(registro)
                return "Exito", [obj for obj in resultado.inserted_ids]
            else:
                registro["metadata"] = metadata
                resultado = col.insert_one(registro)
                return "Exito", resultado.inserted_id
        except Exception as e:
            return "Error", str(e)

    def obtenerRegistro(self, coleccion, query):
        col = self.bdd[coleccion]
        try:
            resultado = col.aggregate(query)
            return "Exito", resultado
        except Exception as e:
            return "Error", str(e)


    def actualizarRegistro(self, coleccion, filtro, nuevosValores, tipo, usuario = "Anon"):
        col = self.bdd[coleccion]
        try:
            update = {}
            if tipo == 1:
                update = {
                "$set": nuevosValores,
                "$push":{
                    "metadata.bitacora":{
                        "operacion": "ACTUALIZACION DE REGISTRO",
                        "fecha": datetime.utcnow(),
                        "observacion": "",
                        "usuario":usuario
                    }
                }
            }
            else:
                update = {
                    "$push": nuevosValores,

                }
            resultado = col.update_many(filtro,update)

            if resultado.modified_count > 0:
                updateBitacora = {
                    "metadata.bitacora": {
                        "operacion": "ACTUALIZACION CREADO",
                        "fecha": datetime.utcnow(),
                        "observacion": "Actualizacion del documento",
                        "usuario":usuario
                    }
                }
                col.update_many(filtro, updateBitacora)
            return "Exito", resultado.modified_count

        except Exception as e:
            return "Error", str(e)

