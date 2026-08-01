from fastapi import FastAPI
from routes import holdings

app = FastAPI()
app.include_router(holdings.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}