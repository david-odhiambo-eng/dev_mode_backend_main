from app.db.db_connections import Base
from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.dialects.postgresql import UUID
import uuid


class Topic(Base):
    __tablename__ = "topics"
    id = Column(Integer, primary_key=True, index=True)
    topic_name = Column(String(30), nullable=False, unique=True)


class Question(Base):
    __tablename__ = "questions"
    id = Column(Integer, primary_key=True, index=True)
    quiz = Column(String, nullable=False, unique=True)
    answer = Column(String, nullable=True, unique=False)
    key_word = Column(String, nullable=True, unique=False)


class TopicsQuestions(Base):
    __tablename__ = "topics_questions"
    topic_id = Column(
        Integer,
        ForeignKey("topics.id"),
        primary_key=True,
        index=True,
    )
    quiz_id = Column(
        Integer,
        ForeignKey("questions.id"),
        primary_key=True,
        index=True,
    )
