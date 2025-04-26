from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

app = FastAPI()
oauth2 = OAuth2PasswordBearer(tokenUrl="login")

class User(BaseModel):
    username: str
    full_name: str
    activo: bool
    email: str
    edad: int

class UserDB(User):
    password:str

users_db = {
    "lhdezg":{
            "username":"lhdezg",
            "full_name":"Lian",
            "activo":True,
            "email": "lian@gmail.com",
            "edad": 32,
            "password":"123456"
        },
    "ivisgm":{
            "username":"ivisgm",
            "full_name":"Ivis",
            "activo":True,
            "email": "ivis@gmail.com",
            "edad": 33,
            "password":"123456"
        },
    "ian":{
            "username":"ianhg",
            "full_name":"Ian",
            "activo":False,
            "email": "ian@gmail.com",
            "edad": 6,
            "password":"123456"
        }        
}

async def current_user(token:str = Depends(oauth2)):
    user = search_user(token)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="No esta autorizado")
    return user
    

def search_user(username: str):
    if username in users_db:
        return UserDB(**users_db[username])#** significa que le puedes pasar la cantidad de paramatros arbitraria


@app.get("/")
async def root():
    return {"message":"Hola"}

@app.post("/login")
async def login(form:OAuth2PasswordRequestForm = Depends()):
    #print(type(users_db)) es un diccionario
    user_db = users_db.get(form.username)
    print(user_db)
    if not user_db:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="El usuario es incorrecto")
    
    user = search_user(form.username)
    
    if not user.password == form.password:
        raise HTTPException(status_code=400, detail="La contrasena es incorrecta")
    
    #esto es un ejemplo el token_access deberia ser algo encriptado
    return {"access_token": user.username, "token_type":"bearer"}

@app.get("/users/me")
async def me(user: User = Depends(current_user)):
    return user