from fastapi import FastAPI
#importar los ficheros de las rutas
from routes import users
from routes import products

#importar los recursos estaticos
from fastapi.staticfiles import StaticFiles
#pip install fastapi
#pip install uvicorn

#correr el servidor Uvicorn
# uvicorn main:app --reload
#cada vez que hagas un cambio en el codigo este se recarga automaticamente

#Uvicorn genera sola la documentacion a raiz de la lectura del codigo solo tienes que escribir /docs o /redoc




app = FastAPI()

#Rutas
app.include_router(products.router)
app.include_router(users.router)

#elementos estaticos
app.mount("/ian",StaticFiles(directory="static/imagenes"),name="ian")

@app.get("/")
async def root():
    return "Hola!"

@app.get("/curso")
async def url_curso():
    return {"url_curso":"https://lian.com"}