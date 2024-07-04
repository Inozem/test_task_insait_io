import os

from dotenv import load_dotenv
from flask import Flask

application = Flask(__name__)

load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

SERVER_NAME = os.getenv('SERVER_NAME')
DB_USERNAME = os.getenv('DB_USERNAME')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')


