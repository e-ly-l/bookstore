from pydantic import BaseModel
import enum
from fastapi import Query


class Role(str, enum.Enum):
    admin: str = "admin"
    personnel: str = "personnel"


class User(BaseModel):
    name: str
    password: str
    mail: str
    #mail: str = Query(..., regex="^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.])\.([a-zA-z]{2,5})$")
    role: str