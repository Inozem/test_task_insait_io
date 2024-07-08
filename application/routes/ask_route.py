from flask import jsonify, request, Response
from werkzeug.exceptions import BadRequest

from configs import application, logger, MESSAGE_MAX_LEN, MESSAGE_MIN_LEN
from database.db_connection import db
from database.models.question_and_answer import QuestionAndAnswer
from llm.gpt import AnswerBot

@application.route("/ask", methods=["POST"])
def get_chats() -> tuple[Response, int]:
    try:
        question = request.get_json()["question"]
        logger.debug(f"Received question: {question}")
        validate_message(question)
        try:
            answer_bot = AnswerBot(llm_model="gpt-4o")
            gpt_answer = answer_bot.get_answer(question=question)
            logger.debug(f"Generated answer: {gpt_answer}")
        except Exception:
            logger.error(f"LLM error: {str(e)}")
            return jsonify({"error": "LLM error."}), 500
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
        logger.info("Question and answer successfully processed")
        return jsonify(question_and_answer), 201
    except BadRequest as e:
        logger.error(f"{str(e)}")
        return jsonify({"error": str(e)}), 400
    except KeyError as e:
        logger.error(f"{str(e)}")
        return jsonify({"error": "The 'question' field is required."}), 400
    except Exception as e:
        logger.error(f"{str(e)}")
        return jsonify({"error": "Server error."}), 500

def validate_message(message: str) -> str:
    if not isinstance(message, str):
        raise BadRequest("The 'question' field must be a string.")
    elif len(message) < MESSAGE_MIN_LEN:
        raise BadRequest(
            "The 'question' field cannot be shorter than "
            f"{MESSAGE_MIN_LEN} character."
        )
    elif len(message) > MESSAGE_MAX_LEN:
        raise BadRequest(
            "The 'question' field cannot be longer than "
            f"{MESSAGE_MAX_LEN} characters."
        )
    return "valid"
