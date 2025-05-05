# marvel-api/main.py

from fastapi import FastAPI

app = FastAPI(title="Marvel Rivals API")

@app.get("/health")
async def health():
    return {"status": "ok"}
