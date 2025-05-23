
from pydantic import BaseModel

# This file defines the QuestionRequest schema for the AI Tutor API.
class QuestionRequest(BaseModel):
    question: str
