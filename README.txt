Quiz App (FastAPI + HTML/JS Frontend)
Overview
This is a simple Quiz Application built with FastAPI (Backend) and HTML, CSS, JavaScript (Frontend). It loads questions from a questions.json file, displays them randomly, and allows the user to:
- Generate a new question
- Select an answer and submit
- View the correct answer
- Read a Brief Solution
- Expand to see a Detailed Explanation
Features
✅ Random question generator
✅ Multiple-choice options (A, B, C, D)
✅ Correct answer validation
✅ Brief & detailed explanations
✅ Clean and attractive UI
✅ CORS enabled for smooth frontend-backend communication
Project Structure
quiz-app/
│── main.py          # FastAPI backend
│── index.html       # Frontend UI
│── questions.json   # Questions database (Q/A/Brief/Detailed)
Installation & Setup
1. Clone the repository
git clone https://github.com/yourusername/quiz-app.git
cd quiz-app
2. Create a virtual environment
python3 -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
3. Install dependencies
pip install fastapi uvicorn
4. Run the server
uvicorn main:app --reload --port 8001
5. Open the app in browser
http://127.0.0.1:8001/
API Documentation
Endpoint: /api/generate_question
Returns one random question from questions.json
Example Response:
{
  "question": "What is 2+2?",
  "options": ["A. 2", "B. 3", "C. 4", "D. 5"],
  "correct_answer": "C",
  "brief_solution": "2+2 equals 4",
  "detailed_explanation": "Adding two and two gives four because ..."
}
Test API in Swagger UI:
http://127.0.0.1:8001/docs
questions.json Format
[
  {
    "question": "The Rudder controls which movement of an aircraft?",
    "options": ["pitch", "yaw", "roll", "turn"],
    "answer": "B",
    "brief": "The rudder controls yaw (nose left/right).",
    "detailed": "The rudder is located on the vertical tail ..."
  }
]
Frontend (index.html)
- Generate Question → fetches a random question
- Select an answer → Submit → shows Correct/Wrong
- Show Answer → reveals Brief Solution
- View Detailed Explanation → expands full explanation
Future Enhancements
- User score tracking
- Timer-based quizzes
- Multiple categories (Math, Science, Aviation, etc.)
- Leaderboard system
- Database integration (PostgreSQL / MongoDB)
Author
Developed by Usman ✨ (Feel free to modify and extend as per your needs)
