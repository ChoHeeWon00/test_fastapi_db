
from fastapi import APIRouter, HTTPException, status
from schemas.user_schemas import User
from db import user_db

user_router = APIRouter(tags=["User"])

@user_router.get("/test")
async def test() -> dict:
    return {"msg":"test"}

@user_router.get("/")
async def get_users() -> list[User] :
    users = await user_db.get_users()
    print( users )
    return users

@user_router.get("/{email}",
                  response_model=User,
                  status_code=201
                  )
async def get_user(email : str) :
    print("email route 연결 : ", email)
    user = await user_db.get_user( email )
    print( user )
    if user:
        return user
    raise HTTPException(
                    status_code = status.HTTP_404_NOT_FOUND , 
                    detail="존재하는 사용자 없음!"
                )

@user_router.post("/",
                  response_model=User,
                  status_code=201,
                  summary="회원가입입니다",
                  responses={ 409:{"description":"중복id"} }
                  )
async def post_user(user : User) -> User:
    #print("사용자 추가 router : ", user)
    result = await user_db.insert( user )
    if not result: #None 거짓
        raise HTTPException(
            status_code = status.HTTP_409_CONFLICT,
            detail = "중복된 id 입니다."
        )
    return result

@user_router.put("/{username}")
async def update_user( username:str , user:User):
    #print( "라우터 연결" )
    #print( username )
    #print( user )
    
    result = await user_db.update(username, user)
    if result:
        return result
    raise HTTPException(
                status_code=404, 
                detail="수정 사용자 id 없음!!!"
        )
    #return None

@user_router.delete("/{username}")
async def delete_user(username : str) -> User:
    result = await user_db.delete( username )
    if result:
        return result
    raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="user not found"
        )

