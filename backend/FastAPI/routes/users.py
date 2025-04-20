from queue import Full
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel


router = APIRouter()

# uvicorn users:app --reload

#Entidad User
class User(BaseModel):
    id: int
    name: str
    apellido: str
    email: str
    edad: int
    
user_list = [User(id=1,name="Lian", apellido="Hernandez",email= "lian@gmail.com",edad= 32),
             User(id=2,name="Ivis", apellido="Garcia", email="ivis@gmail.com",edad= 33),
             User(id=3,name="Ian", apellido="Hernandez",email= "ian@gmail.com", edad=6)]

@router.get("/users")
async def users():
    return user_list

# Path
@router.get("/user/{id}")
async def user(id:int):
    return get_user(id)

# Query
#/user/?id=1
@router.get("/user/")
async def user(id:int):
    #clasico
    #for i in user_list:
    #    if (i.id == id):
    #        return i   
    return get_user(id)
    
    
def get_user(id:int):
    users = filter(lambda user: user.id==id, user_list ) 
    try:
        return list(users)[0]
    except:
        return {"error":"El usuario no existe"}

@router.get("/users_json")
async def users_json():
    return [{"name":"Lian", "apellido":"Hernandez","email":"lian@gmail.com","edad": 32},
            {"name":"Ivis", "apellido":"Garcia","email":"ivis@gmail.com", "edad": 33},
            {"name":"Ian", "apellido":"Hernandez","email":"ian@gmail.com", "edad": 6}]

#Añadir usuario
@router.post("/user/",status_code=201)
async def user_add(user:User):
    if search_user(user.id) == user:
        #esta es la manera correcta
        raise HTTPException(status_code=404,detail="El usuario ya existe")
    else:
        user_list.append(user)
        return user
    
#Actualizar usuario
@router.put("/user/")
async def user_update(user:User):
    update = False
    
    for index, usuario in enumerate(user_list):
        if usuario.id == user.id:
            user_list[index] = user
            update = True
            return user
            
    if not update:
        return {"error":"El usuario no se actualizo"}

#Eliminar usuario
@router.delete("/user/")
async def user_delete(user:User):
    update = False
    for index, usuario in enumerate(user_list):
        if usuario.id == user.id:
            del user_list[index]
            update = True
            
    if not update:
        return {"error":"El usuario no existe"}
        
def search_user(id):
    users = filter(lambda user: user.id==id, user_list ) 
    try:
        return list(users)[0]
    except:
        return {"error":"El usuario no existe"}
    