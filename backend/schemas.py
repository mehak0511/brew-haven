from pydantic import BaseModel, EmailStr
from datetime import date, time


class ReservationCreate(BaseModel):
    full_name: str
    email: EmailStr
    phone: str
    guests: int
    reservation_date: date
    reservation_time: time
    occasion: str | None = None
    special_request: str | None = None


class ReservationResponse(ReservationCreate):
    id: int
    status: str

    class Config:
        from_attributes = True