from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db import get_db
from schemas import ReservationCreate, ReservationResponse
from services import create_reservation

# Create a router object
router = APIRouter()


@router.post(
    "/reservations",
    response_model=ReservationResponse
)
def reserve_table(
    reservation: ReservationCreate,
    db: Session = Depends(get_db)
):
    return create_reservation(db, reservation)