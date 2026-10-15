from pydantic import BaseModel

class GetQuestions(BaseModel):
    topic_id: list[int]