from pydantic import BaseModel

class UserBase(BaseModel):
    username:str
    password:str

class UserCreate(UserBase):
    email:str

class DocSearch(BaseModel):
    title: str
    author: str|None = None
    category: str|None = None
    
class Msg(BaseModel):
    message: str

class GetDocs(BaseModel):
    message: str
    user_id: int
    docs: list[DocSearch]
