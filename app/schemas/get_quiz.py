from pydantic import BaseModel

class GetQuestions(BaseModel):
    topic_names: list[str]