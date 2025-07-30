from fastapi import FastAPI, HTTPException
from models import Resume
from scorer import score_resume
from database import init_db, save_score

app = FastAPI()
init_db()

@app.post("/score")
def score(resume: Resume):
    try:
        score = score_resume(resume)
        save_score(resume.name, score)
        return {"name": resume.name, "score": score}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
