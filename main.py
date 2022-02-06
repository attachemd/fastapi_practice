from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.responses import JSONResponse

from db import models
from db.database import engine
from exceptions import StoryException
from router import user, article, product

app = FastAPI()


app.include_router(user.router)
app.include_router(article.router)
app.include_router(product.router)


@app.get("/hello")
def index():
    return {"message": "Hello world!"}


@app.exception_handler(StoryException)
def story_exceptions_handler(request: Request, exc: StoryException):
    return JSONResponse(
        status_code=418, content={"detail": exc.name}
    )


models.Base.metadata.create_all(engine)
