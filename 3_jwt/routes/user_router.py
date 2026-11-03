from fastapi import APIRouter
from auth.hash_password import HashPassword
from pydantic import BaseModel
from auth.jwt_handler import create_access_token


hash_password = HashPassword()
user_router = APIRouter(tags=["User"])
data_set : list = []

class User(BaseModel):
    username : str
    password : str
    
@user_router.post("/signup")
async def sign_up( user : dict ):
    print("변경 전 pwd : ", user["password"] ) #user.password
    user["password"] = hash_password.create_hash( user["password"] )
    print("변경 후 pwd : ", user["password"] )
    
    data_set.append( user )
    data_set.append( {"username":"bbb", "password":"bbb"} )
    
    return data_set
@user_router.post("/signin")
async def sign_in( user : dict ):
   
    result = hash_password.verify_hash(user["password"], data_set[0]["password"] )

    access_token = create_access_token( user["username"] )

    return { "token":access_token, "token_type":"Bearer" }


from auth.authenticate import authenticate
from fastapi import Depends, HTTPException, status

@user_router.get("/info/{username}")
async def user_info( username:str, user : str = Depends(authenticate) ):
    if username != user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="접근 권한이 없습니다")
    for data in data_set:
        if data["username"] == username: 
            return data
    raise HTTPException(status_code=404, detail="정보 없음")






