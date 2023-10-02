from dotenv import load_dotenv
import os

load_dotenv(".env")

class Config:
    DEBUG = True
    SECRET_KEY = os.getenv("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')


