from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"status": "ok", "message": "Hello World"}


@app.get("/evaluate/")
async def evaluate_x_squared(x: int = 0):
    return {"status": "ok", "message": f"The result is {x*x}"}
