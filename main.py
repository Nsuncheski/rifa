from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

# Definimos el modelo de datos de entrada
class Compra(BaseModel):
    numeros: list
    nombre: str
    cel: int
    email: str

# Definimos la ruta que maneja las solicitudes POST
@app.post("/rifapost")
async def nueva_compra(compra: Compra):
    # Procesamos los datos recibidos
    numeros_seleccionados = compra.numeros
    nombre = compra.nombre
    cel = compra.cel
    email = compra.email

    # Realizamos alguna acción con los datos recibidos
    # ...
    print(f"{numeros_seleccionados}, {nombre}, {cel}, {email}")
    # Devolvemos una respuesta indicando que la compra fue exitosa
    return {"mensaje": "La compra se realizó correctamente."}

@app.get("/saludo")
async def nueva_compra():
    return Compra(numeros=[5,20], nombre="Nahuel", cel=1569347524, email="nagubera@gmail.com" )