'''
auth
 - hash_password.py
'''
from passlib.context import CryptContext

pwd_context = CryptContext( schemes=["bcrypt"] )

class HashPassword:
    def create_hash(self, password : str): 
        return pwd_context.hash( password )
    
    def verify_hash(self, plain_password:str, hashed_password:str):
        return pwd_context.verify( plain_password, hashed_password) #평문, 암호