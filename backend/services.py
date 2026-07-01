from sqlalchemy.orm import Session
from models import Reservation
from schemas import ReservationCreate


def create_reservation(db: Session, reservation: ReservationCreate):

    new_reservation = Reservation(
        full_name=reservation.full_name,
        email=reservation.email,
        phone=reservation.phone,
        guests=reservation.guests,
        reservation_date=reservation.reservation_date,
        reservation_time=reservation.reservation_time,
        occasion=reservation.occasion,
        special_request=reservation.special_request
    )

    db.add(new_reservation)
    db.commit()
    db.refresh(new_reservation)

    return new_reservation