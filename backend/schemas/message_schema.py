from pydantic import BaseModel

class MessageCreate(BaseModel):
    thread_id: int
    content: str

class MessageResponse(BaseModel):
    id: int
    thread_id: int
    content: str

    class Config:
        orm_mode = True
