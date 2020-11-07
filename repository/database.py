import os

from dotenv import load_dotenv

from repository.mongo.MongoDB import *

load_dotenv()

USERNAME = os.getenv("USERNAME")
PASS = os.getenv("PASS")
DB_NAME = "Liquid"
COLLECTIONS = {"session": AUTO_INCREMENT}

URL = f"mongodb+srv://{USERNAME}:{PASS}@cluster0.hhjqb.mongodb.net/{DB_NAME}?retryWrites=true&w=majority"
CONNECTION = MongoDB(database=DB_NAME, docs=COLLECTIONS, url=URL)
