from pydantic import BaseModel, ConfigDict


class CreateTopic(BaseModel):
    topic_name = str


class CreateQuestion(BaseModel):
    quiz = str


class QuestionResponse(BaseModel):
    quiz_id: int
    topic_name: str
    model_config = ConfigDict(from_attributes=True)
