from fastapi import FastAPI, Response, status
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from .database import engine

app = FastAPI()

@app.get("/", status_code=200)
def root():
    return {"message": "Beaumont Bank"}

@app.get("/health", status_code=200)
def health_check():
    return {"status": "healthy"}

@app.get("/health/db", status_code=200)
def db_health_check(response: Response):
    try:
        with engine.connect() as connection:
            result = connection.execute(text("select 1"))
    except SQLAlchemyError:
        response.status_code = status.HTTP_503_SERVICE_UNAVAILABLE
        return {"db_status": "unhealthy"}
    else:
        return {"db_status": "healthy"}    
