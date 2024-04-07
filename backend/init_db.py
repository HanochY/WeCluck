from config.db import database
from models import *
def init_db():
    database.create_all()