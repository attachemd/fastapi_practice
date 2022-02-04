from fastapi import FastAPI

from db import models
from db.database import engine
from router import user, article

app = FastAPI()
app.include_router(user.router)
app.include_router(article.router)


@app.get('/hello')
def index():
    return {'message': 'Hello world!'}


models.Base.metadata.create_all(engine)
