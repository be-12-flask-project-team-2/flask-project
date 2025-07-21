from datetime import datetime
from sqlalchemy import Column, Integer, String, Enum, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    age = Column(
        Enum('teen', 'twenty', 'thirty', 'forty', 'fifty', name='age_enum', native_enum=False),
        nullable=False
    )
    gender = Column(
        Enum('male', 'female', 'other', name='gender_enum', native_enum=False),
        nullable=False
    )
    email = Column(String(120), unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f"<User(name={self.name}, age={self.age}, gender={self.gender}, email={self.email})>"
