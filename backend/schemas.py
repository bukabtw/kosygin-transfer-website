from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ConsultationRequestBase(BaseModel):
    name: str
    phone: str
    email: Optional[str] = None
    faculty: Optional[str] = None
    message: Optional[str] = None

class ConsultationRequestCreate(ConsultationRequestBase):
    pass

class ConsultationRequest(ConsultationRequestBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
