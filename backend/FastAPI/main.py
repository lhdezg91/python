from fastapi import FastAPI
#pip install fastapi
#pip install uvicorn

#correr el servidor Uvicorn
# uvicorn main:app --reload
#cada vez que hagas un cambio en el codigo este se recarga automaticamente

#Uvicorn genera sola la documentacion a raiz de la lectura del codigo solo tienes que escribir /docs o /redoc




app = FastAPI()

@app.get("/")
async def root():
    return "Hola!"

@app.get("/curso")
async def url_curso():
    return {"url_curso":"https://lian.com"}