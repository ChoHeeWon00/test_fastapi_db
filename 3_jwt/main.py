from fastapi import FastAPI
import uvicorn
from routes.user_router import user_router

app = FastAPI()
app.include_router(user_router, prefix="/users")

from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
            CORSMiddleware,
            allow_credentials=True,
            allow_origins=["*"], #["http://localhost:3000", "...."]
            allow_methods=["*"], # http 메소드 허용(get, post 등)
            allow_headers=["*"]  # http 통신 헤더 받을 지(front 전달)
        )

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", 
                            port=8000, reload=True)
