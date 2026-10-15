from fastapi import APIRouter, status, Depends
from app.schemas.get_quiz import GetQuestions
from app.db.topics_quiz_table import Question, Topic, TopicsQuestions
from sqlalchemy.orm import Session
from app.db.db_connections import get_db
from sqlalchemy import func

quiz_router = APIRouter(tags=["QUESTIONS"])


@quiz_router.post("/questions", status_code=status.HTTP_201_CREATED)
def get_questions(topic_ids: GetQuestions, db: Session = Depends(get_db)):
    questions = (
        db.query(Question)
        .join(TopicsQuestions, Question.id == TopicsQuestions.quiz_id)
        .filter(TopicsQuestions.topic_id.in_(topic_ids.topic_id))
        .distinct()
        .order_by(func.random())
        .limit(100)
    )

    return questions
