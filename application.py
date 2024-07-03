from configs import application
from database.db_connection import db
from routes import ask_route


if __name__ == "__main__":
    application.run(debug=True, host="0.0.0.0", port=5000)
