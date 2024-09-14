from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.core.database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    username = Column(String, unique=True, index=True)
    password = Column(String)


class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    status = Column(String)
    created_by = Column(Integer, ForeignKey("users.id"))
    responsible = Column(Integer, ForeignKey("users.id"))

    creator = relationship("User", foreign_keys=[created_by])
    assigned_user = relationship("User", foreign_keys=[responsible])


class Comment(Base):
    __tablename__ = "comments"
    id = Column(Integer, primary_key=True, index=True)
    content = Column(String)
    id_user = Column(Integer, ForeignKey("users.id"))
