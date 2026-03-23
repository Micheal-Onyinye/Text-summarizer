from fastapi import FastAPI
from schema import TextData
from logic import get_summary
import uvicorn

app = FastAPI()


@app.post("/summarize")
async def summarize(data: TextData):
    result = get_summary(data.text, data.max_len, data.min_len)
    return {"summary": result}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)