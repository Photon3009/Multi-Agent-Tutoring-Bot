from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from agents.tutor_agent import handle_query
import logging
from fastapi.middleware.cors import CORSMiddleware
from schemas.answer_response import AnswerResponse
from schemas.question_request import QuestionRequest

# Setup logging for FastAPI and application-wide logging
logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s",  # Log format with time, level, message
    level=logging.DEBUG,
)

# Create a logger for your application
logger = logging.getLogger(__name__)
logger.info("Starting the server...")

# Initialize FastAPI app
app = FastAPI(title="AI Tutor Agent API", version="1.0")

# Middleware for CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Define the root endpoint
@app.post("/ask", response_model=AnswerResponse)
async def ask_tutor(request: QuestionRequest):
    if not request.question.strip():
        raise HTTPException(status_code=400, detail="Question cannot be empty")

    answer = handle_query(request.question)
    return AnswerResponse(answer=answer)
