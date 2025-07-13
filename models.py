from pydantic import BaseModel
from typing import List
from datetime import datetime

class User(BaseModel):
    name: str
    company: str
    email: str

class MessageLog(BaseModel):
    timestamp: datetime
    message: str
    response: str

class UserSession(BaseModel):
    user_id: str
    logs: List[MessageLog]
