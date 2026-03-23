from pydantic import BaseModel

class TextData(BaseModel):
    text: str
    max_len: int = 130
    min_len: int = 30