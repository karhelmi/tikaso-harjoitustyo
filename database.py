from app import app
from flask_sqlalchemy import SQLAlchemy
from os import getenv

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://karhelmi" #getenv("DATABASE_URL")
database = SQLAlchemy(app)

#as instructed in course material
