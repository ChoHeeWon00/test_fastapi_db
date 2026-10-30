from fastapi import FastAPI
from fastapi import APIRouter

from pydantic import BaseModel

from fastapi import Path


class User(BaseModel):
    name : str
    age : int
    addr : str

app = FastAPI(title="test FastAPI", description="부연설명", version="1.1")
#python -m uvicorn ex01:app --port 8000 --reload
router = APIRouter(tags=["회원 관리"])
router_agent = APIRouter(tags=["에이전트"])

@router_agent.get("/test")
def test():
    return {"msg":"데이터 요청"}


@router.post("/test")
def test( user : User ):
    return {"msg":f"데이터 추가 : {user}" }


@router_agent.put("/test")
def test():
    return {"msg":"데이터 수정"}
@router.delete("/test")
def test():
    return {"msg":"데이터 삭제"}


users = [
    User(name="홍길동", age=20, addr="산골짜기"),
    User(name="김개똥", age=30, addr="개똥별"),
    User(name="고길동", age=40, addr="마포구"),
]
@router.get("/api/users")
def get_users():
    print( users )
    return {"users": users }

@router.get("/api/path/{name}")
def get_users(name : str = Path(..., description="input u name") ):
    print( "name : ", name )
    for u in users:
        if u.name == name:
            return {"user" : u}
    return {"user": "존재하지 않는 이름" }

from fastapi import Query
@router.get("/api/path")
def get_users(name : str = Query(None ,description="input u name") ):
    print( "name : ", name )
    for u in users:
        if u.name == name:
            return {"user" : u}
    return {"user": "존재하지 않는 이름" }

app.include_router(router=router)
app.include_router(router=router_agent)

