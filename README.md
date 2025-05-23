# Multi-Agent Tutoring Bot

This assistant (the "Tutor Agent") handle questions across different subjects. Instead of being a monolithic system, it will intelligently route questions to specialized agents, each an expert in its domain (e.g., mathematics, physics). These specialist agents might also need to use "tools" (like a calculator or a data lookup function) to provide accurate answers.

## 🚀 Technology Stack

### Backend

- FastAPI

## 🛠️ Installation & Setup

### Local Development Setup

1. **Create and activate virtual environment**

   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the following command to start the dev server**

   ```bash
   uvicorn src.main:app
   ```

## 🌐 Accessing the Application

- Backend API: http://localhost:8000/docs

## Natural language understanding and response generation capabilities

- Google Gemini Model

### Endpoints

To Ask Tutor Agent

- POST /ask
- Body:

```json
{
  "question": "What is the speed of light?"
}
```

- Response:

```json
{
  "answer": "The speed of light is 299,792,458 m/s"
}
```
### Deployed APIs 
```bash
https://multi-agent-tutoring-bot.onrender.com/docs
```
