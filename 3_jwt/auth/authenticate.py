
from fastapi import Security, HTTPException, status
from auth.jwt_handler import verify_access_token
from fastapi.security import APIKeyHeader
api_key_header = APIKeyHeader(name="Authorization")

async def authenticate(token : str = Security(api_key_header) ):
    #token = Bearea token정보
    print("token : ", token)
    if token.startswith("Bearer "):
        token = token.replace("Bearer ", "")
    print("변경 후 token : ", token)

    payload = verify_access_token( token )
    print("authenticate payload : ", payload)

    return payload["user"]