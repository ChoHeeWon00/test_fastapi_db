'''
auth
 - jwt_handler.py
'''
import time
from jose import jwt, JWTError, ExpiredSignatureError
from fastapi import HTTPException, status
SECRET_KEY = "비밀 키"

def verify_access_token(token : str):
    try:
        payload = jwt.decode( token, SECRET_KEY, algorithms=["HS256"])
        # payload["user"] = username, exp
        return payload
    except ExpiredSignatureError:
        raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="토큰 만료. 인증 먼저 하세요")
    except JWTError:
        raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="잘못된 요청입니다")


def create_access_token( username : str ):
    payload = {
        "user" : username,
        "exp" : time.time() + 30 #10초 후 토큰 만료
    }
    # 헤더.페이로드.시그니처
    token = jwt.encode( payload, SECRET_KEY, algorithm="HS256")
    return token