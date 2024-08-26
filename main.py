from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from prompt import process_claim_question  # Import the function

app = FastAPI()

@app.get("/")
async def read_root():
    return {"🎉 Hello Claims"}

@app.post("/claim-question")
async def claim_question(request: Request) -> JSONResponse:
    data = await request.json()
    question = data.get("question")

    # Use the process_claim_question function from prompt.py
    answer = process_claim_question(question)

    # Return a JSONResponse with status_code 200
    return JSONResponse(
        content={"question": question, "answer": answer},
        status_code=200
    )