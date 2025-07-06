from fastapi import FastAPI

app =FastAPI()

@app.get("/")
def blaal():
    return {"msg":"Ola Mundo"}
