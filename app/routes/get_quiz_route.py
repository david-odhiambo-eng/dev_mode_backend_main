from fastapi import APIRouter, status, Depends, HTTPException, status
from app.schemas.get_quiz import GetQuestions
from app.db.topics_quiz_table import Question, TopicsQuestions
from sqlalchemy.orm import Session
from app.db.db_connections import get_db
from sqlalchemy import func

quiz_router = APIRouter(tags=["QUESTIONS"])


@quiz_router.post("/questions", status_code=status.HTTP_200_OK)
def get_questions(topic_names: GetQuestions, db: Session = Depends(get_db)):
    try:
        questions = (
            db.query(Question)
            .join(TopicsQuestions, Question.id == TopicsQuestions.quiz_id)
            .filter(TopicsQuestions.topic_name.in_(topic_names.topic_names))
            .order_by(func.random())
            .limit(100)
            .all()
        )
        return questions

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"{e}"
        )
