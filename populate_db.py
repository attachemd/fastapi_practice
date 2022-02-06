import random
from faker import Faker
from sqlalchemy.orm import Session

from db import models
from db.database import get_db, engine
from db.hash import Hash
from db.models import DbArticle, DbUser

models.Base.metadata.create_all(engine)

fakegen = Faker()
db: Session = next(get_db())


def populate_users(n=5):
    for _ in range(n):
        name = fakegen.name()
        first_name = name.split(" ")[0]
        last_name = " ".join(name.split(" ")[-1:])
        username = first_name[0].lower() + last_name.lower().replace(
            " ", ""
        )
        email = username + "@" + last_name.lower() + ".com"
        password = "1234"
        new_user = DbUser(
            username=username,
            email=email,
            password=Hash.bcrypt(password),
        )
        db.add(new_user)
        db.commit()


def populate_articles(n=5):
    for _ in range(n):
        name = fakegen.name()
        print(name)
        new_article = DbArticle(
            title=fakegen.name(),
            content=fakegen.sentence(),
            published=fakegen.boolean(),
            user_id=random.randint(1, 5),
        )
        db.add(new_article)
        db.commit()


def handle():
    print("populating script")
    populate_users()
    populate_articles()
    print("populating complete")


handle()
