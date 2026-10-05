from app.db.db_connections import Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
import uuid


class User(Base):
    __tablename__ = "users"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    player_name = Column(String(20), nullable=False)
    email = Column(String(255), unique=True)
    password = Column(String(255), nullable=False)


