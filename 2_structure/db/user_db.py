from schemas.user_schemas import User

users : list[User] = [
    User(username="aaa", password="aaa", email="aaa@aaa.aaa", name="홍길동"),
    User(username="bbb", password="bbb", email="bbb@bbb.bbb", name="김개똥"),
]

async def get_users() -> list[User]:
    return users

async def get_user(email : str) -> User | None:
    print("email 데이터베이스 연결 : ",email)
    for u in users:
        print( u )
        if u.email == email:
            return u
    return None

async def insert( user : User ) -> User | None:
    #print("insert user : ", user)
    for u in users:
        if u.username == user.username:
            return None
    users.append( user )
    return user
'''
users : list[User] = [
    User(username="aaa", password="aaa", email="aaa@aaa.aaa", name="홍길동"),
    User(username="bbb", password="bbb", email="bbb@bbb.bbb", name="김개똥"),
]
'''
async def update( username:str, user:User):
    for i, u in enumerate(users):
        if u.username == username:
            users[i] = user
            #u = user
            return u
    return None

async def delete( username:str ):
    for i, u in enumerate(users):
        if u.username == username:
            del_user = users.pop( i )
            return del_user
    return None
    