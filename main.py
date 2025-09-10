from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import random
import json
import os

app = FastAPI()

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static folder for serving images
app.mount("/static", StaticFiles(directory="static"), name="static")

# Load questions
QUESTIONS_FILE = "questions.json"
if not os.path.exists(QUESTIONS_FILE):
    raise FileNotFoundError("questions.json file missing.")

with open(QUESTIONS_FILE, "r") as f:
    questions = json.load(f)

@app.get("/")
def read_root():
    return FileResponse("index.html")

@app.get("/api/generate_question")
def generate_question():
    if not questions:
        return {"error": "No questions found!"}

    question = random.choice(questions)
    return {
        "question": question["question"],
        "image": question.get("image", None),
        "options": question["options"],
        "correct_answer": question["answer"],
        "brief_solution": question["brief"],
        "detailed_explanation": question["detailed"]
    }
