from fastapi import FastAPI, HTTPException, Request
from google.cloud import firestore
import os

# Carga de variables de entorno
# PROJECT_ID: ID del proyecto de GCP donde existe Firestore
project_id = os.environ["GOOGLE_CLOUD_PROJECT"]
# DATABASE_ID: Nombre de la base de datos Firestore (db-notes)
database_id = os.environ["FIRESTORE_DATABASE"]

# Inicialización del cliente de Firestore
# Creamos el cliente de Firestore pasándole explícitamente el project_id y el database_id
db = firestore.Client(project=project_id, database=database_id)

# Configuración de la app FastAPI
app = FastAPI(title="Notas con Firestore real")

# Endpoint: Listar todas las notas
# Método: GET /notes
@app.get("/notes")
async def list_notes():
    # 1. Accedemos a la colección "notes"
    docs = db.collection("notes").stream()
    # 2. Convertimos cada documento en un diccionario con su ID y datos
    return [{"id": d.id, **d.to_dict()} for d in docs]

# Endpoint: Crear una nueva nota
# Método: POST /notes
@app.post("/notes")
async def create_note(req: Request):
    # 1. Leemos el JSON del cuerpo de la petición
    data = await req.json()

    # 2. Validamos que existan los campos obligatorios 'title' y 'content'
    if not data.get("title") or not data.get("content"):
        raise HTTPException(status_code=400, detail="Faltan 'title' o 'content'")

    # 3. Creamos un nuevo documento con ID automático en la colección "notes"
    ref = db.collection("notes").document()

    # 4. Guardamos los datos junto con la fecha de creación del servidor
    ref.set({
        "title": data["title"],
        "content": data["content"],
        # SERVER_TIMESTAMP inserta la fecha/hora actual del servidor
        "created_at": firestore.SERVER_TIMESTAMP
    })

    # 5. Devolvemos el ID del documento recién creado
    return {"id": ref.id}
