from sqlalchemy import Column, Integer, String, Date, Time, DateTime
from sqlalchemy.sql import func

from db import Base


class Reservation(Base):
    __tablename__ = "reservations"

    id = Column(Integer, primary_key=True, index=True)

    full_name = Column(String(100), nullable=False)

    email = Column(String(100), nullable=False)

    phone = Column(String(20), nullable=False)

    guests = Column(Integer, nullable=False)

    reservation_date = Column(Date, nullable=False)

    reservation_time = Column(Time, nullable=False)

    occasion = Column(String(100))

    special_request = Column(String(500))

    status = Column(String(20), default="Pending")

    created_at = Column(DateTime(timezone=True), server_default=func.now())