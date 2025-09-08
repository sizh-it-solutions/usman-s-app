from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
import random
import json
import os

app = FastAPI()

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # agar specific domain chahiye to ["http://127.0.0.1:5500"] use karo
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load questions
QUESTIONS_FILE = "questions.json"
if not os.path.exists(QUESTIONS_FILE):
    raise FileNotFoundError("questions.json file missing. Please add it in project folder.")

with open(QUESTIONS_FILE, "r") as f:
    questions = json.load(f)

@app.get("/")
def read_root():
    """Serve frontend HTML"""
    return FileResponse("index.html")

@app.get("/api/generate_question")
def generate_question():
    """Return a random question"""
    if not questions:
        return {"error": "No questions found!"}

    question = random.choice(questions)
    return {
        "question": question["question"],
        "options": [
            f"A. {question['options'][0]}",
            f"B. {question['options'][1]}",
            f"C. {question['options'][2]}",
            f"D. {question['options'][3]}"
        ],
        "correct_answer": question["answer"],
        "brief_solution": question["brief"],
        "detailed_explanation": question["detailed"]
    }
