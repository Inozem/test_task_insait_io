from flask import jsonify, request

from configs import application
from llm.gpt import AnswerBot

@application.route("/ask", methods=["POST"])
def get_chats():
    if request.data and "question" in request.get_json():
        question = request.get_json()["question"]
        answer_bot = AnswerBot(llm_model="gpt-4o")
        gpt_answer = answer_bot.get_answer(question=question)
        message_info = {
            "question": question,
            "answer": gpt_answer
        }
        return jsonify(message_info), 201
    else:
        error_message = "A question must be in the request."
        return jsonify({"error": error_message}), 400
