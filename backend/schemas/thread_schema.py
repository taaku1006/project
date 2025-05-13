from pydantic import BaseModel

class ThreadCreate(BaseModel):
    title: str

class ThreadResponse(BaseModel):
    id: int
    title: str

    class Config:
        orm_mode = True
