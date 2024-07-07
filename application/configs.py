import os

from dotenv import load_dotenv
from flask import Flask

application = Flask(__name__)

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

SERVER_NAME = "db"
DB_USERNAME = "user"
DB_PASSWORD = "password"
DB_NAME = "insait_io"

MESSAGE_MIN_LEN = 1
MESSAGE_MAX_LEN = 4096
