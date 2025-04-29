from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"
    id       = Column(Integer, primary_key=True, index=True)
    email    = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    wallets  = relationship("Wallet", back_populates="owner")

class Wallet(Base):
    __tablename__ = "wallets"
    id       = Column(Integer, primary_key=True, index=True)
    address  = Column(String, unique=True, index=True, nullable=False)
    encrypted_key = Column(String, nullable=False)
    user_id  = Column(Integer, ForeignKey("users.id"))
    owner    = relationship("User", back_populates="wallets")
