from fastapi import APIRouter, status, Depends, HTTPException
from app.schemas.topic_quiz import CreateTopic, CreateQuestion, QuestionResponse
from sqlalchemy.orm import Session
from app.db.db_connections import get_db
from app.db.topics_quiz_table import Topic, Question, TopicsQuestions

topic_quiz_router = APIRouter(tags=["TOPICS AND QUESTIONS"])


@topic_quiz_router.post(
    "/topic_quiz", status_code=status.HTTP_201_CREATED, response_model=QuestionResponse
)
def create_topic_and_quiz(
    topic_data: CreateTopic, quiz_data: CreateQuestion, db: Session = Depends(get_db)
):

    try:
        topic = (
            db.query(Topic).filter(Topic.topic_name == topic_data.topic_name).first()
        )
        if not topic:
            topic = Topic(topic_name=topic_data.topic_name)
            db.add(topic)
            db.flush()

        question = Question(
            quiz=quiz_data.quiz, answer=quiz_data.answer, key_word=quiz_data.key_word
        )
        db.add(question)
        db.flush()

        topic_quiz = TopicsQuestions(topic_name=topic.topic_name, quiz_id=question.id)
        db.add(topic_quiz)

        db.commit()

        return QuestionResponse(quiz_id=question.id, topic_name=topic.topic_name)

    except Exception:
        db.rollback()
        raise HTTPException(
            detail="TOPIC ALREADY EXISTS", status_code=status.HTTP_409_CONFLICT
        )
