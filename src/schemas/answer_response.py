from pydantic import BaseModel

# This file defines the AnswerResponse schema for the AI Tutor API.
class AnswerResponse(BaseModel):
    answer: str