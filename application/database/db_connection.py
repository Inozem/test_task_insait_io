from flask_sqlalchemy import SQLAlchemy

from configs import (application, DB_NAME, DB_PASSWORD, DB_USERNAME,
                     SERVER_NAME)

DB_URL = f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{SERVER_NAME}/{DB_NAME}"
application.config['SQLALCHEMY_DATABASE_URI'] = (DB_URL)

db = SQLAlchemy(application)
