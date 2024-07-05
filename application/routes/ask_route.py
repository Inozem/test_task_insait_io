from flask import jsonify, request

from configs import application
from database.db_connection import db
from database.models.question_and_answer import QuestionAndAnswer
from llm.gpt import AnswerBot

@application.route("/ask", methods=["POST"])
def get_chats():
    if request.data and "question" in request.get_json():
        try:
            question = request.get_json()["question"]
            answer_bot = AnswerBot(llm_model="gpt-4o")
            gpt_answer = answer_bot.get_answer(question=question)
            qa = QuestionAndAnswer(
                question=question,
                answer=gpt_answer
            )
            db.session.add(qa)
            db.session.commit()
            question_and_answer = {
                "question": question,
                "answer": gpt_answer
            }
            return jsonify(question_and_answer), 201
        except Exception:
            return jsonify({"error": "Server error."}), 500
    else:
        error_message = "A question must be in the request."
        return jsonify({"error": error_message}), 400
