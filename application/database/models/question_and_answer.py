from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from database.db_connection import db


class QuestionAndAnswer(db.Model):
   __tablename__ = "question_and_answer"

   id: Mapped[int] = mapped_column(
      Integer,
      primary_key=True,
      autoincrement=True
   )
   question: Mapped[str] = mapped_column(
      String(length=4096)
   )
   answer: Mapped[str] = mapped_column(
      String(length=4096)
   )
