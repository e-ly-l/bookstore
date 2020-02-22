from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
async def hello_word():
    return {"Hello Word!"}



# uvicorn run:app --reload
# uvicorn run:app --reload --port 3000