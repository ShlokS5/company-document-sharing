from fastapi import FastAPI

app = FastAPI(title="Company Knowledge Hub")

@app.get("/health")
def health_check():
    return {"status": "healthy"}