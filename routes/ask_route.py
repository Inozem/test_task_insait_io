from flask import jsonify, request

from configs import application
from llm.gpt import AnswerBot

@application.route("/ask", methods=["POST"])
def get_chats():
    data = {}
    if request.data:
        data = request.get_json()
    
    if "question" in data:
        question = data["question"]
        answer_bot = AnswerBot(model="gpt-4o")
        gpt_answer = answer_bot.get_answer(question=question)
        message_info = {
            "question": question,
            "answer": gpt_answer
        }
        return jsonify(message_info), 201
    else:
        error_message = "Question must be in the request."
        return jsonify({"error": error_message}), 400