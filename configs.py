from dotenv import load_dotenv
import os

from flask import Flask

application = Flask(__name__)

load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')


